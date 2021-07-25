import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODY4OTY5MzU2ODc5NjA5OTM4.YP3Yxw.7gE3IWSqB1Og3_FPNJlaojuy_bs')