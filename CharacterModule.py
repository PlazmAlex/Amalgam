class SaveFile:
    def __init__(self, name):
        self.name = name
        #Stats
        self.hp = 20
        self.maxhp = 20
        self.attack = 4
        self.defense = 1
        self.maxattack = 4
        self.AP = 1
        self.maxAP = 1
        self.maxdefense = 1
        #---
        #Battle states
        self.abilityUsed = False
        self.guard = False
        self.superAttack = False
        self.bleedLevel = 0
        self.vulnerable = False
        self.canUseAbilities = True
        self.timeLoop = 0
        self.statEffects = []
        self.statChanges = []
        self.statDuration = []
        #===
        self.abilities = []
        self.currentOptions = ["Attack", "Abilities", "Guard"] 
        self.lastAbilityUsed = [""]
class Enemy:
    def __init__(self, name, hp, attack, defense,sTurns,gTurns,dTurns,ability,loot):
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
        self.bleedLevel = 0
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
        self.loot = loot
        self.lastAbilityUsed = [""]
        #Loot is a list of strings that describes what is gained...
        #... from defeating this enemy
        #The string will be displayed on the ability upgrade fubction 