import React from "react"
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  PieChart,
  Pie,
  Cell,
} from "recharts"

const lineData = [
  { name: "Mon", reports: 10 },
  { name: "Tue", reports: 25 },
  { name: "Wed", reports: 15 },
  { name: "Thu", reports: 40 },
  { name: "Fri", reports: 30 },
]

const pieData = [
  { name: "Verified", value: 65 },
  { name: "Pending", value: 25 },
  { name: "Rejected", value: 10 },
]

const COLORS = ["#0284c7", "#facc15", "#ef4444"]

export default function Dashboard() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Dashboard Overview</h1>

      {/* Stat Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Total Reports</h2>
          <p className="text-3xl font-bold text-sky-600">1,245</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Verified Hazards</h2>
          <p className="text-3xl font-bold text-green-600">860</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Active Alerts</h2>
          <p className="text-3xl font-bold text-red-600">15</p>
        </div>
        <div className="bg-white p-6 rounded-lg shadow text-center">
          <h2 className="text-lg font-semibold">Communities</h2>
          <p className="text-3xl font-bold text-yellow-500">42</p>
        </div>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold mb-4">Reports Trend</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={lineData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Line
                type="monotone"
                dataKey="reports"
                stroke="#0284c7"
                strokeWidth={3}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white p-6 rounded-lg shadow">
          <h2 className="text-lg font-semibold mb-4">Reports Status</h2>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie
                data={pieData}
                cx="50%"
                cy="50%"
                outerRadius={100}
                dataKey="value"
                label
              >
                {pieData.map((entry, index) => (
                  <Cell
                    key={`cell-${index}`}
                    fill={COLORS[index % COLORS.length]}
                  />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}
