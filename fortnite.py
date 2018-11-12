import discord
import json
import requests
from datetime import datetime
from media.emojis.emojis import EmojiHandler

class FortniteHandler(object):
    def __init__(self):
        with open('.auth.json', 'r') as f:
            data = json.load(f)
            self._trn_key = data['TRN-API-key']
            self._fnbr_key = data['fnbr-API-key']

        self._url_base = {'trn': 'https://api.fortnitetracker.com/v1/',
                          'fnbr': 'https://fnbr.co/api/'}
        self._headers = {'content-type': 'application/json',
                         'fnbr-api-key': self._fnbr_key,
                         'trn-api-key': self._trn_key}


        self.emojis = EmojiHandler('./media/emojis/emojis.json')
        self._logo = self.emojis.get_emoji_pre('fn_logo')
        self.color = 0x90ee90

    def _format_url(self, base, extensions, args=None):
        """Formats url using base and its extensions

        Parameters
        ----------
        base: str
            Name of the API that is being requested from
        extensions: list of str
            Extensions being added to url base
        args: list of str
            Arguments to add to url
        
        Return
        ------
        string
            Formatted url
        """
        url = self._url_base[base] + '/'.join(extensions)
        if args:
            url += '?'
            url += '&'.join(args);
        return url
    
    def _get(self, url):
        """Extension of HTTP get request"""
        response = requests.get(url, headers=self._headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def store(self):
        """Creates an embed which displays current store offerings"""
        url = self._format_url('fnbr', ['shop'])
        data = self._get(url)['data']
        
        date = self._get_time(datetime.now())
        embed = discord.Embed(title='%s Sales for %s' % (self._logo, date),
                              color=self.color)

        llama = self.emojis.get_emoji('fn_llama')
        embed.add_field(name='Remember that daily items in the store '+\
                             'will refresh at **5:00 PM PST**.',
                        value='{0} **Featured** {0}'.format(llama), inline=False)
        # Adds featured items in a unique block
        for item in data['featured']:
            self._add_item(embed, item)

        embed.add_field(name='\u200b',
                        value='{0} **Daily** {0}'.format(llama), inline=False)
        # Adds daily items in its own block
        for item in data['daily']:
            self._add_item(embed, item)
        return embed

    def stats(self, args):
        """Creates an embed which displays statistical information
        for a PC user"""
        user = ' '.join(args)
        url = self._format_url('trn', ['profile', 'pc', user])
        data = self._get(url)
        if not data:
            raise ValueError('Did not get data')
        epic_user = data['epicUserHandle']
        # Omits Top X stats
        lifetime = data['lifeTimeStats'][7:]
        stats = data['stats']
        # Solo
        if 'p2' in stats.keys():
            solo = stats['p2']
        else:
            solo = None
        # Duo
        if 'p10' in stats.keys():
            duo = stats['p10']
        else:
            duo = None
        # Squad
        if 'p9' in stats.keys():
            squad = stats['p9']
        else:
            squad = None

        embed = discord.Embed(title='%s %s: Lifetime Stats' % (self._logo,
                                                               epic_user),
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
        embed.add_field(name=self.emojis.get_emoji_pre('fn_bp')+\
                        'Squad',
                        value=self._format_stats(squad), inline=True)

        return embed

    def item(self, args):
        """Creates an embed which displays information and
        images for an item"""
        if not args:
            embed = discord.Embed(title='%s Try !m fn item {itemname}'
                                      % self._logo)
            return embed
        item_name = ' '.join(args)
        url = self._format_url('fnbr', ['images'], ['search=%s' % item_name])
        item = self._get(url)['data'][0]
        images = item['images']
        
        embed = discord.Embed(title='%s Details for %s' % (self._logo,
                                                           item['name']),
                              color=self.color)

        self._add_item(embed, item)
        if images['featured']:
            embed.set_image(url=images['featured'])
        elif images['png']:
            embed.set_image(url=images['png'])
        
        if embed.image:
            embed.set_thumbnail(url=images['icon'])
        else:
            embed.set_image(url=images['icon'])
        
        return embed

    def challenges(self):
        url = self._format_url('trn', ['challenges'])
        data = self._get(url)
        if data:
            challenges = data['items']

        date = self._get_date(datetime.now())
        embed = discord.Embed(title='%s Challenges for the week of %s'
                                  % (self._logo, date),
                              color=self.color)

        for challenge in challenges:
            chal_dict = self._format_challenge(challenge)
            self._add_challenge(embed, chal_dict)

        return embed


    # Private helper functions
    def _convert_time_str(self, time_str):
        """Converts string representation of datetime to readable
        string format of date"""
        date = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%f')
        return self._get_time(date)

    def _get_time(self, date):
        """Reformats datetime variable into readable string
        for date and time"""
        return date.strftime('%B %d, %Y %I:%M %p')

    def _get_date(self, date):
        """Reformats datetime variable into readable string for date"""
        return date.strftime('%B %d, %Y')

    def _add_item(self, embed, item):
        """Adds a field to an embed object for an item, including 
        its name, price, rarity, and item type"""
        # Collects usable values
        rarity = item['rarity']
        raritemoji = self.emojis.get_emoji('fn_'+rarity)
        name = item['name']
        price = item['price']
        icon = item['priceIcon']
        item_type = item['readableType']

        # Assings battle pass or vbuck emoji
        if icon == 'vip':
            emoji = self.emojis.get_emoji_post('fn_bp')
        else:
            emoji = self.emojis.get_emoji_post('fn_vbuck')

        value = 'Price: %s%s\n' % (price, emoji)
        value += 'Rarity: %s%s\n' % (rarity.capitalize(), raritemoji)
        value += 'Type: %s' % item_type
        embed.add_field(name=name, value=value)

    def _format_challenge(self, challenge):
        chal_dict = {}
        for row in challenge['metadata']:
            if 'value' in row:
                chal_dict[row['key']] = row['value']
        return chal_dict

    def _add_challenge(self, embed, challenge):
        name = challenge['name']
        amount = challenge['questsTotal']
        reward = challenge['rewardName']
        emoji = self.emojis.get_emoji_post('fn_bp_point')
        if amount == '1' and 'Stage 1' in name:
            value = 'Reward: 5 or 10%s across multiple stages' % emoji
        elif amount == '1':
            value = 'Reward: %s%s' % (reward, emoji)
        elif 'Stage 1' in name:
            value = 'Amount: %s\nReward: 5 or 10%s across multiple stages'\
                        % (amount, emoji)
        else:
            value = 'Amount: %s\nReward: %s%s' % (amount, reward, emoji)

        embed.add_field(name=name, value=value, inline=False)

    def _add_stat(self, embed, stat):
        """Adds a field to an embed object for a stat, including its
        name and value"""
        key = stat['key']
        value = stat['value']
        embed.add_field(name=key, value=value)

    def _format_stats(self, stats):
        """Formats string for embed object's value by taking stats
        data and formatting it into a single string delimited by newlines"""
        lines = []
        if not stats:
            labels = ['Matches', 'Wins', 'Win %', 'Kills', 'K/d']
            for label in labels:
                lines.append('[**%s**]\tNone' % label)
        else:
            keys = ['matches', 'winRatio', 'kills', 'kd']
            for key in keys:
                lines.append('[**'+stats[key]['label']+'**]\t'+\
                             stats[key]['value'])
            lines.insert(1, '[**Wins**]\t'+\
                         str(int(stats['winRatio']['valueDec']*\
                         stats['matches']['valueInt']/100)))
        value = '\n'.join(lines)
        return value

        


