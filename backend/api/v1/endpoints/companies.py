"""
Companies API Endpoints
Manage company information and tracking
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

router = APIRouter()


class Company(BaseModel):
    """Company model"""
    name: str
    industry: Optional[str] = None
    website: Optional[str] = None
    added_date: datetime = Field(default_factory=datetime.now)
    tracked: bool = False


class CompanyCreate(BaseModel):
    """Create company request"""
    name: str = Field(..., min_length=2, max_length=200)
    industry: Optional[str] = None
    website: Optional[str] = None
    tracked: bool = False


# In-memory storage (replace with database in production)
companies_db: List[Company] = []


@router.post("/", response_model=Company)
async def create_company(company: CompanyCreate):
    """
    Add a new company to track
    """
    new_company = Company(**company.dict())
    companies_db.append(new_company)
    
    return new_company


@router.get("/", response_model=List[Company])
async def list_companies(tracked_only: bool = False):
    """
    List all companies
    
    - **tracked_only**: If true, only return tracked companies
    """
    if tracked_only:
        return [c for c in companies_db if c.tracked]
    return companies_db


@router.get("/{company_name}")
async def get_company(company_name: str):
    """
    Get details for a specific company
    """
    company = next((c for c in companies_db if c.name.lower() == company_name.lower()), None)
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    return company


@router.put("/{company_name}/track")
async def track_company(company_name: str, tracked: bool = True):
    """
    Enable/disable tracking for a company
    """
    company = next((c for c in companies_db if c.name.lower() == company_name.lower()), None)
    
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    
    company.tracked = tracked
    
    return {
        "success": True,
        "message": f"Company {company_name} tracking {'enabled' if tracked else 'disabled'}"
    }


@router.delete("/{company_name}")
async def delete_company(company_name: str):
    """
    Remove a company from the system
    """
    global companies_db
    initial_count = len(companies_db)
    companies_db = [c for c in companies_db if c.name.lower() != company_name.lower()]
    
    if len(companies_db) == initial_count:
        raise HTTPException(status_code=404, detail="Company not found")
    
    return {
        "success": True,
        "message": f"Company {company_name} deleted"
    }
