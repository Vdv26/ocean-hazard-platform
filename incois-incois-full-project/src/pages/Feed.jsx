import React from "react"

const posts = [
  {
    id: 1,
    author: "Community Group A",
    type: "Hazard Report",
    content: "High tide observed near Vizag beach, risk of flooding.",
    time: "2h ago",
  },
  {
    id: 2,
    author: "Citizen User",
    type: "Photo Report",
    content: "Oil spill spotted near Chennai coast.",
    time: "5h ago",
  },
  {
    id: 3,
    author: "Admin",
    type: "Official Alert",
    content: "Cyclone warning issued for Andhra coast. Stay safe!",
    time: "1d ago",
  },
]

export default function Feed() {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Community Feed</h1>
      <div className="space-y-4">
        {posts.map((post) => (
          <div
            key={post.id}
            className="bg-white p-6 rounded-lg shadow hover:shadow-lg transition"
          >
            <div className="flex justify-between items-center mb-2">
              <h2 className="font-semibold text-sky-700">{post.author}</h2>
              <span className="text-xs text-gray-500">{post.time}</span>
            </div>
            <p className="text-gray-700 mb-2">{post.content}</p>
            <span className="text-xs px-2 py-1 bg-sky-100 text-sky-700 rounded">{post.type}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
