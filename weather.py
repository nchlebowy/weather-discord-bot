import aiohttp
import config


async def get_weather(city):
    """
    city is a dictionary like:
    {
        "name": "Lockport, NY",
        "lat": 43.1706,
        "lon": -78.6903
    }
    """

    url = (
        "https://api.openweathermap.org/data/2.5/forecast"
        f"?lat={city['lat']}"
        f"&lon={city['lon']}"
        f"&appid={config.WEATHER_KEY}"
        "&units=imperial"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()

    today = data["list"][:8]  # First 24 hours (8 x 3-hour forecasts)

    high = max(item["main"]["temp_max"] for item in today)
    low = min(item["main"]["temp_min"] for item in today)

    current = today[0]

    rain = 0
    if "pop" in current:
        rain = round(current["pop"] * 100)

    return {
        "city": city["name"],
        "high": round(high),
        "low": round(low),
        "description": current["weather"][0]["description"].title(),
        "humidity": current["main"]["humidity"],
        "wind": round(current["wind"]["speed"]),
        "rain": rain,
        "icon": current["weather"][0]["icon"],
    }