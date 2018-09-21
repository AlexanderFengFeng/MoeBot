import discord
import json
import requests

class FortniteHandler(object):
    def __init__(self):
        with open('./auth.json', 'r') as f:
            self._key = json.load(f)['TRN-Api-Key']

        self.color = 0x90ee90
        self._url_base = 'https://api.fortnitetracker.com/v1/'
        self._headers = {'content-type': 'application/json',
                         'trn-api-key': self._key}

    def _format_url(self, *args):
        url = self._url_base + '/'.join(args)
        return url
    
    def _get(self, url):
        print(url)
        response = requests.get(url, headers=self._headers)

        if response.status_code == 200:
            return json.loads(response.content.decode('utf-8'))
        else:
            return None

    def store(self):
        url = self._format_url('store')
        store_data = self._get(url)
        
        embed = discord.Embed(title='What\'s in the store today',
                              description="1500 <:vbuck:492496592419684365>",
                              color=self.color)

        return embed
        for item in store_data:
            pass

            

        


