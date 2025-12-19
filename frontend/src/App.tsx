import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import InsightsPage from './pages/InsightsPage'
import Layout from './components/Layout'
import { ThemeProvider } from './contexts/ThemeContext'

function App() {
  return (
    <ThemeProvider>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/insights/:companyName" element={<InsightsPage />} />
          </Routes>
        </Layout>
      </Router>
    </ThemeProvider>
  )
}

export default App
