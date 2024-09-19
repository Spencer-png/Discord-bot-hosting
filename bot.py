import discord
import random
import string

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = 'MTI4NjA5MzA3NjEyOTEyMDI3NQ.Gc_YuC.EPJA3G5F4mB5j3PVmfgHfWESFhgF8XtdR2yNN0'

def generate_invite_code(length=8):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!generate_invite'):
        invite_code = generate_invite_code()
        await message.channel.send(f'Your invite code: {invite_code}')

client.run(TOKEN)
