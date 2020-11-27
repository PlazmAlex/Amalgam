class SaveFile:
    def __init__(self, name):
        self.name = name
        self.hp = 20
        self.maxhp = 20
        self.attack = 4
        self.maxattack = 4
        self.defense = 1
        self.maxdefense = 1
        self.chapter = 1
        self.guard = False
        self.abilityUsed = False
        self.superAttack = False
        self.abilities = []
        self.bleedLevel = 0
        self.abilityUses = []
        self.abilityMaxUses = []
        self.AP = 3
        self.maxAP = 3
        self.vulnerable = False
        self.canUseAbilities = True
        self.timeLoop = 0
        self.currentOptions = ["Attack", "Abilities", "Guard"] 
        self.lastAbility = [""]
class enemy:
    def __init__(self, name, hp, attack, defense,sTurns,gTurns,dTurns,ability):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.attack = attack
        self.maxattack = attack
        self.defense = defense
        self.maxdefense = defense
        self.guard = False
        self.debuff = False
        self.superAttack = False
        self.superTurn = sTurns
        self.guardTurn = gTurns
        self.debuffTurn = dTurns
        self.bleedLevel = 0
        self.ability = ability
        self.vulnerable = False
