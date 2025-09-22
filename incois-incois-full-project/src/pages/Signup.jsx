import React, { useState } from "react"

export default function Signup() {
  const [role, setRole] = useState("citizen")

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-lg bg-white shadow-lg rounded-lg p-8">
        <h1 className="text-2xl font-bold mb-6 text-center text-sky-700">Create an Account</h1>
        <form className="flex flex-col gap-4">
          <div>
            <label className="block text-sm font-medium mb-1">Full Name</label>
            <input type="text" placeholder="Enter your name" className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Email</label>
            <input type="email" placeholder="Enter your email" className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200" />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Contact Info</label>
            <input type="text" placeholder="Phone number / Address" className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200" />
          </div>

          <div>
            <label className="block text-sm font-medium mb-1">Register As</label>
            <select value={role} onChange={(e)=>setRole(e.target.value)} className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200">
              <option value="citizen">Citizen</option>
              <option value="community">Self-help Community</option>
            </select>
          </div>

          {role === "community" && (
            <div>
              <label className="block text-sm font-medium mb-1">Community/Group Details</label>
              <textarea placeholder="Enter details of your group" className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200" />
            </div>
          )}

          <button className="w-full bg-sky-600 hover:bg-sky-700 text-white py-2 rounded transition">Sign Up</button>
        </form>
      </div>
    </div>
  )
}
