# Trovule

A modern road-trip planning application that combines current weather information with AI-generated day-by-day itineraries and estimated travel costs in South African Rand.

Trovule was originally built as a Python Streamlit application and was later upgraded into a full React + FastAPI product with a responsive frontend, Python backend, REST API architecture and Vercel deployment.

## Live Demo

**https://trovule.vercel.app**

---

## Overview

Planning a road trip often means checking multiple sources for weather, destinations, activities, stops and expected costs.

Trovule brings those pieces together into one simple experience.

Users enter:

- A starting location
- A destination
- The number of travel days

Trovule then checks current weather conditions and generates a practical one-way road-trip itinerary with suggested stops, activities, meals, overnight plans and estimated costs in South African Rand.

---

## Key Features

- Current weather for the starting point and destination
- AI-generated day-by-day road-trip itineraries
- One-way route planning that finishes at the selected destination
- Estimated daily travel costs in ZAR
- Responsive React interface
- Mobile-friendly trip planner
- Loading, validation and error states
- Invalid-location handling
- Same origin and destination validation
- Protected API credentials using environment variables
- Product-focused landing page
- FastAPI backend
- REST API communication between frontend and backend
- Vercel deployment
- GitHub-connected continuous deployment

---

## Tech Stack

### Frontend

- React
- JavaScript
- Vite
- React Router
- React Markdown
- HTML5
- CSS3

### Backend

- Python
- FastAPI
- Pydantic
- Requests
- python-dotenv
- Uvicorn

### APIs

- SheCodes Weather API
- SheCodes AI API

### Deployment

- Vercel
- GitHub

---

## Architecture

Trovule uses a separated frontend and backend architecture.

```text
User
 │
 ▼
React + Vite Frontend
 │
 │ POST /api/plan
 ▼
FastAPI Backend
 │
 ├── SheCodes Weather API
 │
 └── SheCodes AI API
 │
 ▼
Weather + Generated Itinerary
 │
 ▼
React Results Interface
```

The React frontend handles the product experience, form input, loading states, validation, errors and result presentation.

The FastAPI backend handles request validation, external API communication and itinerary generation while keeping API credentials outside the client.

---

## Project Structure

```text
trovule/
│
├── backend/
│   ├── services/
│   │   ├── __init__.py
│   │   └── shecodes_client.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .python-version
│
├── frontend/
│   ├── public/
│   │   └── assets/
│   │
│   ├── src/
│   │   ├── components/
│   │   │   ├── Footer.jsx
│   │   │   └── Header.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   └── Planner.jsx
│   │   │
│   │   ├── styles/
│   │   │   ├── Footer.css
│   │   │   ├── Header.css
│   │   │   ├── Home.css
│   │   │   └── Planner.css
│   │   │
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── vite.config.js
│
├── .env.example
├── .gitignore
├── README.md
└── vercel.json
```

---

## How It Works

### 1. Enter your route

The user provides a starting point, destination and trip duration.

### 2. Validate the request

The FastAPI backend validates the submitted values before calling external services.

For example, Trovule prevents the starting point and destination from being identical.

### 3. Check the weather

Trovule requests current weather information for both locations through the SheCodes Weather API.

### 4. Generate the itinerary

The route and duration are sent to the SheCodes AI API with instructions to create a practical one-way road-trip itinerary.

The generated itinerary can include:

- Daily routes
- Suggested stops
- Activities
- Meal ideas
- Overnight plans
- Estimated daily costs
- Total estimated trip cost

### 5. Display the results

The FastAPI backend returns the weather and itinerary data to React.

The frontend then displays:

- Route summary
- Trip duration
- Starting-location weather
- Destination weather
- Generated itinerary
- ZAR cost estimates

---

## API Endpoints

### Health Check

```http
GET /api/health
```

Example response:

```json
{
  "status": "ok"
}
```

### Generate Trip

```http
POST /api/plan
```

Example request:

```json
{
  "origin": "Johannesburg",
  "destination": "Durban",
  "duration_days": 3
}
```

Example response structure:

```json
{
  "origin": "Johannesburg",
  "destination": "Durban",
  "duration_days": 3,
  "weather": {
    "origin": {
      "temperature": 20,
      "condition": "clear sky"
    },
    "destination": {
      "temperature": 25,
      "condition": "few clouds"
    }
  },
  "itinerary": "Generated Markdown itinerary..."
}
```

---

## Validation and Error Handling

Trovule includes handling for:

- Missing API credentials
- Invalid city or town names
- Same origin and destination
- Invalid trip duration
- Weather API failures
- AI itinerary API failures
- Network errors
- Empty API responses
- Unreadable API responses
- Loading states while generating a trip

Errors are returned by FastAPI and displayed inside the React interface instead of causing the application to fail silently.

---

## Local Development

### Requirements

You will need:

- Node.js
- npm
- Python
- pip
- A SheCodes API key

---

## Environment Variables

Create a `.env` file in the project root.

```env
SHECODES_API_KEY=your_api_key_here
```

Do not commit the real `.env` file.

The repository includes `.env.example` to show the required variable without exposing credentials.

```env
SHECODES_API_KEY=
```

---

## Run the Backend

From the project root:

```bash
cd backend
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

The backend will run at:

```text
http://127.0.0.1:8000
```

FastAPI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

---

## Run the Frontend

Open a second terminal.

From the project root:

```bash
cd frontend
```

Install the frontend dependencies:

```bash
npm install
```

Start Vite:

```bash
npm run dev
```

The frontend will normally run at:

```text
http://localhost:5173
```

During local development, Vite proxies `/api` requests to the FastAPI backend.

---

## Production Build

To build the frontend:

```bash
cd frontend
npm run build
```

The production build is generated inside:

```text
frontend/dist
```

---

## Deployment

Trovule is deployed on Vercel.

The deployment contains two services:

```text
Frontend
React + Vite

Backend
Python + FastAPI
```

Vercel serves the React application and routes `/api/*` requests to the Python backend.

The SheCodes API key is stored as a protected Vercel environment variable and is not exposed in the frontend source code.

The GitHub repository is connected to Vercel so new pushes can automatically trigger deployments.

---

## From Streamlit to React + FastAPI

Trovule originally used Streamlit for both the application interface and Python functionality.

The project was later restructured to improve:

- UI control
- Responsive behaviour
- Frontend architecture
- Product presentation
- Backend separation
- Deployment
- Maintainability
- Error handling
- Accessibility

The original Python service logic was preserved and adapted into a FastAPI backend rather than replacing the working application with a fake visual redesign.

The migration allowed Trovule to continue using Python while moving the user interface to React and CSS.

---

## Technical Decisions

### React for the frontend

React provides full control over the product interface, responsive behaviour, reusable components and application states.

### FastAPI for the backend

FastAPI exposes the Python functionality through REST endpoints that the React frontend can communicate with.

### Server-side API credentials

The SheCodes API key is accessed only by the Python backend and is never exposed inside the React application.

### Markdown itinerary rendering

The generated itinerary is returned as Markdown and rendered in React using `react-markdown`.

### One-way itinerary generation

The AI instructions are designed so that a generated trip:

- Starts at the selected origin
- Progresses toward the selected destination
- Finishes at the destination on the final day
- Does not automatically create a return journey

---

## Responsive Design

Trovule was designed and tested for both desktop and mobile devices.

Responsive behaviour includes:

- Simplified mobile navigation
- Stacked planner fields
- Responsive weather cards
- Mobile-friendly itinerary content
- Flexible homepage layouts
- Responsive calls to action
- Mobile footer layout
- No horizontal page overflow

---

## Accessibility

The interface includes:

- Semantic HTML
- Proper form labels
- Accessible navigation labels
- Keyboard-friendly controls
- Visible focus states
- Error messages using `role="alert"`
- Loading feedback using `aria-live`
- Responsive typography
- Clear visual contrast

---

## Screenshots

### Product Website

Add the final Trovule desktop homepage screenshot here.

### Trip Planner

Add a screenshot showing a successfully generated road trip here.

### Mobile Experience

Add a final mobile homepage or planner screenshot here.

---

## What I Learned

Building and upgrading Trovule provided practical experience with:

- Migrating an existing Python application to React + FastAPI
- Building a REST API with FastAPI
- Connecting React to a Python backend
- Integrating third-party APIs
- Working with asynchronous frontend requests
- Handling API errors and loading states
- Protecting environment variables
- Rendering generated Markdown in React
- Creating responsive interfaces
- Improving AI prompt instructions
- Debugging itinerary-generation behaviour
- Separating frontend and backend responsibilities
- Preparing a full-stack application for production
- Deploying React and Python together on Vercel
- Connecting GitHub to continuous deployment

---

## Future Improvements

Possible future improvements include:

- Interactive route maps
- Multi-stop trip planning
- Saved trips
- Extended weather forecasts
- Route distance calculations
- Accommodation integrations
- More detailed budget controls

These features are not currently part of the application.

---

## Author

**Git It Bunny**

Designed and developed as a software development portfolio project.

---

## License

All rights reserved.

© 2026 Trovule.