<div align="center">

![Unemployment Analysis Banner](https://capsule-render.vercel.app/api?type=waving&height=280&text=Unemployment%20Analysis%20%F0%9F%93%88&fontSize=52&fontAlign=50&fontAlignY=45&color=0:0d1117,50:0d2137,100:1a0533&fontColor=67e8f9&desc=AI-Powered%20Economic%20Forecasting%20%7C%20India%20Regions%20%7C%20Random%20Forest&descFontColor=a78bfa&descAlignY=65&animation=fadeIn)

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.herokuapp.com?font=Space+Grotesk&weight=700&size=24&pause=1000&color=06B6D4&center=true&vCenter=true&width=650&lines=Unemployment+Analysis+%7C+India;Random+Forest+ML+Model;FastAPI+Backend+%2B+React+Frontend;Live+Deployed+on+Vercel" alt="Typing SVG" /></a>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" />
</p>

<p>
  <img src="https://img.shields.io/badge/Status-Live-10b981?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-7C3AED?style=for-the-badge" />
</p>

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-Visit_Now-06b6d4?style=for-the-badge)](https://unemployment-analysis-with-python-ivory.vercel.app/)

</div>

---

## 🎯 What Is This?

An **end-to-end Machine Learning web application** that predicts unemployment rates across Indian regions based on economic indicators. This project transforms a standard EDA notebook into a full-stack, production-deployed ML product.

> 💡 **Problem**: Unemployment data in India is complex and region-specific. This tool makes predictions accessible through a clean UI — no data science knowledge needed.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🤖 **ML Prediction** | Random Forest model trained on Indian unemployment data |
| 📊 **Interactive EDA** | Temporal trends, regional comparisons, correlation heatmaps |
| 🌐 **Full-Stack App** | React (Vite) frontend + FastAPI backend |
| 📈 **Data Storytelling** | Policy-relevant insights from real open datasets |
| ⚡ **Live Deployed** | Hosted on Vercel — instant access, no setup |
| 📱 **Responsive UI** | Works on mobile and desktop |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────┐
│  Vite + React Frontend (Vercel)     │
│  - Region & indicator selectors     │
│  - Prediction result display        │
│  - EDA charts & visualizations      │
└──────────────┬──────────────────────┘
               │ POST /predict
               ▼
┌─────────────────────────────────────┐
│  FastAPI Backend (Python)           │
│  - Input validation (Pydantic)      │
│  - Feature preprocessing            │
│  - Model inference                  │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Random Forest Model (Scikit-learn) │
│  - Trained on Indian labour data    │
│  - Predicts Estimated Unemploy. %   │
└─────────────────────────────────────┘
```

---

## 📊 ML Pipeline

| Step | Detail |
|---|---|
| **Data Source** | Indian unemployment dataset (region + economic indicators) |
| **EDA** | Temporal trends, regional heatmaps, feature correlations |
| **Preprocessing** | Label encoding, missing value handling, feature scaling |
| **Model** | `RandomForestRegressor` (Scikit-learn) |
| **Evaluation** | RMSE, R², cross-validation |
| **Serving** | FastAPI `/predict` endpoint |

---

## 🗂️ Project Structure

```
Unemployment-Analysis-with-Python/
├── frontend/          # Vite + React UI
├── backend/           # FastAPI server + model
│   ├── main.py        # API routes
│   ├── model.pkl      # Trained Random Forest model
│   └── preprocess.py  # Feature engineering pipeline
├── notebooks/         # EDA Jupyter notebooks
├── data/              # Raw & processed datasets
└── requirements.txt   # Python dependencies
```

---

## 🚀 Run Locally

```bash
# Clone
git clone https://github.com/Shivansh-mishraji/Unemployment-Analysis-with-Python.git
cd Unemployment-Analysis-with-Python

# Backend
pip install -r requirements.txt
uvicorn backend.main:app --reload

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Open **http://localhost:5173**

---

## 📈 Key Insights From EDA

- 🔴 **COVID-19 impact**: Unemployment spiked sharply in April–May 2020
- 🌍 **Regional gap**: Haryana, Jharkhand showed highest peaks; Gujarat & Meghalaya lowest
- 📉 **Post-2020 recovery**: Gradual return to pre-pandemic levels by Q3 2021
- 🏙️ **Urban > Rural**: Urban unemployment consistently higher across most states

---

## 🔗 Links

| Resource | Link |
|---|---|
| 🌐 Live Demo | [Visit App](https://unemployment-analysis-with-python-ivory.vercel.app/) |
| 💻 GitHub | [View Code](https://github.com/Shivansh-mishraji/Unemployment-Analysis-with-Python) |
| 🏆 Kaggle | [Kaggle Profile](https://www.kaggle.com/shivansh7275) |

---

## 👤 Author

**Shivansh Mishra** — ML Builder & AI Product Explorer  
📍 Lucknow, India · [Portfolio](https://shivansh-mishraji.github.io/Portfolio-Website/) · [LinkedIn](https://www.linkedin.com/in/shivansh-mishra-132b97358) · [GitHub](https://github.com/Shivansh-mishraji)

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&height=120&color=0:0d1117,50:0d2137,100:1a0533&section=footer)

</div>
