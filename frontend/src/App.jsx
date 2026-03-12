import { useState } from "react"
import "./App.css"

function App() {
  const [file, setFile] = useState(null)
  const [email, setEmail] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [success, setSuccess] = useState("")
  const [summary, setSummary] = useState("")

  // Get API URL - works on localhost, Vercel, Render, anywhere
  const API_URL = import.meta.env.VITE_API_URL || 
                  (typeof window !== 'undefined' && window.location.hostname === 'localhost' 
                    ? "http://localhost:8000" 
                    : "https://sales-automator-backend.onrender.com")

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError("")
    setSuccess("")
    setSummary("")

    // Validation
    if (!file) {
      setError("Please select a CSV file")
      return
    }

    if (!email) {
      setError("Please enter an email address")
      return
    }

    if (!file.name.endsWith(".csv")) {
      setError("Please upload a CSV file")
      return
    }

    setLoading(true)

    try {
      const formData = new FormData()
      formData.append("file", file)
      formData.append("email", email)

      // Construct API endpoint
      const uploadUrl = `${API_URL.replace(/\/$/, '')}/api/upload`
      
      console.log("Uploading to:", uploadUrl)

      const response = await fetch(uploadUrl, {
        method: "POST",
        body: formData,
        headers: {
          "Accept": "application/json"
        }
      })

      if (!response.ok) {
        const error_data = await response.json()
        throw new Error(error_data.detail || `HTTP error! status: ${response.status}`)
      }

      const data = await response.json()

      if (data.summary_preview) {
        setSummary(data.summary_preview)
      }

      setSuccess(`✓ AI summary generated and sent to ${email}`)
      setFile(null)
      setEmail("")

    } catch (err) {
      console.error("Upload error:", err)
      setError(`Error: ${err.message}`)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <div className="card">
        <h1>📊 Data Insight Automator</h1>
        <p className="subtitle">Upload any CSV file and get AI-powered business insights</p>

        <form onSubmit={handleSubmit} className="form">
          <div className="form-group">
            <label htmlFor="file">Select CSV File</label>
            <input
              id="file"
              type="file"
              accept=".csv"
              onChange={(e) => {
                setFile(e.target.files[0])
                setError("")
              }}
              className="file-input"
              disabled={loading}
            />
            {file && <p className="file-info">Selected: {file.name}</p>}
          </div>

          <div className="form-group">
            <label htmlFor="email">Email Address</label>
            <input
              id="email"
              type="email"
              placeholder="your@email.com"
              value={email}
              onChange={(e) => {
                setEmail(e.target.value)
                setError("")
              }}
              className="email-input"
              disabled={loading}
              required
            />
          </div>

          <button
            type="submit"
            className="submit-btn"
            disabled={loading || !file || !email}
          >
            {loading ? "Processing..." : "Generate AI Summary"}
          </button>
        </form>

        {error && (
          <div className="alert alert-error">
            ⚠️ {error}
          </div>
        )}

        {success && (
          <div className="alert alert-success">
            {success}
          </div>
        )}

        {summary && (
          <div className="summary-box">
            <h3>Summary Preview</h3>
            <p>{summary}</p>
          </div>
        )}

        <p className="api-info">API: {API_URL}</p>
        <p className="api-info">Environment: {import.meta.env.MODE}</p>
      </div>
    </div>
  )
}

export default App