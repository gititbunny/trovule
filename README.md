# Trovule — Your Blissful Trip Buddy

A playful Streamlit app that:

- Checks real-time weather for your origin and destination
- Generates a short, emoji-light road trip itinerary with per-day ZAR estimates (via SheCodes AI)

## Tech

Python • Streamlit • requests • dotenv

## Local setup

```bash
python -m venv .venv
.\.venv\Scripts\activate

python -m pip install -r requirements.txt
copy .env.example .env
python -m streamlit run app.py
```
