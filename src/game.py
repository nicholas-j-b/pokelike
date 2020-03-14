from player import Human, AI
from gameState import GameState

class Game:
    def __init__(self):
        first = 'first'
        second = 'second'
        self.players = {first: Human(first), second: AI(second)}
        GameState.initPlayers(self.players)

    def start(self):
        while(True):
            self.loop()

    def loop(self):
        for player in self.players.values():
            player.turn()
        GameState.debugPrint()