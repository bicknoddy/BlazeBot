import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print(f'{bot.user.name} connected to Discord, meow')

@bot.event
async def on_member_update(before, after):
    print("this member has been updated")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Meow, meow meow {member.name}, meow meeeeeeow!'
    )

#regular commands

@bot.command(name='val', help="Phrase that is related to your skill level")
async def valy(ctx):
    shit_talk = [
        'U are bad',
        'Meow, ur ok.',
        'Penta or die',
        'u ain\'t radient yet??',
    ]

    response = random.choice(shit_talk)
    await ctx.send(response)

#joke commands

@bot.command(name='pp', help="Who has smol pp")
async def pp(ctx):
    aut = ctx.author.nick.capitalize()

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

#dumb name commands lol

@bot.command()
async def boddy(ctx):
    await ctx.send("Wow, Boddy is the best person here....by far. <3")

@bot.command(name='dyl')
async def dyl(ctx):
    await ctx.send("Yeah, I mean, he's aight.")

@bot.command(name='dom')
async def dom(ctx):
    await ctx.send("All hail our el presidente")

@bot.command(name='ethan')
async def ethan(ctx):
    await ctx.send("Who let this guy in here??")

@bot.command(name='aut', help='Aut gives words of wisdom')
async def aut(ctx):
    aut = ctx.author.nick.capitalize()

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


bot.run(TOKEN)