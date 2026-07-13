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
    "Buffalo,US",
    "Lockport,US",
    "Cooks Mills,US",
    "Baton Rouge,US",
    "Glen Allen,US",
    "Thousand Oaks,US",
]