import discord
import json
from discord.ext import commands

with open('./auth.json', 'r') as f:
    auth = json.load(f)
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="MoeBot",
                          description="Work in progress",
                          color=0xb41615)

    embed.add_field(name="!info",
                    value="Gives a little info about the bot")

    embed.add_field(name="!help",
                    value="Gives this message")

    await ctx.send(embed=embed)

bot.run(auth['token'])
