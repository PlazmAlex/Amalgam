class SaveFile:
    def __init__(self, name):
        self.name = name
        #Stats
        self.hp = 20
        self.maxhp = 20
        self.attack = 4
        self.defense = 1
        self.maxattack = 4
        self.AP = 0
        self.maxAP = 0
        self.maxdefense = 1
        #---
        #Battle states
        self.abilityUsed = False
        self.guard = False
        self.superAttack = False
        self.bleed = 0
        self.vulnerable = False
        self.canUseAbilities = True
        self.timeLoop = 0
        self.statEffects = []
        self.statChanges = []
        self.statDuration = []
        #===
        self.abilities = []
        self.allAbilities = []
        self.battleOptions = ["Attack", "Abilities", "Guard"]
        self.currentOptions = ["Attack", "Abilities", "Guard"] 
        self.lastAbilityUsed = [""]
        self.lastAction = [""]
class Enemy:
    def __init__(self, name, hp, attack, defense,sTurns,gTurns,dTurns,ability):
        self.name = name
        #Stats
        self.hp = hp
        self.defense = defense
        self.attack = attack
        self.maxhp = hp
        self.maxattack = attack
        self.maxdefense = defense
        self.AP = 100
        #---
        #Battle states
        self.guard = False
        self.debuff = False
        self.superAttack = False
        self.vulnerable = False
        self.bleed = 0
        self.statEffects = []
        self.statChanges = []
        self.statDuration = []
        #---
        #Turn data
        self.superTurn = sTurns
        self.guardTurn = gTurns
        self.debuffTurn = dTurns
        #---
        self.ability = ability
        self.lastAbilityUsed = [""]
        self.lastAction = [""]