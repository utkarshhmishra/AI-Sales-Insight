import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1'

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

export interface InsightRequest {
  company_name: string
  timeframe_days?: number
  priority?: 'low' | 'medium' | 'high'
  context?: Record<string, any>
}

export interface QuickBriefRequest {
  company_name: string
}

export const insightsApi = {
  generateInsights: (data: InsightRequest) =>
    api.post('/insights/generate', data),
  
  generateQuickBrief: (data: QuickBriefRequest) =>
    api.post('/insights/quick-brief', data),
  
  getHistory: (companyName: string, limit: number = 10) =>
    api.get(`/insights/history/${companyName}`, { params: { limit } }),
  
  clearCache: (companyName: string) =>
    api.delete(`/insights/cache/${companyName}`),
}

export const companiesApi = {
  listCompanies: (trackedOnly: boolean = false) =>
    api.get('/companies/', { params: { tracked_only: trackedOnly } }),
  
  getCompany: (companyName: string) =>
    api.get(`/companies/${companyName}`),
  
  createCompany: (data: { name: string; industry?: string; website?: string; tracked?: boolean }) =>
    api.post('/companies/', data),
  
  trackCompany: (companyName: string, tracked: boolean = true) =>
    api.put(`/companies/${companyName}/track`, null, { params: { tracked } }),
  
  deleteCompany: (companyName: string) =>
    api.delete(`/companies/${companyName}`),
}

export const agentsApi = {
  getStatus: () => api.get('/agents/status'),
  getCapabilities: () => api.get('/agents/capabilities'),
  getMetrics: () => api.get('/agents/metrics'),
}

export const healthApi = {
  check: () => api.get('/health/'),
  detailedCheck: () => api.get('/health/detailed'),
}

export default api
