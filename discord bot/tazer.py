import discord
from discord.ext import commands
client=commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('bot is ready.')


@client.command()
async def candy(ctx):
    await ctx.send('yummy XD!')
@client.command()
async def chocolate(ctx):
    await ctx.send('yummy XD!')
@client.command()
async def yourmom(ctx):
    await ctx.send('yummy XD!')
@client.command()
async def salt(ctx):
    await ctx.send('salty? duh')
@client.command()
async def chips(ctx):
    await ctx.send('depends')
@client.command()
async def chilis(ctx):
    await ctx.send('ahhh get me some water :(')
@client.command()
async def sweets(ctx):
    await ctx.send('yummy XD!')
@client.command()
async def water(ctx):
    await ctx.send("what's that lol")
@client.command()
async def swati(ctx):
    await ctx.send('eww LMAO')




client.run('ODAyNzY1OTgwMzc5Nzc0OTgw.YA0AFA.dkP3Xm6uqPI9Qss7ajJF66iEr_4')            
