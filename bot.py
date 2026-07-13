import discord
from discord.ext import commands

import config
import weather
from scheduler import schedule

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

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


async def build_embed():
    embed = discord.Embed(
        title="🌤 Daily Weather Report",
        color=discord.Color.blue()
    )

    for city in config.CITIES:
        w = await weather.get_weather(city)

        emoji = ICONS.get(w["icon"][:2], "🌤️")

        embed.add_field(
            name=f"{emoji} {w['city']}",
            value=(
                f"**High:** {w['high']}°F\n"
                f"**Low:** {w['low']}°F\n"
                f"{w['description']}\n"
                f"💧 Humidity: {w['humidity']}%\n"
                f"💨 Wind: {w['wind']} mph\n"
                f"🌧 Rain: {w['rain']}%"
            ),
            inline=False,
        )

    return embed


async def post_weather():
    channel = bot.get_channel(config.CHANNEL_ID)

    if channel is None:
        print("Could not find channel.")
        return

    await channel.send(embed=await build_embed())


@bot.tree.command(
    name="weather",
    description="Post today's weather report"
)
async def weather_command(interaction: discord.Interaction):

    await interaction.response.defer()

    await interaction.followup.send(
        embed=await build_embed()
    )


@bot.event
async def on_ready():

    print(f"Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")
    except Exception as e:
        print(e)

    schedule(post_weather)


bot.run(config.TOKEN)