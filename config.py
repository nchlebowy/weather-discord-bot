import os
from dotenv import load_dotenv

# Loads variables from .env when running locally.
# In GitHub Actions, the secrets are already environment variables,
# so this does nothing and is safe to leave in.
load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
WEATHER_KEY = os.environ["OPENWEATHER_API_KEY"]
CHANNEL_ID = int(os.environ["CHANNEL_ID"])

CITIES = [
    {"name": "Buffalo, NY", "lat": 42.8864, "lon": -78.8784},
    {"name": "Lockport, NY", "lat": 43.1706, "lon": -78.6903},
    {"name": "Cooks Mills, IL", "lat": 39.4878, "lon": -88.2164},
    {"name": "Baton Rouge, LA", "lat": 30.4515, "lon": -91.1871},
    {"name": "Glen Allen, VA", "lat": 37.6659, "lon": -77.5064},
    {"name": "Thousand Oaks, CA", "lat": 34.1706, "lon": -118.8376},
]