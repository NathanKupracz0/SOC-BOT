import discord
from discord.ext import commands   
import logging
from dotenv import load_dotenv
import os   

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True


bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"We are ready to go in,{bot.user.name} ")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server, {member.name}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "nazi" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "chink" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "cooney" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "cotton picker" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "curry muncher" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "gringo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "gypsy" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "jiggaboo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "jiggerboo" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "nigger" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "nigga" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "pickaninny" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    if "shitskin" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention}, such language is not allowed here.")
    await bot.process_commands(message)   



bot.run(token, log_handler=handler, log_level=logging.DEBUG)

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! How can I assist you today?")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)