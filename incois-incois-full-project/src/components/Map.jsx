import React from "react"
import { MapContainer, TileLayer, Marker, Popup, Circle } from "react-leaflet"
import L from "leaflet"
import "leaflet/dist/leaflet.css"

import iconUrl from "leaflet/dist/images/marker-icon.png"
import iconShadow from "leaflet/dist/images/marker-shadow.png"
const DefaultIcon = L.icon({
  iconUrl,
  shadowUrl: iconShadow,
})
L.Marker.prototype.options.icon = DefaultIcon

export default function Map() {
  // Example hazard reports with severity levels
  const reports = [
    { id: 1, position: [17.6868, 83.2185], text: "High Tide - Vizag Beach", severity: "high" },
    { id: 2, position: [13.0827, 80.2707], text: "Oil Spill - Chennai Coast", severity: "moderate" },
    { id: 3, position: [9.9312, 76.2673], text: "High Waves - Kochi", severity: "low" },
  ]

  // Circle colors for hotspots
  const severityColors = {
    high: { color: "red", fillColor: "#f87171", radius: 30000 },
    moderate: { color: "orange", fillColor: "#facc15", radius: 20000 },
    low: { color: "green", fillColor: "#4ade80", radius: 10000 },
  }

  return (
    <div className="w-full h-[500px] rounded-lg shadow overflow-hidden">
      <MapContainer
        center={[15.5, 80]}
        zoom={5}
        style={{ height: "100%", width: "100%" }}
      >
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {reports.map((report) => (
          <React.Fragment key={report.id}>
            <Marker position={report.position}>
              <Popup>{report.text}</Popup>
            </Marker>
            <Circle
              center={report.position}
              pathOptions={severityColors[report.severity]}
              radius={severityColors[report.severity].radius}
            />
          </React.Fragment>
        ))}
      </MapContainer>
    </div>
  )
}
