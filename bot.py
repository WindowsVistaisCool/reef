import discord
from discord.ext import commands

client = commands.Bot(command-prefix='./')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='DAN7EH | ./help'))
  
@client.command()
async def help(ctx):
  e = discord.Embed(title="REEF HELP")
  e.add_field(name='Commands:', value='./invite')
  await ctx.channel.send(embed=e)

@client.command()
async def invite():
    await message.channel.send("https://discord.gg/ns7hHDy")
    
@client.command()
@commands.has_permissions(manage_members=True)
async def purge(ctx):
      purgeme = int(purgeme)
      purgeme = purgeme+1
      await ctx.channel.purge(limit=purgeme)


client.run("NzY5MjMyOTQwNzg5MTM3NDE4.X5MCAA.447N_lKUN_wnZCWs9ZpmwSczcVo")
