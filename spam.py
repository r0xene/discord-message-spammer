import discord
import asyncio

# Botun token'ını buraya gir
TOKEN = 'BURAYA_TOKEN_GİR'

# Kanal ID'sini buraya gir
CHANNEL_ID = 'BURAYA_KANAL_ID_GİR'

# Mesaj
MESSAGE = 'BURAYA_GÖNDERİLECEK_MESAJI_GİR'

client = discord.Client()

@client.event
async def on_ready():
    print('Bağlandı:', client.user)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def send_message():
    await client.wait_until_ready()
    channel = client.get_channel(int(CHANNEL_ID))
    while not client.is_closed():
        await channel.send(MESSAGE)
        await asyncio.sleep(0.5)  # Mesaj aralığını ayarla

client.loop.create_task(send_message())
client.run(TOKEN)
