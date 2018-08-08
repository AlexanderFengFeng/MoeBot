import discord
import json

with open('./data/meat.json', 'r') as f: 
    data = json.load(f)

def meat_list():
    output = 'The meats the mansion have are '
    animals = data['animals']
    for i in animals:
        if i is animals[len(animals)-1]:
            output += 'and ' + i + '.'
        else:
            output += i + ', '
    output += '\n\nType !meat *animal* to see what meats '\
              'we have available for that animal.'
    return discord.Embed(description=output, color=0xb41615)

def meat_cuts(animal):
    if animal not in data['animals']:
        output = 'That animal is not in our list of meats'
    else:
        output = 'The meats available for %s are ' % animal
        cuts = data['meats'][data['animals'].index(animal)]['cuts']
        for i in cuts:
            if i is cuts[len(cuts)-1]:
                output += 'and ' + i + '.'
            else:
                output += i + ', '
    return discord.Embed(description=output, color=0xb41615)
    
