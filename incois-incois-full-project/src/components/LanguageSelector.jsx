import React, { useState } from 'react'

export default function LanguageSelector(){
  const [lang, setLang] = useState('en')
  return (
    <select value={lang} onChange={e=>setLang(e.target.value)} className="border rounded p-1">
      <option value="en">English</option>
      <option value="hi">हिन्दी</option>
      <option value="te">తెలుగు</option>
    </select>
  )
}
