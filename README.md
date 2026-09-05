# Trovule

A weather-aware road trip planner that generates simple day-by-day itineraries with estimated costs in South African Rand.

Trovule combines a modern React interface with a Python FastAPI backend, live weather data and AI-generated trip planning.

## Live Demo

**[Try Trovule](https://trovule.vercel.app)**

---

## Overview

Planning a road trip often means checking weather information, deciding where to stop and estimating how much the trip could cost across multiple different tools.

Trovule brings those steps together.

Users enter:

- A starting location
- A destination
- A trip duration

Trovule then retrieves current weather information and generates a practical one-way road trip itinerary with suggested stops, activities and estimated daily costs in ZAR.

---

## Key Features

- Route-based road trip planning
- Current weather for the starting point and destination
- AI-generated day-by-day itineraries
- Estimated daily and total costs in South African Rand
- One-way route planning that finishes at the selected destination
- Responsive interface for desktop and mobile
- Form validation and friendly error handling
- Loading and result states
- Protected API credentials using environment variables

---

## Tech Stack

### Frontend

- React
- JavaScript
- Vite
- React Router
- React Markdown
- CSS

### Backend

- Python
- FastAPI
- Requests
- python-dotenv

### APIs

- SheCodes Weather API
- SheCodes AI API

### Deployment

- Vercel
- GitHub

---

## How It Works

1. The user enters their starting point, destination and trip duration.
2. The React frontend sends the trip details to the FastAPI backend.
3. Python requests current weather information for both locations.
4. The backend sends the route details to the AI service.
5. The generated itinerary is returned to the frontend.
6. React displays the weather, route and formatted day-by-day trip plan.

---

## Architecture

```text
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
Weather + Itinerary Response
        │
        ▼
React Results Interface