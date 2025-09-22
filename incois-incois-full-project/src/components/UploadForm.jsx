import React, { useState } from 'react'
import api from '../utils/api'

export default function UploadForm(){
  const [description, setDescription] = useState('')
  const [files, setFiles] = useState(null)

  const submit = async (e)=>{
    e.preventDefault()
    alert('Demo: this would upload to backend')
  }

  return (
    <form onSubmit={submit} className="bg-white p-4 rounded shadow">
      <div className="mb-2">
        <label className="block">Description</label>
        <textarea value={description} onChange={e=>setDescription(e.target.value)} className="w-full" />
      </div>
      <div className="mb-2">
        <label className="block">Media</label>
        <input type="file" multiple onChange={e=>setFiles(e.target.files)} />
      </div>
      <button className="px-4 py-2 bg-sky-600 text-white rounded" type="submit">Upload</button>
    </form>
  )
}
