import json
from urllib.request import Request, urlopen

class AnimeHandler(object):
    def __init__(self):
        self._token = 'https://api.jikan.moe/v3/anime/'

    def _format_url(self, args):
        _url = self._token + '/'.join(args)
        return _url

    def seasonal(self, block):
        pass
        url = self._format_url('season')
        request = Request(url)
        data = json.loads(urlopen(request).read)

        season_name = data['season_name']
        season_year = str(data['season_year'])
        season = ' '.join([season_name, season_year])
        anime = data['anime']


