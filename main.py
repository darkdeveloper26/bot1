import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import time
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("OTc0MjI5MDgxNDAwOTYzMTcy.GxJpxc.DmPN3Uc8djQ5D9VQQIIJZBqCVpJYyXFocYDJO4")
#Bot command thing prefix
bot = commands.Bot(command_prefix="&")


# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("✿﹕sushiㆍᶻz is in " + str(guild_count) + " server.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.command(name='8ball')
async def _8ball(ctx):
  await ctx.channel.send('Henlo guys welcome')

@bot.command(name=('exit'))
async def close(ctx):
  await ctx.channel.send('Closing for maintenance...')
  time.sleep(0.5)
  exit(0)

@bot.command()
async def servercount(ctx):
  await ctx.channel.send('Checking...')
  time.sleep(2.5)
  await ctx.channel.send("✿﹕sushiㆍᶻz is in " + str(guild_count) + " server.")



# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
bot.run("OTc0MjI5MDgxNDAwOTYzMTcy.GxJpxc.DmPN3Uc8djQ5D9VQQIIJZBqCVpJYyXFocYDJO4")