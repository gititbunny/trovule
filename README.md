# Trovule — Your Blissful Trip Buddy

A playful Streamlit app that:

- Checks real-time weather for your origin and destination
- Generates a short, emoji-light road trip itinerary with per-day ZAR estimates (via SheCodes AI)

## Tech

Python • Streamlit • requests • dotenv

## Local setup

```bash
python -m venv .venv
.\.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # macOS/Linux

python -m pip install -r requirements.txt
copy .env.example .env        # add your API_API_KEY
python -m streamlit run app.py
```
