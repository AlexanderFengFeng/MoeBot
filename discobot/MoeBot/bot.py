import discord
import json
from discord.ext import commands
from handlers.anime import AnimeHandler
from fortnite import FortniteHandler

bot = commands.Bot(command_prefix='!m ')
bot.remove_command('help')
anime = AnimeHandler()
fortnite = FortniteHandler()

class MoeBot(object):
    def __init__(self):
        with open('./auth.json', 'r') as f:
            self._token = json.load(f)['token']

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

    @bot.command()
    async def help(ctx):
        embed = discord.Embed(title="MoeBot",
                              description="Work in progress",
                              color=0xb41615)

        embed.add_field(name="!info",
                        value="Gives a little info about the bot")

        embed.add_field(name="!help",
                        value="Gives this message")

        embed.add_field(name="!anime",
                        value="Learn about awesome animes")

        await ctx.send(embed=embed)

    @bot.command()
    async def info(ctx):
        embed = discord.Embed(title="TheMeatMansion",
                              description="The meatiest mansion around",
                              color=0xb41615)
        
        embed.add_field(name="Author", value="TheMeatMangler")
        embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

        await ctx.send(embed=embed)

#    @bot.command()
#    async def anime(ctx, *args):
#        if not args:
#            embed = discord.Embed(description="Try !anime seasonal",
#                                  color=0xffb6c1)
#            embed = discord.Embed(description = 'https://myanimelist.net/anime/37497/Irozuku_Sekai_no_Ashita_kara',
#                    color = 0xffb6c1)
#            embed.set_thumbnail(url='https://myanimelist.cdn-dena.com/images/anime/1424/93855.jpg?s=4c08edcdff5521d159b0fda21e80efd3')
#        else:
#            if args[1] == 'seasonal':
#                embed = self.anime.seasonal(0)
#
#        await ctx.send(embed=embed)

    @bot.command()
    async def fortnite(ctx, *args):
        if not args:
            embed = discord.Embed(description="Fortnite functions",
                                  color=fortnite.color)
        elif args[0] == 'store':
            embed = fortnite.store()
        #elif args[0] == 'items':
        #    if len(args) > 1:
        #        embed = fortnite.item(args[1:])
        #    else:
        #        embed = fortnite.item()
        elif args[0] == 'stats':
            embed = fortnite.stats(args[1:])
        await ctx.send(embed=embed)

    @bot.command()
    async def yeet(ctx):
        embed = discord.Embed(title="*Y E E T*", color=0xff8c00)
        embed.set_image(url='https://media1.tenor.com/images/202045f7022731b513a4a836744d9765/tenor.gif')
        await ctx.send(embed=embed)

if __name__ == "__main__": 
    MoeBot = MoeBot()
    bot.run(MoeBot._token)
