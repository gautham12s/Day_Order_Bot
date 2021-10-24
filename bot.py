import discord
from discord.ext import commands

r = input("Enter Todays Day Order")










dyorder = {1:"9-950(Chemistry),950-1040(Chemistry),1050-1230(PPS),120-210(Maths)",2:"9-1040(FL),1050-1230(Civil Engg),120-210(GA),210-350(Chemistry Lab)",3:"9-1040(Maths),1050-1140(Chemistry),1140-1230(GA),120-210(FL),210-350(PPS Lab)",4:"9-950(Value Ed.),1050-1140(FL),120-210(Civil Engg),210-350 (Civil Engg Lab)",5:"1050-1140(Maths),1140-1230(PPS),120-210(Chemistry)"}

client = commands.Bot(command_prefix="!>")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def dayorder(ctx):
    await ctx.send(r)

@client.command()
async def dy1(ctx):
    await ctx.send(dyorder[1])
@client.command()
async def dy2(ctx):
    await ctx.send(dyorder[2])
@client.command()
async def dy3(ctx):
    await ctx.send(dyorder[3])
@client.command()
async def dy4(ctx):
    await ctx.send(dyorder[4])
@client.command()
async def dy5(ctx):
    await ctx.send(dyorder[5])



client.run("NzcwNTAzMDYxNDk1MzQ5MjUw.X5eg5Q.4_6GrMZGzlBnBhk68oqdXiElo5M")
