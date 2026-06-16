# Interview Preparation Guide: Unemployment Analysis ML Project

This guide provides a comprehensive overview of the technical decisions, architecture, and potential cross-questioning scenarios for the Unemployment Analysis End-to-End project.

## 1. Project Overview & Architecture

**Question:** *Walk me through the architecture of your Unemployment Analysis project.*

**Answer:**
The project is built using a modern, decoupled architecture:
- **Data & Model Pipeline**: Python, Pandas, and Scikit-Learn. I took the raw dataset, handled missing values by dropping them (as they were consistent across columns), extracted temporal features (Month, Year) from the Date column, and built a Pipeline utilizing `StandardScaler` for numeric features and `OneHotEncoder` for categorical ones.
- **Model**: A Random Forest Regressor was trained on this pipeline. The model is serialized using `joblib`.
- **Backend API**: The serialized model is served via a FastAPI application. FastAPI was chosen for its asynchronous capabilities, high performance, and auto-generated Swagger documentation.
- **Frontend**: A React web application built with Vite, utilizing Vanilla CSS to implement a modern glassmorphism design. It communicates with the backend via REST endpoints using `fetch`.
- **DevOps**: Both the frontend and backend are containerized using Docker, and orchestrated using `docker-compose`.

## 2. Machine Learning Decisions

**Question:** *Why did you choose a Random Forest Regressor for this problem?*

**Answer:**
Unemployment rates, especially during periods like the COVID-19 pandemic covered in this dataset, can have highly non-linear relationships with features like labour participation and the specific region. Linear models (like Linear Regression) often fail to capture these complex interactions. 
Random Forest is an ensemble method that builds multiple decision trees and averages their predictions. It is highly robust to outliers, doesn't require extensive feature scaling (though I included a scaler in the pipeline for best practices), and automatically handles non-linearities and interactions between features (like Region and Area).

**Question:** *How did you handle missing values in the dataset?*

**Answer:**
Upon performing Exploratory Data Analysis (EDA), I found exactly 28 missing values across all columns. Because the missingness was small and uniformly distributed across rows, I chose to drop these rows (`dropna`). In a larger or more complex dataset, I might have used imputation strategies (like median for numerical, mode for categorical, or KNN Imputation).

**Question:** *What metrics did you use to evaluate the model?*

**Answer:**
I used **Root Mean Squared Error (RMSE)** and **Mean Absolute Error (MAE)**. 
- MAE gives a linear penalty to errors, giving me an intuitive sense of how far off the predictions are on average (e.g., "The model is off by 3.7% on average").
- RMSE heavily penalizes larger errors. Given the drastic spikes in unemployment during the pandemic, minimizing large predictive errors is crucial, making RMSE an essential metric.

## 3. Engineering & Deployment

**Question:** *Why use FastAPI over Flask or Django?*

**Answer:**
FastAPI is significantly faster than Flask because it is built on ASGI (Asynchronous Server Gateway Interface). For Machine Learning model serving, latency is critical. Additionally, FastAPI leverages Pydantic for data validation, ensuring that the API automatically returns 422 Unprocessable Entity errors if the frontend sends incorrect data types (e.g., passing a string instead of a float for 'Employed'). The auto-generated Swagger UI is also a massive productivity boost.

**Question:** *Why use Vite instead of Create React App (CRA)?*

**Answer:**
Vite uses native ES modules, providing incredibly fast hot module replacement (HMR) and significantly faster build times compared to Webpack-based CRA. It represents the modern standard for React scaffolding.

**Question:** *Why did you Dockerize the application?*

**Answer:**
Dockerizing the application solves the "it works on my machine" problem. By defining the environment in `Dockerfile`s and linking them with `docker-compose.yml`, any developer (or CI/CD pipeline) can spin up the exact same environment with a single command (`docker-compose up`). It isolates dependencies and makes the transition to cloud deployment (like AWS ECS or Kubernetes) trivial.

**Question:** *How is the application deployed to production?*

**Answer:**
The application is deployed as a monolithic repository (Monorepo) on **Vercel** using their Zero-Configuration capabilities. 
- The root `package.json` instructs Vercel to engage its Node.js builder. It compiles the Vite/React frontend and deposits the static assets into a `public/` directory, which Vercel natively serves at the root (`/`) of the domain.
- The Python backend resides in the `api/` directory (`api/main.py`). Vercel's Serverless environment automatically detects this directory and converts the FastAPI application into a highly scalable Python Serverless Function mapped to `/api/main`.
- Vercel rewrites (`vercel.json`) are used to seamlessly route frontend API requests (`/predict`) to the Serverless Function, and handle Single Page Application (SPA) routing fallbacks. This setup completely eliminates the need for managing underlying infrastructure.

## 4. Potential Cross-Questioning (Handling Edge Cases)

**Question:** *What happens if the model receives a `Region` it has never seen before?*

**Answer:**
Because I used `OneHotEncoder(handle_unknown='ignore')` in my scikit-learn pipeline, the pipeline won't crash. Instead, it will encode the unknown region as all zeros for the region features. The model will then make a prediction based on the other available features (like Area, Employed, etc.). This ensures the API remains robust in production.

**Question:** *How would you scale this application if you had 10,000 requests per second?*

**Answer:**
1. **Backend Scaling**: I would deploy the FastAPI container to a Kubernetes cluster or AWS ECS and use an Auto Scaling Group to spin up more pods/instances based on CPU utilization.
2. **Model Serving**: Loading the model in memory for each request is inefficient. Currently, the model is loaded once globally when the FastAPI app starts. For extreme scale, I might move the model to a specialized serving layer like Triton Inference Server or SageMaker Endpoints.
3. **Frontend Scaling**: The React app consists of static files. I would build the frontend and serve the static files via a CDN (Content Delivery Network) like AWS CloudFront or Cloudflare, ensuring zero latency globally.
