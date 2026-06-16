import { useState } from 'react'

const REGIONS = [
  "Andhra Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi", "Goa", "Gujarat", 
  "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Karnataka", 
  "Kerala", "Madhya Pradesh", "Maharashtra", "Meghalaya", "Odisha", "Puducherry", 
  "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", 
  "Uttar Pradesh", "Uttarakhand", "West Bengal"
];

function App() {
  const [formData, setFormData] = useState({
    Region: REGIONS[0],
    Employed: 10000000,
    Labour_participation: 40.0,
    Area: "Rural"
  });
  
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    
    try {
      // Fetch uses the relative path /predict, which will be proxied in dev, and matched by Vercel routes in prod
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          Region: formData.Region,
          Frequency: " Monthly",
          Employed: parseFloat(formData.Employed),
          Labour_participation: parseFloat(formData.Labour_participation),
          Area: formData.Area,
          Month: 6,
          Year: 2020
        })
      });
      
      if (!response.ok) throw new Error("Failed to fetch prediction");
      
      const data = await response.json();
      setPrediction(data.Unemployment_rate);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="header">
        <h1>Unemployment Predictor</h1>
        <p>AI-powered economic forecasting for Indian regions</p>
      </div>

      <div className="glass-card">
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="Region">Region</label>
            <select 
              id="Region" 
              name="Region" 
              className="form-control" 
              value={formData.Region}
              onChange={handleChange}
            >
              {REGIONS.map(region => (
                <option key={region} value={region}>{region}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label htmlFor="Employed">Estimated Employed Workforce</label>
            <input 
              type="number" 
              id="Employed" 
              name="Employed" 
              className="form-control" 
              value={formData.Employed}
              onChange={handleChange}
              min="0"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="Labour_participation">Labour Participation Rate (%)</label>
            <input 
              type="number" 
              id="Labour_participation" 
              name="Labour_participation" 
              className="form-control" 
              value={formData.Labour_participation}
              onChange={handleChange}
              step="0.01"
              min="0"
              max="100"
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="Area">Area Type</label>
            <select 
              id="Area" 
              name="Area" 
              className="form-control" 
              value={formData.Area}
              onChange={handleChange}
            >
              <option value="Rural">Rural</option>
              <option value="Urban">Urban</option>
            </select>
          </div>

          <button type="submit" className="submit-btn" disabled={loading}>
            {loading ? "Analyzing..." : "Predict Unemployment Rate"}
          </button>
        </form>

        {error && <div className="error-message">{error}</div>}

        {prediction !== null && !error && (
          <div className="result-section">
            <h2>Estimated Unemployment Rate</h2>
            <div className="result-value">
              {prediction.toFixed(2)}%
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
