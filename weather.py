import aiohttp
import config

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


async def get_weather(city):

    url = (
        f"{BASE_URL}"
        f"?q={city}"
        f"&appid={config.WEATHER_KEY}"
        f"&units=imperial"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()

    today = data["list"][:8]

    temps = [x["main"]["temp"] for x in today]

    rain = max(
        [x.get("pop", 0) * 100 for x in today]
    )

    weather = today[0]["weather"][0]

    return {
        "city": city.split(",")[0],
        "high": round(max(temps)),
        "low": round(min(temps)),
        "description": weather["description"].title(),
        "icon": weather["icon"],
        "humidity": today[0]["main"]["humidity"],
        "wind": round(today[0]["wind"]["speed"]),
        "rain": round(rain),
    }
