import { ReactNode, useState } from 'react'
import { Link } from 'react-router-dom'
import { Sparkles, LayoutDashboard, Users, Settings, Moon, Sun, Menu, X } from 'lucide-react'
import { useTheme } from '../contexts/ThemeContext'

interface LayoutProps {
  children: ReactNode
}

export default function Layout({ children }: LayoutProps) {
  const { theme, toggleTheme } = useTheme()
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900 transition-colors duration-200">
      {/* Header */}
      <header className="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 sticky top-0 z-50 shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <Link to="/" className="flex items-center group">
              <div className="relative">
                <Sparkles className="h-8 w-8 text-blue-600 dark:text-blue-400 group-hover:scale-110 transition-transform" />
                <div className="absolute inset-0 bg-blue-400 blur-xl opacity-0 group-hover:opacity-30 transition-opacity"></div>
              </div>
              <span className="ml-2 text-xl font-bold text-gray-900 dark:text-white">
                AI Sales Insight
              </span>
            </Link>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex items-center space-x-1">
              <Link
                to="/"
                className="inline-flex items-center px-4 py-2 rounded-lg text-sm font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
              >
                <LayoutDashboard className="h-4 w-4 mr-2" />
                Dashboard
              </Link>
              <a
                href="#companies"
                className="inline-flex items-center px-4 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
              >
                <Users className="h-4 w-4 mr-2" />
                Companies
              </a>
              <a
                href="#settings"
                className="inline-flex items-center px-4 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 hover:text-gray-900 dark:hover:text-gray-100 transition-colors"
              >
                <Settings className="h-4 w-4 mr-2" />
                Settings
              </a>
              
              {/* Theme Toggle */}
              <button
                onClick={toggleTheme}
                className="ml-4 p-2 rounded-lg bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors"
                aria-label="Toggle theme"
              >
                {theme === 'light' ? (
                  <Moon className="h-5 w-5 text-gray-700 dark:text-gray-300" />
                ) : (
                  <Sun className="h-5 w-5 text-gray-700 dark:text-gray-300" />
                )}
              </button>
            </nav>

            {/* Mobile menu button */}
            <div className="flex md:hidden items-center space-x-2">
              <button
                onClick={toggleTheme}
                className="p-2 rounded-lg bg-gray-100 dark:bg-gray-700"
                aria-label="Toggle theme"
              >
                {theme === 'light' ? (
                  <Moon className="h-5 w-5 text-gray-700 dark:text-gray-300" />
                ) : (
                  <Sun className="h-5 w-5 text-gray-700 dark:text-gray-300" />
                )}
              </button>
              <button
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                className="p-2 rounded-lg bg-gray-100 dark:bg-gray-700"
              >
                {mobileMenuOpen ? (
                  <X className="h-6 w-6 text-gray-700 dark:text-gray-300" />
                ) : (
                  <Menu className="h-6 w-6 text-gray-700 dark:text-gray-300" />
                )}
              </button>
            </div>
          </div>

          {/* Mobile Navigation */}
          {mobileMenuOpen && (
            <div className="md:hidden py-4 space-y-2 animate-in slide-in-from-top">
              <Link
                to="/"
                className="flex items-center px-4 py-2 rounded-lg text-sm font-medium text-gray-900 dark:text-gray-100 hover:bg-gray-100 dark:hover:bg-gray-700"
                onClick={() => setMobileMenuOpen(false)}
              >
                <LayoutDashboard className="h-4 w-4 mr-2" />
                Dashboard
              </Link>
              <a
                href="#companies"
                className="flex items-center px-4 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700"
                onClick={() => setMobileMenuOpen(false)}
              >
                <Users className="h-4 w-4 mr-2" />
                Companies
              </a>
              <a
                href="#settings"
                className="flex items-center px-4 py-2 rounded-lg text-sm font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700"
                onClick={() => setMobileMenuOpen(false)}
              >
                <Settings className="h-4 w-4 mr-2" />
                Settings
              </a>
            </div>
          )}
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {children}
      </main>

      {/* Footer */}
      <footer className="bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <p className="text-center text-sm text-gray-500 dark:text-gray-400">
            © 2025 AI Sales Insight - Intelligent Sales Intelligence Platform
          </p>
        </div>
      </footer>
    </div>
  )
}
