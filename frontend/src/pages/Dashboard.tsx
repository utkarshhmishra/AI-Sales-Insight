import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { useMutation } from '@tanstack/react-query'
import { 
  Search, TrendingUp, Newspaper, DollarSign, Users as UsersIcon, 
  Loader2, Zap, Target, BarChart3, Clock, Award, Briefcase, UserCircle
} from 'lucide-react'
import { insightsApi } from '../services/api'

type Persona = 'sales-rep' | 'sales-manager' | 'business-dev'

export default function Dashboard() {
  const [companyName, setCompanyName] = useState('')
  const [quickMode, setQuickMode] = useState(false)
  const [selectedPersona, setSelectedPersona] = useState<Persona>('sales-rep')
  const navigate = useNavigate()

  const generateMutation = useMutation({
    mutationFn: (data: { company_name: string }) => 
      quickMode 
        ? insightsApi.generateQuickBrief(data)
        : insightsApi.generateInsights({ ...data, timeframe_days: 30, priority: 'high' }),
    onSuccess: () => {
      navigate(`/insights/${encodeURIComponent(companyName)}`)
    },
  })

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (companyName.trim()) {
      generateMutation.mutate({ company_name: companyName })
    }
  }

  const personas = [
    { 
      id: 'sales-rep' as Persona, 
      name: 'Sales Rep', 
      icon: <UserCircle className="h-5 w-5" />,
      description: 'Quick prep for meetings',
      color: 'blue'
    },
    { 
      id: 'sales-manager' as Persona, 
      name: 'Sales Manager', 
      icon: <Briefcase className="h-5 w-5" />,
      description: 'Team insights & trends',
      color: 'purple'
    },
    { 
      id: 'business-dev' as Persona, 
      name: 'Business Dev', 
      icon: <Target className="h-5 w-5" />,
      description: 'Strategic opportunities',
      color: 'green'
    },
  ]

  const demoCompanies = [
    'Microsoft',
    'Salesforce',
    'Adobe',
    'TechStart India'
  ]

  const getPersonaContent = () => {
    switch(selectedPersona) {
      case 'sales-rep':
        return {
          tagline: 'Close deals faster with AI-powered insights',
          description: 'Get personalized talking points, recent company news, and decision-maker insights in seconds.'
        }
      case 'sales-manager':
        return {
          tagline: 'Empower your team with intelligence',
          description: 'Track trends, monitor pipeline health, and provide your reps with the best insights.'
        }
      case 'business-dev':
        return {
          tagline: 'Identify strategic opportunities',
          description: 'Discover partnerships, investment trends, and market positioning for better decisions.'
        }
    }
  }

  const personaContent = getPersonaContent()

  return (
    <div className="space-y-12 animate-in fade-in duration-500">
      {/* Hero Section */}
      <div className="text-center space-y-6">
        <div className="inline-flex items-center px-4 py-2 bg-blue-50 dark:bg-blue-900/30 border border-blue-200 dark:border-blue-800 rounded-full text-blue-700 dark:text-blue-300 text-sm font-medium animate-in slide-in-from-top">
          <Zap className="h-4 w-4 mr-2" />
          95% Faster Research • 2-3 Minutes vs 1-4 Hours
        </div>
        
        <h1 className="text-5xl md:text-6xl font-extrabold text-gray-900 dark:text-white mb-4 animate-in slide-in-from-bottom">
          {personaContent.tagline}
        </h1>
        
        <p className="text-xl text-gray-600 dark:text-gray-400 max-w-3xl mx-auto animate-in slide-in-from-bottom animation-delay-100">
          {personaContent.description}
        </p>

        {/* Persona Selector */}
        <div className="flex flex-wrap justify-center gap-3 pt-4">
          {personas.map((persona) => (
            <button
              key={persona.id}
              onClick={() => setSelectedPersona(persona.id)}
              className={`
                flex items-center px-5 py-3 rounded-xl font-medium transition-all duration-200 transform hover:scale-105
                ${selectedPersona === persona.id
                  ? `bg-${persona.color}-600 text-white shadow-lg dark:bg-${persona.color}-500`
                  : 'bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 shadow'
                }
              `}
            >
              {persona.icon}
              <span className="ml-2">{persona.name}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Search Section */}
      <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl p-8 md:p-10 border border-gray-100 dark:border-gray-700 hover:shadow-2xl transition-shadow duration-300">
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label htmlFor="company" className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-3">
              Company Name
            </label>
            <div className="relative group">
              <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 h-5 w-5 text-gray-400 group-focus-within:text-blue-500 transition-colors" />
              <input
                id="company"
                type="text"
                value={companyName}
                onChange={(e) => setCompanyName(e.target.value)}
                placeholder="Enter company name (e.g., Microsoft, Salesforce)"
                className="w-full pl-12 pr-4 py-4 bg-gray-50 dark:bg-gray-700 border-2 border-gray-200 dark:border-gray-600 text-gray-900 dark:text-white rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                disabled={generateMutation.isPending}
                autoFocus
              />
            </div>
          </div>

          <div className="flex items-center p-4 bg-yellow-50 dark:bg-yellow-900/20 border border-yellow-200 dark:border-yellow-800 rounded-xl">
            <input
              id="quick-mode"
              type="checkbox"
              checked={quickMode}
              onChange={(e) => setQuickMode(e.target.checked)}
              className="h-5 w-5 text-blue-600 focus:ring-blue-500 border-gray-300 rounded cursor-pointer"
            />
            <label htmlFor="quick-mode" className="ml-3 block text-sm font-medium text-gray-900 dark:text-gray-100 cursor-pointer">
              <span className="inline-flex items-center">
                <Zap className="h-4 w-4 mr-2 text-yellow-600 dark:text-yellow-400" />
                Quick Brief Mode <span className="ml-1 text-gray-600 dark:text-gray-400">(30 sec response, essential info only)</span>
              </span>
            </label>
          </div>

          <button
            type="submit"
            disabled={generateMutation.isPending || !companyName.trim()}
            className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white py-4 px-8 rounded-xl font-semibold text-lg shadow-lg hover:shadow-xl disabled:from-gray-400 disabled:to-gray-400 disabled:cursor-not-allowed flex items-center justify-center transition-all duration-200 transform hover:scale-[1.02] active:scale-[0.98]"
          >
            {generateMutation.isPending ? (
              <>
                <Loader2 className="animate-spin h-6 w-6 mr-3" />
                Generating Insights...
              </>
            ) : (
              <>
                <Search className="h-6 w-6 mr-3" />
                Generate Insights
              </>
            )}
          </button>

          {generateMutation.isError && (
            <div className="bg-red-50 dark:bg-red-900/30 border-2 border-red-200 dark:border-red-800 text-red-700 dark:text-red-300 px-5 py-4 rounded-xl flex items-center animate-in slide-in-from-top">
              <span className="font-medium">Error generating insights. Please try again.</span>
            </div>
          )}
        </form>

        {/* Demo Companies */}
        <div className="mt-8 pt-6 border-t-2 border-gray-200 dark:border-gray-700">
          <p className="text-sm font-semibold text-gray-700 dark:text-gray-300 mb-4">Try with demo companies:</p>
          <div className="flex flex-wrap gap-3">
            {demoCompanies.map((company, idx) => (
              <button
                key={company}
                onClick={() => setCompanyName(company)}
                className="px-5 py-2.5 bg-gradient-to-r from-gray-100 to-gray-200 dark:from-gray-700 dark:to-gray-600 hover:from-blue-50 hover:to-purple-50 dark:hover:from-blue-900/30 dark:hover:to-purple-900/30 text-gray-800 dark:text-gray-200 text-sm font-medium rounded-lg border border-gray-300 dark:border-gray-600 hover:border-blue-400 dark:hover:border-blue-500 transition-all duration-200 transform hover:scale-105 hover:shadow-md"
                style={{ animationDelay: `${idx * 100}ms` }}
              >
                {company}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Features Grid */}
      <div>
        <h2 className="text-3xl font-bold text-gray-900 dark:text-white mb-6 text-center">
          Multi-Agent Intelligence System
        </h2>
        <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <FeatureCard
            icon={<TrendingUp className="h-10 w-10" />}
            title="Research Agent"
            description="Company background, decision-makers, and organizational insights"
            color="blue"
            delay={0}
          />
          <FeatureCard
            icon={<Newspaper className="h-10 w-10" />}
            title="News Agent"
            description="Recent news, announcements, and press releases"
            color="green"
            delay={100}
          />
          <FeatureCard
            icon={<DollarSign className="h-10 w-10" />}
            title="Financial Agent"
            description="Stock performance, funding, and financial metrics"
            color="purple"
            delay={200}
          />
          <FeatureCard
            icon={<UsersIcon className="h-10 w-10" />}
            title="Social Media Agent"
            description="LinkedIn activity, Twitter engagement, and sentiment"
            color="orange"
            delay={300}
          />
        </div>
      </div>

      {/* Stats Section */}
      <div className="relative bg-gradient-to-br from-blue-600 via-purple-600 to-pink-600 rounded-2xl shadow-2xl p-8 md:p-12 text-white overflow-hidden">
        <div className="absolute inset-0 bg-grid-white/10 [mask-image:linear-gradient(0deg,white,rgba(255,255,255,0.5))]"></div>
        <div className="relative">
          <div className="text-center mb-10">
            <Award className="h-12 w-12 mx-auto mb-4 animate-bounce" />
            <h2 className="text-3xl md:text-4xl font-extrabold mb-3">Success Metrics</h2>
            <p className="text-blue-100 text-lg">Real results from real customers</p>
          </div>
          <div className="grid md:grid-cols-3 gap-8">
            <StatCard
              icon={<Clock className="h-8 w-8" />}
              value="95%"
              label="Reduction in prep time"
              subtext="2-3 min vs 60-240 min"
            />
            <StatCard
              icon={<BarChart3 className="h-8 w-8" />}
              value="15%"
              label="Improvement in conversion"
              subtext="Better qualified leads"
            />
            <StatCard
              icon={<Target className="h-8 w-8" />}
              value="10%"
              label="Faster pipeline velocity"
              subtext="Accelerated deal cycles"
            />
          </div>
        </div>
      </div>
    </div>
  )
}

function FeatureCard({ 
  icon, 
  title, 
  description, 
  color,
  delay 
}: { 
  icon: React.ReactNode; 
  title: string; 
  description: string; 
  color: string;
  delay: number;
}) {
  const colorClasses = {
    blue: 'from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700',
    green: 'from-green-500 to-green-600 hover:from-green-600 hover:to-green-700',
    purple: 'from-purple-500 to-purple-600 hover:from-purple-600 hover:to-purple-700',
    orange: 'from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700',
  }

  return (
    <div 
      className="group bg-white dark:bg-gray-800 rounded-2xl shadow-lg hover:shadow-2xl p-6 border-2 border-gray-100 dark:border-gray-700 hover:border-transparent transition-all duration-300 transform hover:scale-105 hover:-translate-y-1 animate-in fade-in slide-in-from-bottom"
      style={{ animationDelay: `${delay}ms` }}
    >
      <div className={`inline-flex p-3 rounded-xl bg-gradient-to-br ${colorClasses[color as keyof typeof colorClasses]} text-white mb-4 shadow-lg group-hover:scale-110 transition-transform`}>
        {icon}
      </div>
      <h3 className="text-xl font-bold text-gray-900 dark:text-white mb-3">{title}</h3>
      <p className="text-sm text-gray-600 dark:text-gray-400 leading-relaxed">{description}</p>
    </div>
  )
}

function StatCard({ 
  icon, 
  value, 
  label, 
  subtext 
}: { 
  icon: React.ReactNode; 
  value: string; 
  label: string; 
  subtext: string;
}) {
  return (
    <div className="text-center group">
      <div className="inline-flex items-center justify-center mb-3 opacity-80 group-hover:opacity-100 transition-opacity">
        {icon}
      </div>
      <div className="text-5xl md:text-6xl font-extrabold mb-3 group-hover:scale-110 transition-transform">{value}</div>
      <div className="text-xl font-semibold mb-1">{label}</div>
      <div className="text-blue-100 text-sm">{subtext}</div>
    </div>
  )
}
