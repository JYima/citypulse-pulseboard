from fastapi import FastAPI
from typing import List
# Import des modèles depuis le fichier models.py
from models import WeatherResponse, AirQualityResponse, Event, PredictionResponse, UrbanScore

app = FastAPI(title="CityPulse API")

@app.get("/api/weather/{city}", response_model=WeatherResponse)
async def get_weather(city: str):
    return {
        "city": city,
        "temperature": 22.5,
        "feels_like": 24.0,
        "description": "Ensoleillé",
        "humidity": 45
    }

@app.get("/api/air/{city}", response_model=AirQualityResponse)
async def get_air(city: str):
    return {
        "city": city,
        "aqi": 42,
        "status": "Bon",
        "health_recommendation": "Parfait pour une balade."
    }

@app.get("/api/events/{city}", response_model=List[Event])
async def get_events(city: str):
    return [
        {"name": "Festival Lumière", "date": "2024-10-12", "location": "Lyon", "category": "Cinéma"}
    ]

@app.get("/api/predict/{city}", response_model=PredictionResponse)
async def get_prediction(city: str):
    return {"city": city, "prediction_6h": 21.0, "confidence_score": 0.85}

@app.get("/api/score/{city}", response_model=UrbanScore)
async def get_urban_score(city: str):
    return {"city": city, "global_score": 82, "level": "Très Bien"}