import discord
import json
import requests
from datetime import datetime
from media.emojis.emojis import EmojiHandler

class FortniteHandler(object):
    def __init__(self):
        with open('./auth.json', 'r') as f:
            data = json.load(f)
            self._trn_key = data['TRN-API-key']
            self._fnbr_key = data['fnbr-API-key']

        self._url_base = {'trn': 'https://api.fortnitetracker.com/v1/',
                          'fnbr': 'https://fnbr.co/api/'}
        self._headers = {'content-type': 'application/json',
                         'fnbr-api-key': self._fnbr_key,
                         'trn-api-key': self._trn_key}


        self.emojis = EmojiHandler('./media/emojis/emojis.json')
        self.color = 0x90ee90

    def _format_url(self, base, *args):
        """Formats url using base and its extensions

        Parameters
        ----------
        base
            Name of the API that is being requested from
        *args
            Extensions being added to url base
        
        Return
        ------
        string
            Formatted url
        """
        url = self._url_base[base] + '/'.join(args)
        return url
    
    def _get(self, url):
        response = requests.get(url, headers=self._headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def _get_time(self, date):
        return date.strftime('%B %d, %Y %I:%M %p')

    def _convert_time_str(self, time_str):
        date = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f')
        return self._get_time(date)

    def _add_item(self, embed, item):
        rarity = item['rarity']
        name = item['name']
        value = 'Price: '+item['price']+\
                self.emojis.get_emoji_post('fn_vbuck')+'\n'
        value += 'Rarity: '+rarity.capitalize()+\
                 self.emojis.get_emoji('fn_'+rarity)
        embed.add_field(name=name, value=value)

    def store(self):
        url = self._format_url('fnbr', 'shop')
        data = self._get(url)['data']
        
        embed = discord.Embed(title=self.emojis.get_emoji_pre('fn_logo')+\
                                    'Sales for %s'\
                                    % self._get_time(datetime.now()),
                              color=self.color)

        llama = self.emojis.get_emoji('fn_llama')

        embed.add_field(name='Remember that daily items in the store '+\
                             'will refresh at **5:00 PM PST**.',
                        value=llama+' **Featured** '+llama, inline=False)
        for item in data['featured']:
            self._add_item(embed,item)

        embed.add_field(name='\u200b',
                        value=llama+' **Daily** '+llama, inline=False)
        for item in data['daily']:
            self._add_item(embed, item)
        return embed

    def _add_stat(self, embed, stat):
        key = stat['key']
        value = stat['value']
        embed.add_field(name=key, value=value)

    def _format_stats(self, stats):
        lines = []
        if not stats:
            labels = ['Matches', 'Wins', 'Win %', 'Kills', 'K/d']
            for label in labels:
                lines.append('[**'+label+'**]\t'+'None')
        else:
            keys = ['matches', 'winRatio', 'kills', 'kd']
            for key in keys:
                lines.append('[**'+stats[key]['label']+'**]\t'+\
                             stats[key]['value'])
            lines.insert(1, '[**Wins**]\t'+str(int(stats['winRatio']['valueDec']*\
                         stats['matches']['valueInt']/100)))
        value = '\n'.join(lines)
        return value

    def stats(self, args):
        user = ' '.join(args)
        url = self._format_url('trn', 'profile', 'pc', user)
        data = self._get(url)
        if not data:
            raise ValueError('Did not get data')
        epic_user = data['epicUserHandle']
        lifetime = data['lifeTimeStats'][7:]
        stats = data['stats']
        if 'p2' in stats.keys():
            solo = stats['p2']
        else:
            solo = None
        if 'p10' in stats.keys():
            duo = stats['p10']
        else:
            duo = None
        if 'p9' in stats.keys():
            squad = stats['p9']
        else:
            squad = None

        embed = discord.Embed(title=self.emojis.get_emoji_pre('fn_logo')+\
                              '%s: Lifetime Stats' % epic_user,
                              color=self.color)
        for stat in lifetime:
            self._add_stat(embed, stat)
        embed.add_field(name='\u200b', value='\u200b')

        embed.add_field(name=self.emojis.get_emoji_pre('fn_solo')+\
                        'Solo',
                        value=self._format_stats(solo), inline=True)
        embed.add_field(name=self.emojis.get_emoji_pre('fn_duo')+\
                        'Duo',
                        value=self._format_stats(duo), inline=True)
        embed.add_field(name=self.emojis.get_emoji_pre('fn_squad')+\
                        'Squad',
                        value=self._format_stats(squad), inline=True)

        return embed


#    def item(self, *args):
#        if not args:
#            embed = discord.Embed(title='Try !m fortnite item {itemname}')
#            return embed
#        url = self._format_url('fnbr', 'item', 'search=%s' % args[0])
#        data = self._get(url)
#        embed = discord.Embed(title=args[0])
#        embed.set_image


        


