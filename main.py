import os
import CharacterModule
import CombatModule
import AbilityModule
import UIModule
import sys

print("*********\n*Amalgam*\n*********")
UIModule.wait()
def levelUp(player, enemy, hp,attack,defense,AP):
    UIModule.clear()
    print(enemy.name + " defeated! Level Up!")
    input()
    if hp > 0:
        player.maxhp += hp
        player.hp = player.maxhp
        print("Max Health Points + " + str(hp))
        input()
    if attack > 0:
        player.maxattack += attack
        player.attack = player.maxattack
        print("Attack + " + str(attack))
        input()
    if defense > 0: 
        player.maxdefense += defense
        player.defense = player.maxdefense
        print("Defense + " + str(defense))
        input()
    if AP > 0:
        player.maxAP += AP
        player.AP = player.maxAP
        print("Max Ability Points + " + str(AP))
    UIModule.wait()
    UIModule.clear()

def initialize_game():
    UIModule.clear()
    response = input("[Enter number to select menu option]\n\n1) New Run\n2) Class\n")
    
    if response == "2":
        print("No other classes unlocked")
        UIModule.wait()
        initialize_game()
        
    elif response == "1": 
        global SaveOne
        name = ""
        n = 1
        while (len(name) > 15 or len(name) < 1):
            UIModule.clear()
            if n < 2:
                limit = ""
            else:
                limit = "(15 Character limit)"
            name = input("Please name your Amalgam %s\n" % limit)
            n += 1
        UIModule.clear()
        SaveOne = CharacterModule.SaveFile(name)
        print(("Alright " + SaveOne.name + ", time to begin your adventure."))
        UIModule.wait()
    else:
        initialize_game()

UIModule.clear()
initialize_game()


#Chapter 1
"""
UIModule.clear()
print((SaveOne.name + " breaks from of his egg to breathe his first breath."))
UIModule.wait()
UIModule.clear()
print("The hands of fate have other plans, however...")
UIModule.wait()
UIModule.clear()
print("A rat seeks to claim your newfound mortality.")
UIModule.wait()
"""
Rat = CharacterModule.Enemy("Rat", 25, 3, 1,
[3,4,9,12,15], [], [], AbilityModule.default)
#CombatModule.battle(SaveOne, Rat)

levelUp(SaveOne, Rat, 5,1,0,0)

#Chapter Wolf
wolfSTurns = [4, 6, 12]
wolfDTurns = [2, 5, 8, 10, 11]
Wolf = CharacterModule.Enemy("Dire Wolf", 35, 1, 2,
wolfSTurns, [], wolfDTurns, AbilityModule.strengthen)
#CombatModule.battle(SaveOne, Wolf)
AbilityModule.getAbility(SaveOne, AbilityModule.strengthen, Wolf)

levelUp(SaveOne, Wolf, 5,1,0,1)

#Chapter Cat
#This chaper may need to be made easier
Cat = CharacterModule.Enemy("Feral Cat", 40, 4, 2,
[3, 14, 17], [], [2, 5, 8, 9, 11, 12], AbilityModule.shred)
#CombatModule.battle(SaveOne, Cat)
AbilityModule.getAbility(SaveOne, AbilityModule.shred, Cat)

levelUp(SaveOne, Cat, 5,1,0,1)


#Chapter Lazy pig
pigSTurns = []
pigGTurns = []
Pig = CharacterModule.Enemy("Pig",50,3,1,
pigSTurns,pigGTurns, [5, 10, 15, 20], AbilityModule.heal)
#CombatModule.battle(SaveOne, Pig)
AbilityModule.getAbility(SaveOne, AbilityModule.heal, Pig)

levelUp(SaveOne, Pig, 10,1,1,1)

#Chapter Orc 
orcSTurns = [2,7,13,15,16,20,23,24,28,29,30]
orcGTurns = [3,4,8,9,14,17,19,21,25]
Orc = CharacterModule.Enemy("Young Orc",50,9,3,
orcSTurns,orcGTurns,[],AbilityModule.default)
#CombatModule.battle(SaveOne, Orc)

AbilityModule.abilityUpgrade(SaveOne, [AbilityModule.shred, AbilityModule.heal, AbilityModule.strengthen], Orc)

#Chapter Sloth
slothSTurns = [6,15,18,23,26,30,35,38,41,42,43,44,45]
slothGTurns = [4,5,9,14,16,20,21,24,25,31,32,33,34,36,37]
slothDTurns = [1,2,3,7,8,10,11,12,13,17,19,22,27,28,29,39,40]
SavageSloth = CharacterModule.Enemy("Savage Sloth", 100, 10, 1,
slothSTurns, slothGTurns, slothDTurns,AbilityModule.shred)
#CombatModule.battle(SaveOne, SavageSloth)
levelUp(SaveOne, SavageSloth, 25,2,1,1)

paladinSTurns = []
paladinGTurns = []
paladinDTurns = []
Paladin =  CharacterModule.Enemy("Paladin", 90, 12, 3,
paladinSTurns, paladinGTurns, paladinDTurns, AbilityModule.heal)
AbilityModule.abilityUpgrade(SaveOne, [AbilityModule.shred, AbilityModule.heal, AbilityModule.strengthen], Paladin)

ogreSTurns = []
ogreGTurns = []
ogreDTurns = []
Ogre =CharacterModule.Enemy("Giant Ogre", 150, 15, 2,
ogreSTurns, ogreDTurns, ogreDTurns, AbilityModule.strengthen)
levelUp(SaveOne, Ogre, 30,2,1,0)

"""
tortoiseSTurns = []
tortoiseGTurns = []
tortoiseDTurns = []
Tortoise = CharacterModule.Enemy("Continental Tortoise")
"""
#Chapter Mage
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
CombatModule.mageEffect = True
temporalMage = CharacterModule.Enemy("Temporal Mage",191,13,2,
mageSTurns, mageGTurns, mageDTurns, AbilityModule.timeLoop)
UIModule.wait()
CombatModule.battle(SaveOne, temporalMage)

UIModule.clear()
print((SaveOne.name + " defeated " + temporalMage.name + "!"))
UIModule.wait()

UIModule.clear()
print("Temporal mage class unlocked!!")
UIModule.wait()

UIModule.clear()
print("But not yet...\nComing soon!")
UIModule.wait() 