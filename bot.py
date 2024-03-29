import discord
import json
from os import system
from discord.ext import commands

client = commands.Bot(command_prefix='./')
client.remove_command('help')

def write(file, key=None, val=None, read=False, spec=False):
	with open(file, 'r') as v:
		x = json.load(v)
	if read == False:
		x[key] = val
		with open(file, 'w') as v:
			json.dump(x, v, indent=4)
	else:
		if spec is not False:
			return x[key]
		else:
			return x

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='DAN7EH | ./help'))
	print("ready")

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.NotOwner) or isinstance(error, commands.CheckFailure):
		await ctx.send("No Permission!")
	elif isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
		await ctx.send("Arg error")
	else:
		await ctx.send(f"Error {error}")

@client.event
async def on_message(message):
	if message.author.bot:
		return
	await client.process_commands(message)

@client.command()
@commands.is_owner()
async def execute(ctx, com):
	system(com)
	await ctx.send("done")

@client.command()
async def help(ctx, comma=None):
	e = discord.Embed(title="REEF HELP", color=discord.Color.dark_blue())
	e.add_field(name='Commands:', value='./invite\n./report\n./suggest')
	e.add_field(name='Coming Soon:', value='None')
	if comma is not None:
		if comma is "invite":
			await ctx.send("Use \"./invite\" to get the invite for the server.")
		elif comma is "report":
			await ctx.send("Use \"./report @member reason\" to report a user to the admins.")
		elif comma is "suggest":
			await ctx.send("User \"./suggest idea\" to suggest an idea to the admins.")
		else:
			await ctx.send(embed=e)
	else:
		await ctx.send(embed=e)

@client.command()
async def invite(ctx):
	await ctx.send("https://discord.gg/ns7hHDy")

@client.command()
@commands.is_owner()
async def input(ctx, file, key, val):
	with open(file, 'r') as v:
		x = json.load(v)
	x[key] = val
	with open(file, 'w') as v:
		json.dump(x, v, indent=4)

@client.command()
@commands.has_permissions(manage_roles=True)
async def purge(ctx, purgeme):
	purgeme = int(purgeme)
	purgeme = purgeme+1
	await ctx.channel.purge(limit=purgeme)

@client.command()
@commands.is_owner()
async def stop(ctx):
	await ctx.message.delete()
	await ctx.send("kk")
	await client.close()

@client.command()
async def report(ctx, member: discord.Member, *, reason="Bad Behavior"):
	if member.id == ctx.author.id:
		await ctx.send("You can't warn yourself, silly!")
		return
	elif member.id == client.user.id:
		await ctx.send("You can't warn me, silly!")
		return
	elif member.bot:
		await ctx.send("You can't warn bots, silly!")
		return

	with open("config.json", 'r') as v:
		x = json.load(v)
	chn = x["rch"]
	channel = client.get_channel(int(chn))
	e = discord.Embed(title=f"{ctx.author} reported {member} for ", color=discord.Color.red())
	e.add_field(name="Reason:", value=reason)
	await channel.send(embed=e)

@client.command()
async def suggest(ctx, messa="Good server!"):
	x = write('config.json', "sch", read=True, spec=True)
	chn = client.get_channel(int(x))
	await ctx.send("Thank you for your suggestion, we will review it soon.")
	await chn.send(f"Suggestion from {ctx.author.name}: {messa}")

client.run("NzY5MjMyOTQwNzg5MTM3NDE4.X5MCAA.447N_lKUN_wnZCWs9ZpmwSczcVo")
