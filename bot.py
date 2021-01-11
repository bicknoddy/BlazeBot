import os
from os import path
import random
import discord
import db

from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} connected to Discord, meow')
    await bot.change_presence(activity=discord.Activity(type = discord.ActivityType.watching, name = 'the birds'))


@bot.event
async def on_guild_join(guild):
    db.add_guild(guild.id, guild.name)
    print("Just added {guild.name} to the database")


@bot.event
async def on_member_join(member):
    desired_channel = discord.utils.get(member.guild.text_channels, name = "general")
    await desired_channel.send(f"Meow, {member.mention} welcome to the channel *bro*")
    db.add_user(member.id, member.name, member.joined_at, member.guild.id)
    print("added {member.name} to db")



@bot.command()
async def points(ctx):
    db.update_points(ctx.author.id, ctx.guild.id, 10)

@bot.command(help="The sorting hat for Valorant")
async def val(ctx):
    shit_talk = [
        'Radient',
        'Immortal',
        'Diamond',
        'Plat',
        'Gold',
        'Silver',
        'Bronze',
        'Iron'
    ]

    response = random.choice(shit_talk)
    await ctx.send(response)

#joke commands

@bot.command(help="Who has smol pp")
async def pp(ctx):
    try:
        aut = ctx.author.nick.capitalize()
    except:
        aut = ctx.author.name.capitalize()

    peepees = [
        '{} is hiding their one inch peen',
        'Unfortunately, {} has shown everyone their two inch peen',
        'To our surprise, {}\'s three inch peen is pretty aborable',
        'No {}, a four inch peen is not average size no matter how many times you Google it',
        'Respectable five inch peen, {}',
        'I think six inches is average peen size {}, but really, how should I know',
        'Hm, that is a pretty solid seven inch peen, {}',
        'You\'ll make someone happy with that eight inch peen someday, {}',
        'Okay, put that nine inch peen away {}',
        'Just because you have a ten inch peen does not mean you have to wear grey sweats all the time, {}'
    ]
    response = random.choice(peepees)
    await ctx.send(response.format(aut))

@bot.command(help='Aut gives words of wisdom')
async def aut(ctx):
    try:
        aut = ctx.author.nick.capitalize()
    except:
        aut = ctx.author.name.capitalize()

    positives = [
        'Keep up the good work, {}',
        'You can do it, {}!',
        '{}, you fancy, huh?',
        '{}, you\'re the coolest cat!',
        'You\'re freakin awesome, {}',
        '{}, new phone, who dis?'
    ]
    response = random.choice(positives)
    await ctx.send(response.format(aut))

#dumb name commands lol

@bot.command()
async def boddy(ctx):
    await ctx.send("Wow, Boddy is the best person here....by far. <3")

@bot.command()
async def dyl(ctx):
    await ctx.send("Yeah, I mean, he's aight.")

@bot.command()
async def dom(ctx):
    await ctx.send("All hail our el presidente")

@bot.command()
async def ethan(ctx):
    await ctx.send("Who let this guy in here??")

#Games

@bot.command(help="Flip a coin!")
async def flip(ctx):
    flip = random.randint(0, 1)
    if flip == 1:
        await ctx.send("Nice u got heads. :coin:")
    else:
        await ctx.send("Tails nvr fails. :snake:")

@bot.command(help="Throw some dice!")
async def dice(ctx):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    await ctx.send("You rolled a {}, and a {}!".format(dice1, dice2))


bot.run(TOKEN)