import discord
import json
from fortnite import FortniteHandler

client = discord.Client()

fortnite = FortniteHandler()

with open('.auth.json', 'r') as f:
    _token = json.load(f)['token']

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    args = message.content.split()

    if args[0] != '!m' or len(args) <= 1:
        return

    if args[1] == 'help':
        embed = discord.Embed(title="MoeBot",
                              description="Work in progress",
                              color=0xb41615)

        embed.add_field(name="!m info",
                        value="Gives a little info about the bot")

        embed.add_field(name="!m help",
                        value="Gives this message")

        embed.add_field(name="!m fn store",
                        value="Gives current Fortnite store info")

        embed.add_field(name="!m fn item {item name}",
                        value="Gives info for an item in Fortnite")

        embed.add_field(name="!m fn stats {epic username}",
                        value="Gives stats for a PC player in Fortnite")

        embed.add_field(name="!m fn challenges",
                        value="Gives info on battle pass challenges" +\
                              " for the current week")
        await client.send_message(message.channel, embed=embed)
    
    elif args[1] == 'info':
        embed = discord.Embed(title="TheMoeBot",
                          description="~Uguuuu~",
                          color=0xb41615)
        embed.add_field(name="Author", value="AlexanderFengFeng")
        await client.send_message(message.channel, embed=embed)

    elif args[1] == 'fn':
        if len(args) <= 2:
            embed = discord.Embed(description="Fortnite functions",
                              color=fortnite.color)
        elif args[2] == 'store':
            embed = fortnite.store()
        elif args[2] == 'item':
            embed = fortnite.item(args[3:])
        elif args[2] == 'stats':
            embed = fortnite.stats(args[3:])
        elif args[2] == 'challenges':
            embed = fortnite.challenges()
        else:
            embed = discord.Embed(description='Command failed. Try !m help.',
                                  color=fortnite.color)
        await client.send_message(message.channel, embed=embed)

    elif args[1] == 'yeet':
        embed = discord.Embed(title="*Y E E T*", color=0xff8c00)
        embed.set_image(url='https://media1.tenor.com/images/202045f7022731b513a4a836744d9765/tenor.gif')
        await client.send_message(message.channel, embed=embed)

client.run(_token)
