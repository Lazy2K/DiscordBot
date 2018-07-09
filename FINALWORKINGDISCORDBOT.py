import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

token = "NDYyMzE2NjAwOTM5NTExODA4.DhqfaA.UnFav21Y-2_QaGn_RlB00SU_GbE"


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

#List Of Commands
a = "!owner"
b = "!ping"
c = "!countdown"

commands = [a, b, c]


@client.event
async def on_ready():
    print("Bot is ready!")



@client.event
async def on_message(message):
    if message.content == "!commands":
        print("User ran !commands")
        await client.send_message(message.channel, commands)
################################################################
    if message.content == a:
        print("User ran !owner")
        await client.send_message(message.channel, "The Owners of this Server are: <@259082317752958976> & <@195233589359673344>")
################################################################
    if message.content == b:
        print("User ran !ping")
        await client.send_message(message.channel, "pong")
################################################################
    if message.content == c:
        print("User ran !countdown")
        await client.send_message(message.channel, "3")
        time.sleep(1)
        await client.send_message(message.channel, "2")
        time.sleep(1)
        await client.send_message(message.channel, "1")
        time.sleep(1)
        await client.send_message(message.channel, "GO!!!")
################################################################
    if message.content == "!help":
        print("User ran !help")
        await client.send_message(message.channel, "To view all commands type ``` !commands ```")
##################################################################
    if message.content == "!spam":
        print("User ran !spam")
        for range in (1,100):
            await client.send_message(message.channel, "FUCK YOU!!!")
            time.sleep(0.3)


                            



client.run(token)
