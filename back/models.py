from pydantic import BaseModel
from typing import List, Optional

# Modèle pour la Météo
class WeatherResponse(BaseModel):
    city: str
    temperature: float
    feels_like: float
    description: str
    humidity: int

# Modèle pour la Qualité de l'Air
class AirQualityResponse(BaseModel):
    city: str
    aqi: int
    status: str
    health_recommendation: str

# Modèle pour un Événement
class Event(BaseModel):
    name: str
    date: str
    location: str
    category: str

# Modèle pour la Prédiction IA
class PredictionResponse(BaseModel):
    city: str
    prediction_6h: float
    confidence_score: float

# Modèle pour le Score Urbain
class UrbanScore(BaseModel):
    city: str
    global_score: int
    level: str