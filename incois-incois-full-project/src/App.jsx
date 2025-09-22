import React from "react"
import { Routes, Route } from "react-router-dom"
import MainLayout from "./layouts/MainLayout"
import Home from "./pages/Home"
import Dashboard from "./pages/Dashboard"
import Alerts from "./pages/Alerts"
import Feed from "./pages/Feed"
import Login from "./pages/Login"
import Signup from "./pages/Signup"
import About from "./pages/About"

export default function App() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/alerts" element={<Alerts />} />
        <Route path="/feed" element={<Feed />} />
        <Route path="/about" element={<About />} />
      </Route>
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
    </Routes>
  )
}
