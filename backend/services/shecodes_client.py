import os

import requests


class APIError(Exception):
    """Friendly exception for API and configuration failures."""


def _get_api_key() -> str:
    """Read the SheCodes API key from the environment."""

    api_key = os.getenv("SHECODES_API_KEY", "").strip()

    if not api_key:
        raise APIError(
            "Missing API key. Set SHECODES_API_KEY in your environment."
        )

    return api_key


def current_weather(location: str) -> dict:
    """Return a normalized weather summary for a valid city or town."""

    api_key = _get_api_key()

    endpoint = "https://api.shecodes.io/weather/v1/current"

    params = {
        "query": location,
        "key": api_key,
        "units": "metric",
    }

    try:
        response = requests.get(endpoint, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        try:
            temperature = round(float(data["temperature"]["current"]))
            condition = str(data["condition"]["description"]).strip()

        except (KeyError, TypeError, ValueError) as exc:
            raise APIError(
                f"Weather data could not be found for '{location}'. "
                "Please enter a valid city or town name."
            ) from exc

        if not condition:
            condition = "Weather unavailable"

        return {
            "temperature": temperature,
            "condition": condition,
        }

    except requests.HTTPError as exc:
        status_code = (
            exc.response.status_code if exc.response is not None else "unknown"
        )

        if status_code in (400, 404):
            raise APIError(
                f"Weather data could not be found for '{location}'. "
                "Please enter a valid city or town name."
            ) from exc

        raise APIError(
            f"Weather API error ({status_code}). Please try again."
        ) from exc

    except requests.RequestException as exc:
        raise APIError(
            "Trovule could not reach the weather service. "
            "Check your internet connection and try again."
        ) from exc

    except ValueError as exc:
        raise APIError(
            "The weather service returned an unreadable response."
        ) from exc


def generate_itinerary(
    origin: str,
    destination: str,
    duration_days: int,
) -> str:
    """Generate a concise Markdown road-trip itinerary."""

    api_key = _get_api_key()

    endpoint = "https://api.shecodes.io/ai/v1/generate"

    prompt = (
        f"Create a {duration_days}-day ONE-WAY road trip itinerary "
        f"from {origin} to {destination}. "
        f"The journey must begin in {origin} and finish in {destination} "
        f"on day {duration_days}. "
        "Do not create a return journey to the starting point unless the user "
        "explicitly asks for one. "
        "Each day should move the traveller sensibly closer to the destination. "
        "Keep the route geographically sensible and practical for driving. "
        "Use Markdown. Start with a short itinerary title. "
        "For each day, use a bold day heading followed by concise bullet points "
        "for the day's route, activities, meals or stops, overnight plan where "
        "relevant, and an estimated daily cost in South African Rands (ZAR). "
        "The final day's overnight location should be the destination. "
        "At the end, include a total estimated trip cost in ZAR. "
        "Use no more than 5 emojis in total. "
        "Do not use a Markdown table. "
        "Do not invent specific venues when you are unsure; prefer well-known "
        "areas or generic suggestions."
    )

    context = (
        "You are a practical travel planner who creates concise, realistic "
        "one-way road-trip plans. Prioritize sensible routes, useful stops, "
        "clear daily cost estimates, and ensure the journey ends at the "
        "requested destination."
    )

    params = {
        "prompt": prompt,
        "context": context,
        "key": api_key,
    }

    try:
        response = requests.get(endpoint, params=params, timeout=60)
        response.raise_for_status()

        data = response.json()
        answer = data.get("answer")

        if not isinstance(answer, str) or not answer.strip():
            raise APIError(
                "The itinerary service returned an empty response. "
                "Please try again."
            )

        return answer.strip()

    except requests.HTTPError as exc:
        status_code = (
            exc.response.status_code if exc.response is not None else "unknown"
        )

        raise APIError(
            f"Itinerary API error ({status_code}). Please try again."
        ) from exc

    except requests.RequestException as exc:
        raise APIError(
            "Trovule could not reach the itinerary service. "
            "Check your internet connection and try again."
        ) from exc

    except ValueError as exc:
        raise APIError(
            "The itinerary service returned an unreadable response."
        ) from exc