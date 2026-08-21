# Trovule 🚗🗺️

![Trovule Logo](./assets/logo.png)

**Trovule** is a playful road-trip planning companion built with Python and Streamlit. It checks the current weather at your starting point and destination, then generates a simple AI-assisted day-by-day road-trip itinerary with estimated daily costs in South African Rands (ZAR).

The goal is to make planning a road trip quick, useful and a little more fun.

## Features

* Enter a starting city and destination
* Choose a trip duration from 1–60 days
* Retrieve current weather for both locations
* Display current temperature and weather conditions
* Generate an AI-assisted day-by-day road-trip itinerary
* Receive estimated daily travel costs in ZAR
* Practical route, activity, meal and overnight suggestions
* Input validation for missing or identical locations
* Friendly API and connectivity error handling
* Custom Streamlit interface with responsive styling
* Animated background and celebratory confetti interaction

## Tech Stack

**Application**

* Python
* Streamlit

**APIs**

* SheCodes Weather API
* SheCodes AI API

**Libraries**

* Requests
* python-dotenv
* Streamlit Components

**Development**

* Git
* GitHub
* Python virtual environments

## How It Works

Users provide:

* A starting city
* A destination city
* The number of days for the trip

Trovule first retrieves current weather information for the origin and destination.

It then sends the trip information to the SheCodes AI API, which generates a concise road-trip itinerary containing daily routes, suggested activities and stops, meal or overnight recommendations where relevant, and estimated daily costs in **South African Rands (ZAR)**.

The finished weather summary and itinerary are displayed directly in the Streamlit interface.

## Project Structure

```text
trovule/
├── assets/
│   ├── bg.mp4
│   ├── icon.png
│   └── logo.png
├── services/
│   ├── ___init__.py
│   └── shecodes_client.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/gititbunny/trovule.git
```

Navigate into the project directory:

```bash
cd trovule
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.\.venv\Scripts\activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Create your local environment file:

```bash
copy .env.example .env
```

Add your SheCodes API key to `.env`:

```env
SHECODES_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
python -m streamlit run app.py
```

## Environment Variables

Trovule requires a SheCodes API key.

For local development:

```env
SHECODES_API_KEY=YOUR_API_KEY
```

The `.env` file is excluded from Git and should never be committed to the repository.

For Streamlit Cloud, the API key can be stored securely using **Streamlit Secrets**.

## Error Handling

Trovule includes handling for:

* Missing API configuration
* Invalid or unavailable cities
* Weather API errors
* AI itinerary API errors
* Network connection failures
* Empty API responses
* Invalid trip inputs

User-facing error messages are displayed within the application instead of exposing raw API failures.

## What This Project Demonstrates

Trovule demonstrates practical experience with:

* Python application development
* Building interactive applications with Streamlit
* REST API integration
* Working with AI-generated responses
* Processing JSON API responses
* HTTP requests and exception handling
* Environment variable and API-key management
* Input validation
* Responsive interface customisation
* HTML and CSS integration within Streamlit
* Git and GitHub version control

## Notes

Weather information represents current conditions for the selected origin and destination.

Trip costs are estimates generated for planning purposes and may differ from real-world prices.

AI-generated activities, routes and recommendations should be treated as suggestions and verified before travelling.

## Author

Built by **Git It Bunny**

[GitHub](https://github.com/gititbunny)
