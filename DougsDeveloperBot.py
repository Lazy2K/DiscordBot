import requests
import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import random
import sys

token = "NDY5NTUyNDY0OTcxMTY5ODA0.DjJY0A.Ct8hbdCxbO3ZoMeexLj1jrJcV_I"


Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    
    print("Bot is ready!")




def hash(message):
        output = ""
        x = 1
        message = message.replace(" ", "")
        for i in message:
            x = x * ord(i)
            newMessage = str(x)
            for k in range(0, len(newMessage)):
                output = output + str(chr(int(newMessage[k:k + 3:])))
        output = output.replace(" ", "")
        return output
    
#\

#Supporting Stuff
commands = "__**COMMANDS**__ \n\n`!developer -- Tells you who made me!` \n\n`!seach <querey> -- Simple google search!` \n\n`!stack <querey> -- Creates a stackoverflow link to the querey!` \n\n`!hash <input> -- Hashes any input!` "

###############################################################################################################
#                                              COMMANDS                                                       #
###############################################################################################################
@client.event
async def on_message(message):
    if message.content.lower() == "!commands":   #Update the way commands are shown (Read from a text file or something) 
        await client.send_message(message.channel, "*Check your dircet messages for commands!*")
        await client.send_message(message.author,commands)

    if message.content.lower() == "!developer": #Says the o
        await client.send_message(message.channel, "*I was created by <@259082317752958976>*")

    if message.content[0:7:].lower() == "!search": #Searches Google
        search_querey = message.content[8:]
        await client.send_message(message.channel, "*Searching Google...*")
        search_querey = search_querey.replace(" ", "+")
        await client.send_message(message.channel, "https://www.google.com/search?q=" + search_querey)

    if message.content[0:6:].lower() == "!stack": #Searches Stack Overflow
        search_querey = message.content[7:]
        await client.send_message(message.channel, "*Searching StackOverlfow...*")
        search_querey = search_querey.replace(" ", "+")
        search_url = "https://stackoverflow.com/search?q=" + search_querey
        r = requests.get(search_url)
        n = (r.text)
        result = n.find('<a href="/questions/',30000)
        num = ""
        for k in range(0, 10):
            if n[result + 20 + k] != "/":
                num = num + n[result + 20 + k]
            elif n[result + 20 + k] == "/":
                break 
        url = "https://stackoverflow.com/questions/" + num
        await client.send_message(message.channel, url)
        


    if message.content[0:5:].lower() == "!hash":
        await client.send_message(message.channel,"__**WARNING**__ *This hashing algoritm is not secure! Do* ***NOT*** *use this for security purposes!*")
        to_hash = message.content[6:]
        output = hash(to_hash)
        output = output.replace(" ", "")
        await client.send_message(message.channel, "```" + output + "```")
        


    #Future Bot Features:
        #Joining/Leaving Voice Channels
        #Audio playing from youtube
        #Coffee Reminder (Reminds you every x minutes to get coffee)
        #Programming encouragement
        #Social Media APIs
        

    



client.run(token)
