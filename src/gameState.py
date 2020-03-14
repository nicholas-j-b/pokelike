class GameState:
    players = {}

    @staticmethod
    def getEnemy(playerName):
        return [v for (k, v) in GameState.players.items() if k != playerName][0]
    
    @staticmethod
    def getEnemyActive(playerName):
        return GameState.getEnemy(playerName).getActiveFighter()

    @staticmethod
    def initPlayers(players):
        GameState.players = players

    #@staticmethod
    #def turnEffect():
        #GameState.players
    
    @staticmethod
    def debugPrint():
        print(GameState.players)