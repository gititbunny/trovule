# Trovule — Your Blissful Trip Buddy

Trovule is a playful Streamlit road-trip planner that checks current weather for the origin and destination and generates a concise AI-assisted itinerary with daily ZAR cost estimates.

## Tech

Python • Streamlit • Requests • python-dotenv • SheCodes Weather API • SheCodes AI API

## Local setup (Windows)

```bash
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and replace `YOUR_KEY_HERE` with your real SheCodes API key:

```env
SHECODES_API_KEY=YOUR_REAL_KEY
```

Then run:

```bash
python -m streamlit run app.py
```

## Streamlit Cloud

Add this secret in your app settings:

```toml
SHECODES_API_KEY="YOUR_REAL_KEY"
```

Never commit `.env` or `.streamlit/secrets.toml` to Git.
