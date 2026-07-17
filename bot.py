import discord

import config
import weather

intents = discord.Intents.default()

ICONS = {
    "01": "☀️",
    "02": "🌤️",
    "03": "⛅",
    "04": "☁️",
    "09": "🌧️",
    "10": "🌦️",
    "11": "⛈️",
    "13": "❄️",
    "50": "🌫️",
}


class WeatherClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

        channel = self.get_channel(config.CHANNEL_ID)

        if channel is None:
            print("ERROR: Could not find the Discord channel.")
            await self.close()
            return

        embed = discord.Embed(
            title="🌤 Daily Weather Report",
            description="Today's forecast for your selected locations",
            color=discord.Color.blue()
        )

        for city in config.CITIES:
            try:
                w = await weather.get_weather(city)

                emoji = ICONS.get(w["icon"][:2], "🌤️")

                embed.add_field(
                    name=f"{emoji} {w['city']}",
                    value=(
                        f"🌡️ **High:** {w['high']}°F\n"
                        f"🥶 **Low:** {w['low']}°F\n"
                        f"📝 {w['description']}\n"
                        f"💧 Humidity: {w['humidity']}%\n"
                        f"💨 Wind: {w['wind']} mph\n"
                        f"🌧️ Rain Chance: {w['rain']}%"
                    ),
                    inline=False
                )

            except Exception as e:
                print(f"Failed to get weather for {city['name']}: {e}")

                embed.add_field(
                    name=f"❌ {city['name']}",
                    value="Unable to retrieve weather.",
                    inline=False
                )

        embed.set_footer(text="Powered by OpenWeather")

        await channel.send(embed=embed)

        print("Weather report posted successfully.")

        await self.close()


client = WeatherClient(intents=intents)
client.run(config.TOKEN)