import React from "react"
import { Link } from "react-router-dom"

export default function Login() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md bg-white shadow-lg rounded-lg p-8">
        <h1 className="text-2xl font-bold mb-6 text-center text-sky-700">
          Login to INCOIS
        </h1>
        <form className="flex flex-col gap-4">
          <div>
            <label className="block text-sm font-medium mb-1">Username</label>
            <input
              type="text"
              placeholder="Enter your username"
              className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200"
            />
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Password</label>
            <input
              type="password"
              placeholder="Enter your password"
              className="w-full border rounded px-3 py-2 focus:ring focus:ring-sky-200"
            />
          </div>
          <button className="w-full bg-sky-600 hover:bg-sky-700 text-white py-2 rounded transition">
            Login
          </button>
        </form>
        <p className="mt-4 text-sm text-center">
          New user? <Link to="/signup" className="text-sky-600 hover:underline">Sign up</Link>
        </p>
      </div>
    </div>
  )
}
