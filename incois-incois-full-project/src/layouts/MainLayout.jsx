import React from "react"
import { Link, Outlet } from "react-router-dom"
import LanguageSelector from "../components/LanguageSelector"

export default function MainLayout() {
  return (
    <div className="flex min-h-screen bg-gray-100">
      {/* Sidebar */}
      <aside className="w-64 bg-sky-900 text-white flex flex-col">
        <div className="p-4 text-xl font-bold border-b border-sky-700">
          INCOIS
        </div>
        <nav className="flex-1 p-4 space-y-3">
          <Link to="/" className="block hover:bg-sky-800 p-2 rounded">🏠 Home</Link>
          <Link to="/dashboard" className="block hover:bg-sky-800 p-2 rounded">📊 Dashboard</Link>
          <Link to="/alerts" className="block hover:bg-sky-800 p-2 rounded">🚨 Alerts</Link>
          <Link to="/feed" className="block hover:bg-sky-800 p-2 rounded">📰 Feed</Link>
          <Link to="/about" className="block hover:bg-sky-800 p-2 rounded">ℹ️ About</Link>
        </nav>
      </aside>

      {/* Main content */}
      <div className="flex-1 flex flex-col">
        {/* Top Navbar */}
        <header className="bg-white border-b p-4 flex justify-between items-center shadow">
          <h1 className="font-semibold text-lg">Hazard Reporting Platform</h1>
          <div className="flex items-center gap-4">
            <LanguageSelector />
            <Link to="/login" className="text-sky-600 font-medium">Login</Link>
          </div>
        </header>

        {/* Page Content */}
        <main className="flex-1 p-6 overflow-y-auto">
          <Outlet />
        </main>

        {/* Footer */}
        <footer className="bg-gray-200 text-center p-4 text-sm">
          © 2025 INCOIS Hazard Reporting Platform
        </footer>
      </div>
    </div>
  )
}
