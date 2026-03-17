-- Nettoyage si besoin (Attention : supprime les données existantes)
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS air_quality;
DROP TABLE IF EXISTS weather;
DROP TABLE IF EXISTS cities;

-- 1. Table Météo
CREATE TABLE weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    temperature DECIMAL(5,2),
    feels_like DECIMAL(5,2),
    humidity INTEGER,
    wind_speed DECIMAL(5,2),
    description VARCHAR(255),
    icon_code VARCHAR(10),
    measured_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 2. Table Qualité de l'Air
CREATE TABLE air_quality (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    aqi INTEGER NOT NULL,
    pm25 DECIMAL(6,2),
    no2 DECIMAL(6,2),
    o3 DECIMAL(6,2),
    measured_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 3. Table Événements
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    city VARCHAR(255) NOT NULL,
    external_id VARCHAR(100) UNIQUE, -- ID provenant d'OpenAgenda
    title VARCHAR(255) NOT NULL,
    description TEXT,
    event_date DATE NOT NULL,
    start_time TIME,
    location VARCHAR(255),
    category VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Table Utilisateurs (optionnelle, pour fonctionnalités futures)
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

