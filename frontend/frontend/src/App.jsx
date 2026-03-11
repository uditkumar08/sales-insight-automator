import { useState } from "react"

function App() {

  const [file,setFile] = useState(null)
  const [email,setEmail] = useState("")

  const handleSubmit = async () => {

    const formData = new FormData()

    formData.append("file",file)
    formData.append("email",email)

    await fetch("http://localhost:8000/upload",{
      method:"POST",
      body:formData
    })

    alert("Summary sent!")
  }

  return (
    <div>

      <h1>Sales Insight Automator</h1>

      <input
        type="file"
        onChange={(e)=>setFile(e.target.files[0])}
      />

      <input
        type="email"
        placeholder="Enter email"
        onChange={(e)=>setEmail(e.target.value)}
      />

      <button onClick={handleSubmit}>
        Upload
      </button>

    </div>
  )
}

export default App