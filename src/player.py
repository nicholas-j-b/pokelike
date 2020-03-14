from fighter import Tree
from controller import HumanController, AIController
from gameState import GameState

class Player:
    def __init__(self, name):
        self.name = name
        self.fighters = []
        self.controller = None
    
    def getName(self):
        return self.name

    def setActiveFighter(self):
        self.activeFighter = self.fighters[0]
    
    def getActiveFighter(self):
        return self.activeFighter

    def turn(self):
        activeAgent = self.activeFighter
        options = activeAgent.getAttackOptions()
        decision = self.controller.decide(options)
        effect = activeAgent.getAttackEffects(decision)
        receptiveAgent = GameState.getEnemyActive(self.name)
        receptiveAgent.receiveEffects(effect)

    def __repr__(self):
        return str(self.activeFighter)

class Human(Player):
    def __init__(self, name):
        super().__init__(name)
        self.fighters = [Tree()]
        self.controller = HumanController()
        self.setActiveFighter()

class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.fighters = [Tree()]
        self.controller = AIController()
        self.setActiveFighter()