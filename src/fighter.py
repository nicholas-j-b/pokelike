class Fighter:
    def __init__(self):
        self.health = 100
        self.attacks = {}

    def receiveEffects(self, effects):
        self.health -= effects

    def getAttackOptions(self):
        return self.attacks.keys()
    
    def getAttackEffects(self, attack):
        return self.attacks[attack]


class Tree(Fighter):
    def __init__(self):
        super().__init__()
        self.attacks = {'punch': 10, 'grow': 0}

    def __str__(self):
        return 'health: ' + str(self.health)