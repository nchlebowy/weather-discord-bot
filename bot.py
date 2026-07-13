import discord
import asyncio

import config
import weather


intents = discord.Intents.default()


class WeatherClient(discord.Client):

    async def on_ready(self):
        print(f"Logged in as {self.user}")

        channel = self.get_channel(config.CHANNEL_ID)

        if channel is None:
            print("Channel not found")
            await self.close()
            return

        embed = discord.Embed(
            title="🌤 Daily Weather Report",
            color=discord.Color.blue()
        )

        for city in config.CITIES:

            w = await weather.get_weather(city)

            embed.add_field(
                name=f"📍 {w['city']}",
                value=(
                    f"**High:** {w['high']}°F\n"
                    f"**Low:** {w['low']}°F\n"
                    f"{w['description']}\n"
                    f"💧 Humidity: {w['humidity']}%\n"
                    f"💨 Wind: {w['wind']} mph\n"
                    f"🌧 Rain: {w['rain']}%"
                ),
                inline=False
            )

        await channel.send(embed=embed)

        print("Weather posted successfully")

        await self.close()


client = WeatherClient(intents=intents)

client.run(config.TOKEN)