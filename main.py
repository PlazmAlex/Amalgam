import os
import Character
import Combat
import Ability
import UI
import sys
#This mage effect needs to be moved into a class
mageEffect = False

print("*********\n*Amalgam*\n*********")
UI.wait()

def initialize_game():
    UI.clear()
    response = input("Enter number to select menu option\n\n1) New Run\n2) Class\n")
    UI.wait()
    
    if response == "2":
        print("No other classes unlocked")
        UI.wait()
        initialize_game()
        
    elif response == "1": 
        global SaveOne
        name = ""
        n = 1
        while (len(name) > 15 or len(name) < 1):
            UI.clear()
            if n < 2:
                limit = ""
            else:
                limit = "(15 character limit)"
            name = input("Please name your Amalgam %s\n" % limit)
            n += 1
        UI.clear()
        SaveOne = Character.SaveFile(name)
        print(("Alright " + SaveOne.name + ", time to begin your adventure."))
        input()
    else:
        initialize_game()
        
def shred(player, enemy):
    if enemy.guard == True:
        UI.clear()
        print((enemy.name + " guarded!\n"))
        UI.wait()
        UI.clear()
        return
    enemy.bleedLevel += 1
    UI.clear()
    print((enemy.name + " has been shredded!"))
    UI.wait()
def shredE(player, enemy):
    if player.guard == True:
        UI.clear()
        print((player.name + " guarded!\n"))
        UI.wait()
        UI.clear()
        return
    player.bleedLevel += 1
    UI.clear()
    print((player.name + " has been shredded!"))
    UI.wait()
def doubleeviscerate(player,enemy):
    if enemy.guard == True:
        UI.clear()
        print((enemy.name + " guarded!\n"))
        UI.wait()
        UI.clear()
        return
    enemy.bleedLevel += 2
    UI.clear()
    print((enemy.name + " was torn apart!"))
    UI.wait()    
def useAbilityEnemy(player,enemy):
    enemyAbilityLib = {
        "Shred": shredE,
        "Time Loop" : timeLoopE
    }
    enemyAbilityLib.get(enemy.ability)(player,enemy)
def heal(player, enemy):
    UI.clear()
    heal = int(round(player.maxhp * 0.70) + 1)
    player.hp = player.hp + heal
    print((player.name + " healed " + str(heal) + " HP!"))
    UI.wait()
    if player.hp > player.maxhp:
        player.hp = player.maxhp
def rejuvinate(player,enemy):
    UI.clear()
    heal = int(player.maxhp)
    player.hp = player.hp + heal
    print((player.name + " restored " + "all" + " HP!"))
    UI.wait()
    if player.hp > player.maxhp:
        player.hp = player.maxhp
def strengthen(player, enemy):
    player.attack = player.attack + 2
    UI.clear()
    print((player.name + " grew stronger!\n\nAttack + 2"))
    UI.wait()
def bellow(player, enemy):
    player.attack = player.attack + 3
    UI.clear()
    print((player.name + " ROARED!!\n\nAttack + 3"))
    UI.wait()
def timeLoopE(player,enemy):
    player.timeLoop += 3
    UI.clear()
    print((enemy.name + " put " + player.name + " in a time loop for 2 turns!"))
    UI.wait()
def useAbility(ability, player, enemy):
    abilityLib = {
        "Shred": shred,
        "Heal": heal,
        "Strengthen": strengthen,
        "Double Eviscerate": doubleeviscerate,
        "Rejuvinate": rejuvinate,
        "Bellow": bellow
    }
    abilityLib.get(ability)(player, enemy)
    player.abilityUsed = True
    player.lastAbilityUsed[0] = ability
    player.AP -= 1
def getAbilities(player, enemy):
    if len(player.abilities) < 1:
        UI.clear()
        print ("No Abilities")
        UI.wait()
        return
    choice = ""
    options = []
    for x in range(1,(len(player.abilities)+2)):
        options.append(str(x))
    while (choice not in options):
        UI.clear()
        n = 1
        for x in player.abilities:
            print((str(n) + ") " + x))
            n = n + 1
        print((str(n) + ") " + "Return"))
        choice = input()
    if int(choice) == len(player.abilities) + 1:
        return
    if player.AP < 1:
        UI.clear()
        print("No ability points left")
        UI.wait()
        return
    else:
        #player.abilityUses[int(choice)-1] = player.abilityUses[int(choice)-1] - 1 THIS IS FOR SUBTRACTING A USE FROM INDIVIDUAL ABILITIES
        useAbility(player.abilities[int(choice)-1], player, enemy)

def resethp(player, enemy):
    player.hp = player.maxhp
    enemy.hp = enemy.maxhp
def resetdefense(player, enemy):
    player.defense = player.maxdefense
    enemy.defense = enemy.maxdefense
def resetattack(player, enemy):
    player.attack = player.maxattack
    enemy.attack = enemy.maxattack

UI.clear()
initialize_game()


#CHAPTER 1
UI.clear()
print((SaveOne.name + " breaks from of his egg to breathe his first breath."))
UI.wait()
UI.clear()
print("The hands of fate have other plans, however...")
UI.wait()
UI.clear()
print("A rat seeks to claim your newfound mortality.")
UI.wait()
Rat = Character.Enemy("Rat",25,3,1,[3,4,9,12],[],[],None,["no loot"])
Combat.battle(SaveOne, Rat)

def abilityUpgrade(player,abilities,enemy):
    response = 0
    responseBank = []
    n = 1
    while response not in responseBank:
        for ability in abilities:
            responseBank.append(str(n))
            print(enemy.name + " defeated! Choose an ability!")
            print("\n" + n + ")" + enemy.loot[n] + "\n" + ability.name + " - " + ability.description)
            n += 1
            continue
        response = input()
        UI.clear()
    player.abilities.append(abilities[int(response)-1])
UI.clear()



#Chapter 2
UI.clear()
print("A wild Pig appears!")
UI.wait()
pigSTurns = [2,7,8,10,12,16,20]
pigGTurns = []
Pig = ClassFile.Enemy("Pig",35,4,1,pigSTurns,pigGTurns,[],None,["no loot"])
battle(SaveOne, Pig)

def levelUp(player,hp,attack,defense,AP):
    print("Pig Defeated! Level Up!")
    input()
    player.maxhp += hp
    player.hp = player.maxhp
    print("HP + " + str(hp))
    input()
    player.maxattack += attack
    player.attack = player.maxattack
    print("Attack + " + str(attack))
    input()
    player.maxdefense += defense
    player.defense = player.maxdefense
    print("Defense + " + str(defense))
    input()
    player.maxAP += AP
    player.AP = player.maxAP
    print("Max AP + " + str(AP))
UI.clear()
levelUp(SaveOne,20,4,1,1)
UI.wait()

#Chapter 3

orcSTurns = [2,7,13,15,16,17]
orcGTurns = [3,4,8,9,14]
Orc = ClassFile.enemy("Young Orc",40,9,3,orcSTurns,orcGTurns,[],None,["no loot"])
battle(SaveOne, Orc)


def secondUpgrade(player):
    response = 0
    responseBank = ["1","2","3"]
    while response not in responseBank:
        print("Orc defeated! Choose an Ability or Upgrade!")
        
        if "Shred" in player.abilities:
            description = ("Double Eviscerate - Increase enemy's bleed level by 2.")
        else:
            description = ("Shred - Increase enemy's bleed level by 1. Each level deals 2 damage per turn.")
        print(("\n1)Equip Orc's Sword\n%s" % description))
        
        if "Heal" in player.abilities:
            description = ("Rejuvinate - Heal all HP")
        else:
            description = ("Heal - Restore 70% of max HP.")
        print(("\n2)Absorbs Orc's soul\n%s" % description))
        
        if "Strengthen" in player.abilities:
            description = ("Bellow - Buff attack by 3 until end of battle.")
        else:
            description = ("Strengthen - Buff attack by 2 until end of battle.")
        print(("\n3)Feel the Orc's rage\n%s" % description))
        response = input()
        if response == "1":
            if "Shred" in player.abilities:
                player.abilities[(player.abilities.index("Shred"))] = "Double Eviscerate"
            else:
                player.abilities.append("Shred")
        elif response == "2":
            if "Heal" in SaveOne.abilities:
                player.abilities[player.abilities.index("Heal")] = "Rejuvinate"
            else:
                player.abilities.append("Heal")
        elif response == "3":
            if "Strengthen" in player.abilities:
                player.abilities[player.abilities.index("Strengthen")] = "Bellow"
            else:
                player.abilities.append("Strengthen")
        UI.clear()
        continue
UI.clear()
secondUpgrade(SaveOne)
#Chapter 4
slothSTurns = [6,15,18,23,26,30,35,38,41,42,43,44,45]
slothGTurns = [4,5,9,14,16,20,21,24,25,31,32,33,34,36,37]
slothDTurns = [1,2,3,7,8,10,11,12,13,17,19,22,27,28,29,39,40]
SavageSloth = ClassFile.enemy("Savage Sloth", 100, 10, 1,
slothSTurns, slothGTurns, slothDTurns,"Shred",["no loot"])
battle(SaveOne, SavageSloth)
UI.clear()

levelUp(SaveOne,55,3,2,1)

mageSTurns = []
for x in range(1,100,5):
    mageSTurns.append(x)
    mageSTurns.append(x+1)
mageGTurns = []
for x in range(3,100,5):
    mageGTurns.append(x)
    mageGTurns.append(x+1)
mageDTurns = []
for x in range(5,100,5):
    mageDTurns.append(x)
mageEffect = True
temporalMage = ClassFile.enemy("Temporal Mage",191,13,2,
mageSTurns, mageGTurns, mageDTurns, "Time Loop", ["no loot"])
UI.wait()
battle(SaveOne, temporalMage)

UI.clear()
print((SaveOne.name + " defeated " + temporalMage.name + "!"))
UI.wait()

UI.clear()
print("Temporal mage class unlocked!!")
UI.wait()

UI.clear()
print("But not yet...\nComing soon!")
UI.wait() 
