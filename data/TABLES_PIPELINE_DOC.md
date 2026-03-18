# CityPulse - Documentation tables et pipeline

## Tables PostgreSQL

### weather_data
- Role: mesures meteo horaires.
- Colonnes principales: city, temperature, feels_like, humidity, wind_speed, icon, measured_at.
- Contraintes: UNIQUE(city, measured_at).

### air_quality
- Role: mesures qualite de l'air horaires.
- Colonnes principales: city, aqi, pm25, no2, o3, measured_at.
- Contraintes: CHECK aqi entre 1 et 5, UNIQUE(city, measured_at).

### events
- Role: evenements publics OpenAgenda.
- Colonnes principales: city, external_id, title, event_date, start_time, location, category.
- Contraintes: external_id unique.

## Pipeline de donnees

1. Collecte APIs publiques:
- OpenWeather (meteo actuelle)
- OpenWeather Air Pollution (AQI, PM2.5, NO2, O3)
- OpenAgenda (evenements)

2. Normalisation et nettoyage:
- Uniformisation du nom de ville
- Conversion robuste numerique
- Clamp AQI 1..5
- Parsing date/heure ISO des evenements
- Troncature defensive de champs texte

3. Chargement en base:
- Insert weather_data / air_quality horodates
- Upsert events sur external_id
- Calcul du score urbain en memoire (non stocke en base)

4. Planification horaire:
- Script boucle avec intervalle configurable (3600s par defaut)

## Commandes utiles

Depuis le dossier back:

- Initialiser le schema:
  python ../data/init.py

- Lancer une collecte immediate:
  python -m pipelines.collect_public_data --cities Paris Lyon Marseille

- Lancer alimentation horaire continue:
  python -m pipelines.hourly_ingest --cities Paris Lyon Marseille

- Test rapide (1 cycle):
  python -m pipelines.hourly_ingest --once

- Injecter 48h de donnees simulees:
  python -m pipelines.simulate_48h --hours 48 --cities Paris Lyon Marseille
