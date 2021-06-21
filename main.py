import discord
import os

TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

# Bot code
@client.event
async def on_message(message):
  if message.author == client.user: # dont respond to self
    return

  if message.channel.id == 856607621971836988:
    if "http" in message.content or message.attachments:
      await message.add_reaction('<a:tickgreen:850803068110766120>')
      await message.add_reaction('<a:tickred:850803121491017728>')
    else:
      await message.delete()

client.run(TOKEN)