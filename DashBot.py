import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() 
client = commands.Bot(command_prefix = "!") 


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") 

@client.event
async def on_message(message):
    if message.content == "hello":
        await client.send_message(message.channel, ":wave:")
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))    

client.run("NDMyMjY2Njc4OTUzNTc0NDIy.Daq1tQ.MOngmk7nnJ9z6xpmJ5b2zkP56NM") 

