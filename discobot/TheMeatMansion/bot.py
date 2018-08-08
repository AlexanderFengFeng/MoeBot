import discord
import json
import functions as func
from discord.ext import commands

with open('./auth.json', 'r') as f:
    auth = json.load(f)
with open('./data/meat.json', 'r') as f:
    data = json.load(f)

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def steak(ctx):
    await ctx.send('https://media0.giphy.com/media/c11ISnPiRdis8/giphy.gif')

@bot.command()
async def meat(ctx, *args):
    if len(args) == 0:
        await ctx.send(embed=func.meat_list())
    else:
        await ctx.send(embed=func.meat_cuts(args[0]))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="TheMeatMansion",
                          description="The meatiest mansions around",
                          color=0xb41615)
    
    # give info about you here
    embed.add_field(name="Author", value="TheMeatMangler")
    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="TheMeatMansion",
                          description="The meatiest mansion around. "\
                                      "List of commands are:",
                          color=0xb41615)

    embed.add_field(name="!steak",
                    value="Gives a juicy steak gif",
                    inline=False)

    embed.add_field(name="!meat",
                    value="Gives list of meats and associated cuts",
                    inline=False)

    embed.add_field(name="!info",
                    value="Gives a little info about the bot",
                    inline=False)

    embed.add_field(name="!help",
                    value="Gives this message",
                    inline=False)

    await ctx.send(embed=embed)

bot.run(auth['token'])
