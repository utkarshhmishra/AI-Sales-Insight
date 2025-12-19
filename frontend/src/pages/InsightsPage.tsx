import { useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { 
  Loader2, TrendingUp, Newspaper, DollarSign, Users, Lightbulb, 
  CheckCircle, AlertTriangle, ArrowLeft, Download, Share2, 
  Copy, Check, Star, Clock, Target
} from 'lucide-react'
import { insightsApi } from '../services/api'

export default function InsightsPage() {
  const { companyName } = useParams<{ companyName: string }>()
  const [copied, setCopied] = useState(false)
  const [expandedSections, setExpandedSections] = useState<Record<string, boolean>>({
    summary: true,
    talking: true,
    opportunities: true,
    agents: true,
    risks: true
  })

  const { data, isLoading, error } = useQuery({
    queryKey: ['insights', companyName],
    queryFn: () => insightsApi.generateInsights({
      company_name: companyName!,
      timeframe_days: 30,
      priority: 'high'
    }),
    enabled: !!companyName,
  })

  const handleCopy = () => {
    // Copy summary to clipboard
    if (data?.data?.data?.synthesis?.data?.executive_summary) {
      navigator.clipboard.writeText(data.data.data.synthesis.data.executive_summary)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    }
  }

  const toggleSection = (section: string) => {
    setExpandedSections(prev => ({ ...prev, [section]: !prev[section] }))
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-[500px]">
        <div className="text-center space-y-6 animate-in fade-in">
          <div className="relative">
            <Loader2 className="h-16 w-16 animate-spin text-blue-600 mx-auto" />
            <div className="absolute inset-0 h-16 w-16 bg-blue-400 blur-2xl opacity-20 mx-auto animate-pulse"></div>
          </div>
          <div>
            <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-3">
              Generating Insights for {companyName}
            </h2>
            <p className="text-gray-600 dark:text-gray-400 mb-4">
              Our AI agents are gathering data from multiple sources...
            </p>
            <div className="flex items-center justify-center space-x-2 text-sm text-gray-500 dark:text-gray-400">
              <Clock className="h-4 w-4 animate-pulse" />
              <span>Estimated time: 2-3 seconds</span>
            </div>
          </div>
          
          {/* Loading progress */}
          <div className="max-w-md mx-auto space-y-3">
            <LoadingStep label="Research Agent" delay={0} />
            <LoadingStep label="News Agent" delay={200} />
            <LoadingStep label="Financial Agent" delay={400} />
            <LoadingStep label="Social Media Agent" delay={600} />
            <LoadingStep label="Synthesizing Insights" delay={800} />
          </div>
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="bg-red-50 dark:bg-red-900/20 border-2 border-red-200 dark:border-red-800 rounded-2xl p-8 animate-in slide-in-from-top">
        <AlertTriangle className="h-12 w-12 text-red-600 dark:text-red-400 mx-auto mb-4" />
        <h2 className="text-2xl font-bold text-red-900 dark:text-red-100 mb-2 text-center">Error Loading Insights</h2>
        <p className="text-red-700 dark:text-red-300 text-center mb-6">Failed to generate insights. Please try again.</p>
        <Link 
          to="/"
          className="flex items-center justify-center px-6 py-3 bg-red-600 hover:bg-red-700 text-white rounded-lg font-medium mx-auto w-fit transition-colors"
        >
          <ArrowLeft className="h-4 w-4 mr-2" />
          Back to Dashboard
        </Link>
      </div>
    )
  }

  const insightData = data?.data?.data
  const synthesis = insightData?.synthesis?.data
  const agentOutputs = insightData?.agent_outputs

  return (
    <div className="space-y-8 animate-in fade-in duration-700">
      {/* Back Button */}
      <Link
        to="/"
        className="inline-flex items-center text-gray-600 dark:text-gray-400 hover:text-gray-900 dark:hover:text-white transition-colors group"
      >
        <ArrowLeft className="h-4 w-4 mr-2 group-hover:-translate-x-1 transition-transform" />
        Back to Dashboard
      </Link>

      {/* Header */}
      <div className="bg-gradient-to-br from-white to-gray-50 dark:from-gray-800 dark:to-gray-900 rounded-2xl shadow-xl p-8 border-2 border-gray-100 dark:border-gray-700">
        <div className="flex items-start justify-between mb-4">
          <div className="flex-1">
            <h1 className="text-4xl font-extrabold text-gray-900 dark:text-white mb-3 flex items-center">
              {companyName}
              {synthesis?.meeting_preparation_score && (
                <div className="ml-4 inline-flex items-center px-4 py-2 bg-gradient-to-r from-green-500 to-emerald-500 text-white rounded-full text-sm font-medium shadow-lg">
                  <Star className="h-4 w-4 mr-1" />
                  {synthesis.meeting_preparation_score.percentage}% Ready
                </div>
              )}
            </h1>
            <div className="flex flex-wrap items-center gap-4 text-sm text-gray-600 dark:text-gray-400">
              <span className="inline-flex items-center">
                <Clock className="h-4 w-4 mr-1" />
                {new Date(insightData?.timestamp).toLocaleString()}
              </span>
              <span>•</span>
              <span className="inline-flex items-center font-semibold text-blue-600 dark:text-blue-400">
                <Target className="h-4 w-4 mr-1" />
                Executed in {insightData?.execution_time_ms}ms
              </span>
            </div>
          </div>
          
          {/* Action Buttons */}
          <div className="flex items-center space-x-2">
            <button
              onClick={handleCopy}
              className="p-3 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg transition-colors"
              title="Copy summary"
            >
              {copied ? <Check className="h-5 w-5 text-green-600" /> : <Copy className="h-5 w-5 text-gray-600 dark:text-gray-400" />}
            </button>
            <button className="p-3 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg transition-colors" title="Share">
              <Share2 className="h-5 w-5 text-gray-600 dark:text-gray-400" />
            </button>
            <button className="p-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg transition-colors" title="Download">
              <Download className="h-5 w-5" />
            </button>
          </div>
        </div>
      </div>

      {/* Executive Summary */}
      {synthesis?.executive_summary && (
        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 border-2 border-yellow-100 dark:border-yellow-900/30 hover:shadow-2xl transition-shadow animate-in slide-in-from-bottom">
          <button
            onClick={() => toggleSection('summary')}
            className="w-full flex items-center justify-between mb-6 group"
          >
            <h2 className="text-3xl font-bold text-gray-900 dark:text-white flex items-center">
              <div className="p-3 bg-gradient-to-br from-yellow-400 to-orange-500 rounded-xl mr-3 shadow-lg group-hover:scale-110 transition-transform">
                <Lightbulb className="h-7 w-7 text-white" />
              </div>
              Executive Summary
            </h2>
            <div className={`transform transition-transform ${expandedSections.summary ? 'rotate-180' : ''}`}>
              <svg className="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </button>
          
          {expandedSections.summary && (
            <div className="prose max-w-none animate-in slide-in-from-top">
              <div className="p-6 bg-gradient-to-br from-yellow-50 to-orange-50 dark:from-yellow-900/10 dark:to-orange-900/10 rounded-xl border border-yellow-200 dark:border-yellow-800">
                <pre className="whitespace-pre-wrap font-sans text-gray-800 dark:text-gray-200 leading-relaxed text-base">
                  {synthesis.executive_summary}
                </pre>
              </div>
            </div>
          )}
        </div>
      )}

      {/* Talking Points */}
      {synthesis?.talking_points && synthesis.talking_points.length > 0 && (
        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 border-2 border-green-100 dark:border-green-900/30 hover:shadow-2xl transition-shadow animate-in slide-in-from-bottom animation-delay-100">
          <button
            onClick={() => toggleSection('talking')}
            className="w-full flex items-center justify-between mb-6 group"
          >
            <h2 className="text-3xl font-bold text-gray-900 dark:text-white flex items-center">
              <div className="p-3 bg-gradient-to-br from-green-400 to-emerald-500 rounded-xl mr-3 shadow-lg group-hover:scale-110 transition-transform">
                <CheckCircle className="h-7 w-7 text-white" />
              </div>
              Key Talking Points
            </h2>
            <div className={`transform transition-transform ${expandedSections.talking ? 'rotate-180' : ''}`}>
              <svg className="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
              </svg>
            </div>
          </button>
          
          {expandedSections.talking && (
            <ul className="space-y-4 animate-in slide-in-from-top">
              {synthesis.talking_points.map((point: string, index: number) => (
                <li 
                  key={index} 
                  className="flex items-start p-4 bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-900/10 dark:to-emerald-900/10 rounded-xl border border-green-200 dark:border-green-800 hover:border-green-400 dark:hover:border-green-600 transition-colors group"
                  style={{ animationDelay: `${index * 50}ms` }}
                >
                  <span className="inline-flex items-center justify-center w-8 h-8 bg-gradient-to-br from-green-500 to-emerald-600 text-white rounded-full text-sm font-bold mr-4 flex-shrink-0 shadow-lg group-hover:scale-110 transition-transform">
                    {index + 1}
                  </span>
                  <span className="text-gray-800 dark:text-gray-200 leading-relaxed">{point}</span>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}

      {/* Opportunities */}
      {synthesis?.opportunities && synthesis.opportunities.length > 0 && (
        <div className="bg-green-50 border border-green-200 rounded-lg p-6">
          <h2 className="text-xl font-bold text-gray-900 mb-4">🎯 Opportunities</h2>
          <div className="grid gap-4">
            {synthesis.opportunities.map((opp: any, index: number) => (
              <div key={index} className="bg-white p-4 rounded-lg">
                <h3 className="font-semibold text-gray-900">{opp.opportunity}</h3>
                <p className="text-sm text-gray-600 mt-1">{opp.description}</p>
                <div className="flex items-center mt-2 space-x-4 text-sm">
                  <span className="text-green-600">Confidence: {opp.confidence}</span>
                  <span className="text-blue-600">Value: {opp.potential_value}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Agent Outputs Grid */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Research */}
        {agentOutputs?.research && (
          <AgentCard
            title="Research Agent"
            icon={<TrendingUp className="h-6 w-6 text-blue-600" />}
            insights={agentOutputs.research.insights || []}
            status={agentOutputs.research.status}
          />
        )}

        {/* News */}
        {agentOutputs?.news && (
          <AgentCard
            title="News Agent"
            icon={<Newspaper className="h-6 w-6 text-green-600" />}
            insights={agentOutputs.news.insights || []}
            status={agentOutputs.news.status}
          />
        )}

        {/* Financial */}
        {agentOutputs?.financial && (
          <AgentCard
            title="Financial Agent"
            icon={<DollarSign className="h-6 w-6 text-purple-600" />}
            insights={agentOutputs.financial.insights || []}
            status={agentOutputs.financial.status}
          />
        )}

        {/* Social Media */}
        {agentOutputs?.social_media && (
          <AgentCard
            title="Social Media Agent"
            icon={<Users className="h-6 w-6 text-orange-600" />}
            insights={agentOutputs.social_media.insights || []}
            status={agentOutputs.social_media.status}
          />
        )}
      </div>

      {/* Risks */}
      {synthesis?.risks && synthesis.risks.length > 0 && (
        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-6">
          <h2 className="text-xl font-bold text-gray-900 mb-4 flex items-center">
            <AlertTriangle className="h-5 w-5 mr-2 text-yellow-600" />
            Potential Risks & Mitigation
          </h2>
          <div className="grid gap-4">
            {synthesis.risks.map((risk: any, index: number) => (
              <div key={index} className="bg-white p-4 rounded-lg">
                <h3 className="font-semibold text-gray-900">{risk.risk}</h3>
                <p className="text-sm text-gray-600 mt-1">{risk.description}</p>
                <div className="mt-2 text-sm">
                  <span className="text-yellow-700 font-medium">Mitigation: </span>
                  <span className="text-gray-700">{risk.mitigation}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function AgentCard({ title, icon, insights, status }: any) {
  const [expanded, setExpanded] = useState(false)
  
  return (
    <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg hover:shadow-xl p-6 border-2 border-gray-100 dark:border-gray-700 hover:border-blue-300 dark:hover:border-blue-600 transition-all group">
      <div className="flex items-center mb-4">
        <div className="p-2 bg-gradient-to-br from-blue-50 to-purple-50 dark:from-blue-900/30 dark:to-purple-900/30 rounded-lg group-hover:scale-110 transition-transform">
          {icon}
        </div>
        <h3 className="text-lg font-bold text-gray-900 dark:text-white ml-3">{title}</h3>
        <span className={`ml-auto px-3 py-1 text-xs font-semibold rounded-full ${
          status === 'success' 
            ? 'bg-green-100 dark:bg-green-900/30 text-green-800 dark:text-green-400' 
            : 'bg-gray-100 dark:bg-gray-700 text-gray-800 dark:text-gray-400'
        }`}>
          {status}
        </span>
      </div>
      <ul className="space-y-3">
        {insights.slice(0, expanded ? insights.length : 5).map((insight: string, index: number) => (
          <li key={index} className="text-sm text-gray-700 dark:text-gray-300 flex items-start group/item">
            <span className="mr-3 text-blue-500 font-bold">•</span>
            <span className="group-hover/item:text-gray-900 dark:group-hover/item:text-white transition-colors">{insight}</span>
          </li>
        ))}
      </ul>
      {insights.length > 5 && (
        <button
          onClick={() => setExpanded(!expanded)}
          className="mt-4 text-sm font-medium text-blue-600 dark:text-blue-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors"
        >
          {expanded ? 'Show Less' : `Show ${insights.length - 5} More`}
        </button>
      )}
    </div>
  )
}

function LoadingStep({ label, delay }: { label: string; delay: number }) {
  return (
    <div 
      className="flex items-center space-x-3 animate-in slide-in-from-left"
      style={{ animationDelay: `${delay}ms` }}
    >
      <Loader2 className="h-4 w-4 animate-spin text-blue-600" />
      <span className="text-sm text-gray-600 dark:text-gray-400">{label}</span>
    </div>
  )
}
