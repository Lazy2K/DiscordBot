#Linked Discord Bot
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random
import sys
import requests
import instaStat
from instaStat import stat_find
from discord.utils import find


token = "NjA3OTg0MTIxODQ2ODI1MDAx.XUhloQ.elSLvVzFRyFf_nH5HHhFxLBTq-k"
Client = discord.Client()
prefix = "!"
client = commands.Bot(command_prefix = prefix)


#setup
member_join_message = ""
member_join_channel = ""



@client.event
async def on_ready():
    print("Bot is ready!")

@client.command(pass_context=True)
async def test(ctx):
    await client.say("Test")
    await client.say("Test " + ctx.message.server.name)
    await client.say("Test #" + ctx.message.channel.name)





    

@client.event
async def on_member_join(member): #Triggers when member joins
    await client.send_message(member,member_join_message)

@client.event
async def on_message_delete(message):
    await client.send_message(message.channel, "*Why did you delete that?*")

@client.command(pass_context=True)
async def users(ctx):
    server = ctx.message.server
    await client.say("*" + server.name + " has " + str(server.member_count) + " users!*")

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("*Pong*")

@client.command(pass_context=True)
async def insta(ctx):
    fullCommand = ctx.message.content
    username = fullCommand[7::]
    await client.say("*Checking the stats for* @" + username)
    if stat_find(username) == "non":
        await client.say("*Sorry, I couldn't find any accound with ther username* @" + username)
    else:
        await client.say("@" + username + " *has* " + stat_find(username))
    
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.add_reaction(ctx.message, "✅")
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await client.add_reaction(ctx.message, "✅")
    await voice_client.disconnect()

client.run(token)
