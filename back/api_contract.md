```json
// GET /api/weather/paris
{
  "city": "Paris",
  "temperature": 22.5,
  "feels_like": 21.0,
  "unit": "Celsius",
  "humidity": 45,
  "wind_speed": 8.3,
  "description": "Partiellement nuageux",
  "icon": "03d",
  "forecast_24h": [
    {"time": "14:00", "temp": 19.0},
    {"time": "17:00", "temp": 17.5},
    {"time": "20:00", "temp": 15.2}
  ]
}
```

```json
// GET /api/air/paris
{
  "city": "Paris",
  "aqi": 45,
  "status": "Bon",
  "color_code": "#00E400",
  "pollutants": {
    "pm25": 9.8,
    "no2": 14.2,
    "o3": 35.1
  },
  "health_recommendation": "La qualité de l'air est jugée satisfaisante. Idéal pour les activités en extérieur."
}
```

```json
// GET /api/events/paris
[
  {
    "id": 101,
    "title": "Festival de la Soie",
    "date": "2024-03-20",
    "time": "10:00",
    "location": "Palais de la Bourse",
    "category": "Culture",
    "description": "Découverte des métiers du tissage lyonnais."
  },
  {
    "id": 102,
    "title": "Marathon de la Gastronomie",
    "date": "2024-03-22",
    "time": "19:00",
    "location": "Vieux Lyon",
    "category": "Loisirs",
    "description": "Parcours dégustation dans les bouchons lyonnais."
  }
]
```

```json
// GET /api/predict/paris
{
  "city": "Paris",
  "prediction_target": "Qualité de l'air (AQI)",
  "value_in_6h": 52,
  "trend": "En hausse légère",
  "confidence_score": 0.88,
  "model_info": "RandomForestRegressor v1.2",
  "timestamp": "2024-03-16T12:00:00"
}
```

```json
// GET /api/score/paris
{
  "city": "Paris",
  "global_score": 74,
  "max_score": 100,
  "rating": "Agréable",
  "breakdown": {
    "environment": 82,
    "activity": 65,
    "safety": 75
  },
  "last_update": "Il y a 10 minutes"
}
```
