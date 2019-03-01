from errbot import BotPlugin, botcmd
import requests


class Dadjoke(BotPlugin):
    """
    get a random dad joke
    """

    @botcmd()
    def dadjoke(self, message, args):
        """get a random dad joke"""
        return requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).content.decode()
