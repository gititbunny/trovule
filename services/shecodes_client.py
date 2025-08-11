import os
import requests
from urllib.parse import urlencode

class APIError(Exception):
    pass

def _get_api_key():

    try:
        import streamlit as st
        if "SHECODES_API_KEY" in st.secrets:
            return st.secrets["SHECODES_API_KEY"]
    except Exception:
        pass

 
    api_key = os.getenv("SHECODES_API_KEY")
    if not api_key:
        raise APIError("Missing API key. Set SHECODES_API_KEY in .env (local) or Streamlit Secrets (cloud).")
    return api_key

def current_weather(location: str) -> dict:
   
    api_key = _get_api_key()
    base = "https://api.shecodes.io/weather/v1/current"
    params = {
        "query": location,
        "key": api_key,
        "units": "metric"
    }
    try:
        r = requests.get(base, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        temp = round(data["temperature"]["current"])
        cond = data["condition"]["description"]
        return {"temperature": temp, "condition": cond}
    except requests.HTTPError as e:
        raise APIError(f"Weather API error: {e.response.status_code} - {e.response.text}") from e
    except requests.RequestException as e:
        raise APIError(f"Network error: {e}") from e
    except Exception as e:
        raise APIError(f"Unexpected weather error: {e}") from e

def generate_itinerary(origin: str, destination: str, duration_days: int) -> str:
   
    api_key = _get_api_key()
    prompt = (
        f"Generate an itinerary for a road trip from {origin} to {destination} in {duration_days} days. "
        f"Keep it short (<= 15 lines). Use <= 5 emojis. Include a per-day estimated price in South African Rands."
    )
    context = "You are a specialist travel planner and know the best tourist spots worldwide."

    base = "https://api.shecodes.io/ai/v1/generate"
    qs = urlencode({"prompt": prompt, "context": context, "key": api_key})

    try:
        r = requests.get(f"{base}?{qs}", timeout=60)
        r.raise_for_status()
        data = r.json()
        return data["answer"]  
    except requests.HTTPError as e:
        raise APIError(f"AI API error: {e.response.status_code} - {e.response.text}") from e
    except requests.RequestException as e:
        raise APIError(f"Network error: {e}") from e
    except KeyError:
        raise APIError("AI response format unexpected (missing 'answer').")
