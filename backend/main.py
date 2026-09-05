from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from dotenv import load_dotenv

from services.shecodes_client import (
    APIError,
    current_weather,
    generate_itinerary,
)

load_dotenv()

app = FastAPI()


class TripRequest(BaseModel):
    origin: str = Field(min_length=2, max_length=100)
    destination: str = Field(min_length=2, max_length=100)
    duration_days: int = Field(ge=1, le=14)


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/plan")
def plan_trip(trip: TripRequest):
    origin = trip.origin.strip()
    destination = trip.destination.strip()

    if origin.lower() == destination.lower():
        raise HTTPException(
            status_code=400,
            detail="Origin and destination must be different.",
        )

    try:
        origin_weather = current_weather(origin)
        destination_weather = current_weather(destination)

        itinerary = generate_itinerary(
            origin,
            destination,
            trip.duration_days,
        )

        return {
            "origin": origin,
            "destination": destination,
            "duration_days": trip.duration_days,
            "weather": {
                "origin": origin_weather,
                "destination": destination_weather,
            },
            "itinerary": itinerary,
        }

    except APIError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        ) from error