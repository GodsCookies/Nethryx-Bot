from discord.ext.commands import Bot
from discord import channel
from discord.ext import commands
import discord

client = commands.Bot(command_prefix = '?',  case_insensitive=True)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity= discord.Game('discord.gg | ?helpme') )
    client.remove_command('help')
    print("The bot is ready!")

@client.event
async def on_message(message):
    ctx = await client.get_context(message)

@client.command(name='kick')
async def kick(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Staff")
    if role in ctx.author.roles:
        await ctx.send(f'You already have the role {role.name}')
    else:
        await ctx.send(" :no_entry_sign: Sorry you do not have permission to use this command")

    

@client.command(name='helpme')
async def helpme(ctx):
    channel = ctx.message.channel
    embed = discord.Embed(
        title = 'List Of Commands',
        description = '',
        colour = discord.Colour.dark_blue(),
    )
    embed.add_field(name="say", value="A Command to make the bot say something", inline="false")
    embed.add_field(name="ping", value="Pings The server", inline="false")
    embed.add_field(name="pinguser", value="A Command to ping a user of your choice", inline="false")

    await ctx.send(embed=embed)
    

@client.command(name='say')
async def say(ctx, arg):
    await ctx.send(arg)

@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Pong! {client.latency}s')

@client.command(name='pinguser')
async def pinguser(ctx,  arg):
    ctx.send(arg)    

@client.command(name='msgoftheday')
async def msgoftheday(ctx, msgofthedayd):
    ctx.send(msgofthedayd)    

msgofthedayd = "Even if todays bad tomorrow will be better"

client.run(Put Token here in quotes)
