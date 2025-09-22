import React from "react"

const alerts = [
  {
    id: 1,
    type: "High Alert",
    message: "Cyclone approaching east coast. Evacuation in progress.",
    level: "high",
  },
  {
    id: 2,
    type: "Moderate Alert",
    message: "High waves expected in Kerala. Avoid coastal activities.",
    level: "moderate",
  },
  {
    id: 3,
    type: "Information",
    message: "Sea temperature rise observed. Monitoring situation.",
    level: "info",
  },
]

const alertStyles = {
  high: "bg-red-100 text-red-700 border-red-300",
  moderate: "bg-yellow-100 text-yellow-700 border-yellow-300",
  info: "bg-blue-100 text-blue-700 border-blue-300",
}

export default function Alerts() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Alerts</h1>
      <div className="space-y-4">
        {alerts.map((alert) => (
          <div
            key={alert.id}
            className={`border-l-4 p-4 rounded ${alertStyles[alert.level]} shadow`}
          >
            <h2 className="font-semibold">{alert.type}</h2>
            <p>{alert.message}</p>
          </div>
        ))}
      </div>
    </div>
  )
}
