"""
LLM Service for AI Sales Insight
Provides unified interface for OpenAI, Anthropic, and local models
"""

import os
from typing import Optional, Dict, Any, AsyncGenerator
import logging
from enum import Enum

logger = logging.getLogger(__name__)


class LLMProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    OLLAMA = "ollama"


class LLMService:
    """Service for interacting with various LLM providers"""
    
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        # Determine which provider to use
        self.provider = self._determine_provider()
        self.client = None
        
        if self.provider:
            self._initialize_client()
    
    def _determine_provider(self) -> Optional[LLMProvider]:
        """Determine which LLM provider to use based on available API keys"""
        if self.openai_api_key:
            logger.info("Using OpenAI as LLM provider")
            return LLMProvider.OPENAI
        elif self.anthropic_api_key:
            logger.info("Using Anthropic as LLM provider")
            return LLMProvider.ANTHROPIC
        else:
            logger.info("Using Ollama (local) as LLM provider")
            return LLMProvider.OLLAMA
    
    def _initialize_client(self):
        """Initialize the appropriate LLM client"""
        try:
            if self.provider == LLMProvider.OPENAI:
                from openai import AsyncOpenAI
                self.client = AsyncOpenAI(api_key=self.openai_api_key)
                logger.info("OpenAI client initialized")
                
            elif self.provider == LLMProvider.ANTHROPIC:
                from anthropic import AsyncAnthropic
                self.client = AsyncAnthropic(api_key=self.anthropic_api_key)
                logger.info("Anthropic client initialized")
                
            elif self.provider == LLMProvider.OLLAMA:
                # Ollama uses HTTP requests - we'll implement as needed
                logger.info("Ollama client will use HTTP requests")
                
        except ImportError as e:
            logger.warning(f"Failed to import LLM client: {e}. Install with: pip install openai anthropic")
            self.client = None
    
    async def generate_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 2000,
        stream: bool = False
    ) -> str:
        """
        Generate a completion from the LLM
        
        Args:
            prompt: The user prompt
            system_prompt: Optional system prompt
            temperature: Sampling temperature (0-1)
            max_tokens: Maximum tokens to generate
            stream: Whether to stream the response
            
        Returns:
            Generated text response
        """
        if not self.client:
            logger.warning("No LLM client available, using fallback")
            return await self._fallback_generation(prompt)
        
        try:
            if self.provider == LLMProvider.OPENAI:
                return await self._generate_openai(prompt, system_prompt, temperature, max_tokens, stream)
            elif self.provider == LLMProvider.ANTHROPIC:
                return await self._generate_anthropic(prompt, system_prompt, temperature, max_tokens, stream)
            elif self.provider == LLMProvider.OLLAMA:
                return await self._generate_ollama(prompt, system_prompt, temperature, max_tokens, stream)
        except Exception as e:
            logger.error(f"Error generating completion: {e}")
            return await self._fallback_generation(prompt)
        
        return await self._fallback_generation(prompt)
    
    async def _generate_openai(
        self,
        prompt: str,
        system_prompt: Optional[str],
        temperature: float,
        max_tokens: int,
        stream: bool
    ) -> str:
        """Generate completion using OpenAI"""
        from openai import AsyncOpenAI
        
        if not isinstance(self.client, AsyncOpenAI):
            return await self._fallback_generation(prompt)
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = await self.client.chat.completions.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4o"),
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False  # Force non-streaming for simplicity
        )
        
        return response.choices[0].message.content or ""
    
    async def _generate_anthropic(
        self,
        prompt: str,
        system_prompt: Optional[str],
        temperature: float,
        max_tokens: int,
        stream: bool
    ) -> str:
        """Generate completion using Anthropic Claude"""
        try:
            from anthropic import AsyncAnthropic
        except ImportError:
            return await self._fallback_generation(prompt)
        
        if not isinstance(self.client, AsyncAnthropic):
            return await self._fallback_generation(prompt)
        
        # Type ignore for Anthropic API - it's correctly typed but linter doesn't see it
        response = await self.client.messages.create(  # type: ignore
            model=os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022"),
            system=system_prompt or "",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=False  # Force non-streaming
        )
        
        return response.content[0].text
    
    async def _generate_ollama(
        self,
        prompt: str,
        system_prompt: Optional[str],
        temperature: float,
        max_tokens: int,
        stream: bool
    ) -> str:
        """Generate completion using Ollama (local)"""
        import aiohttp
        
        url = f"{self.ollama_base_url}/api/generate"
        
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"
        
        payload = {
            "model": os.getenv("OLLAMA_MODEL", "llama3.2"),
            "prompt": full_prompt,
            "temperature": temperature,
            "stream": stream
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                result = await response.json()
                return result.get("response", "")
    
    async def _fallback_generation(self, prompt: str) -> str:
        """Fallback when no LLM is available - return structured template"""
        logger.info("Using fallback generation (no LLM available)")
        return f"[Template Response] Analysis for the provided context would appear here. Configure OPENAI_API_KEY or ANTHROPIC_API_KEY in .env for AI-powered insights."
    
    async def generate_structured_output(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        output_schema: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate structured JSON output
        
        Args:
            prompt: The user prompt
            system_prompt: Optional system prompt
            output_schema: JSON schema for structured output
            
        Returns:
            Structured dictionary
        """
        # Add JSON formatting instruction
        json_instruction = "\n\nProvide your response in valid JSON format."
        if output_schema:
            json_instruction += f"\n\nFollow this schema: {output_schema}"
        
        response = await self.generate_completion(
            prompt=prompt + json_instruction,
            system_prompt=system_prompt,
            temperature=0.3  # Lower temperature for structured output
        )
        
        # Parse JSON response
        import json
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown code blocks
            import re
            json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', response, re.DOTALL)
            if json_match:
                return json.loads(json_match.group(1))
            
            logger.warning("Failed to parse structured output, returning raw response")
            return {"raw_response": response}


# Singleton instance
_llm_service = None


def get_llm_service() -> LLMService:
    """Get or create LLM service singleton"""
    global _llm_service
    if _llm_service is None:
        _llm_service = LLMService()
    return _llm_service
