import discord
import random
import string

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = 'BOT_TOKEN_HERE'

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/hello'):
        await message.channel.send(f'Hello there!')

client.run(TOKEN)
