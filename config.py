import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
WEATHER_KEY = os.getenv("OPENWEATHER_API_KEY")

CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

POST_HOUR = int(os.getenv("POST_HOUR", 7))
POST_MINUTE = int(os.getenv("POST_MINUTE", 0))

TIMEZONE = os.getenv("TIMEZONE", "America/New_York")

CITIES = [
    "Buffalo,US",
    "Lockport,US",
    "Cooks Mills,US",
    "Baton Rouge,US",
    "Glen Allen,US",
]
