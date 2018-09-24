import json

class EmojiHandler(object):
    def __init__(self, loc):
        with open(loc, 'r') as f:
            self.emojis = json.load(f)

    def get_emoji_pre(self, name):
        emoji = self.get_emoji(name)
        return emoji+' '

    def get_emoji_post(self, name):
        emoji = self.get_emoji(name)
        return ' '+emoji

    def get_emoji(self, name):
        return self.emojis[name]
