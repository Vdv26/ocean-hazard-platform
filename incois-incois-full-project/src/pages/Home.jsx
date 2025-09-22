import React from 'react'
import Map from '../components/Map'

export default function Home() {
  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <section className="bg-gradient-to-r from-sky-600 to-blue-500 text-white rounded-lg p-8 shadow">
        <h1 className="text-3xl font-bold mb-2">
          Welcome to INCOIS Hazard Reporting
        </h1>
        <p className="text-lg opacity-90">
          Crowdsourced Ocean Hazard Reporting & Social Media Analytics Platform
        </p>
      </section>

      {/* Quick Stats */}
      <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Reports Submitted</h2>
          <p className="text-3xl font-bold text-sky-600">12,450</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Verified Hazards</h2>
          <p className="text-3xl font-bold text-green-600">8,920</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Communities</h2>
          <p className="text-3xl font-bold text-yellow-500">128</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Active Alerts</h2>
          <p className="text-3xl font-bold text-red-600">23</p>
        </div>
      </section>

      {/* Map Section */}
      <section>
        <h2 className="text-xl font-bold mb-4">Live Hazard Map</h2>
        <Map />
      </section>
    </div>
  )
}
