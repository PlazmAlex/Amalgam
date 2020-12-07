import UIModule
import AbilityModule
import sys
import time
#mage effect is a bad implementation.
#Need to create a class that handles turn based events independent of enemy
mageEffect = False

#This subtracts health points from the defender according to various battle data including attack power 
#and defense
def dealDamage(attacker, defender):
    critical = ""
    devastate = ""
    if defender.guard == True:
        UIModule.clear()
        print((defender.name + " guarded!\n"))
        defense = defender.defense * 3
        UIModule.wait()
    else:
        defense = defender.defense
    damage = attacker.attack - defense
    if attacker.superAttack == True:
        damage = damage * 3
        devastate = (UIModule.color.red + "!!Devastating Attack!!\n\n" + UIModule.color.endColor)
        attacker.superAttack = False
    elif defender.vulnerable == True:
        damage = damage * 2
        critical = (UIModule.color.blue + "!!!Critical Strike!!!\n\n" + UIModule.color.endColor)
    if damage <= 0:
        damage = 1
    defender.hp = defender.hp - damage
    UIModule.clear()
    print((critical + devastate + attacker.name + " dealt " + str(damage) + " damage to " + defender.name + "!"))
    UIModule.wait()
    if defender.hp < 0:
        defender.hp = 0
        
#this handles the main battle loop by calling functions based on player input and enemy intent
def battle(player, enemy):
    turn = 1
    enemyBleed = ""
    playerBleed = ""
    while enemy.hp > 0 and player.hp > 0:
        UIModule.clear()
        #Display info
        print(("Turn: " + str(turn)))
        if mageEffect == True:
            if turn in range(1,100,2):
                print(("\n!!!!" + enemy.name + " prevents abilities on odd turns!!!!\n"))
                player.canUseAbilities = False
        turnCheck(turn, enemy, player)
        #-------------------

        #Time Loop Check
        #if player.timeLoop == 0:  
         
        print("\n" + UIModule.color.lightBlue + player.name + "'s HP (" + str(player.hp) + "/" + str(player.maxhp) +
        ")  Ability Points (" + str(player.AP) + "/" + str(player.maxAP) + ") " + UIModule.color.endColor +
         UIModule.color.red + playerBleed + UIModule.color.endColor +
        "\n\n" + enemy.name + "'s HP (" + str(enemy.hp) + "/" + str(enemy.maxhp) +
         ")" + UIModule.color.red + enemyBleed + UIModule.color.endColor +
        "\n")
        n = 1
        print("[Enter number to select battle option]\n")
        if player.timeLoop == 1:
            player.currentOptions = player.lastAction
        for x in player.currentOptions:
            print((str(n) + ") " + x))
            n += 1
        if player.timeLoop == 1:
            if input() == "1":
                choice = "1"
                pass
            else:
                continue
        else:
            choice = input()
        #-------------
        #Menu Choice
        if choice in [str(x) for x in range (1, len(player.currentOptions) + 1)]:
            if applyMenuChoice(player, enemy, choice) == 0:
                continue
        else:
            continue
        #--------------
        #Enemy Action
        if enemy.hp > 0 and enemy.guard == False and enemy.debuff == False:
            dealDamage(enemy, player)
        elif enemy.debuff == True and enemy.hp > 0:
            AbilityModule.useAbility(enemy.ability,enemy, player)
        #------------
        #End of Turn effects
        if len(player.statDuration) > 0:
            applyDurationDecay(player)
        if len(enemy.statDuration) > 0:
            applyDurationDecay(enemy)
        if player.timeLoop > 0:
            UIModule.clear()
            print(player.name + " is stuck in a time loop!")
            UIModule.wait()
        player.canUseAbilities = True
        player.guard = False
        enemy.guard = False
        enemy.vulnerable = False
        enemy.debuff = False
        playerBleed = ""
        enemyBleed = ""
        player.currentOptions = player.battleOptions
        if (player.bleed > 0) and (enemy.hp > 0):   
            playerBleed = (" BLEED(" + str(player.bleed) + ")")
            applyBleed(player)
        if enemy.bleed > 0:
            enemyBleed = (" BLEED(" + str(enemy.bleed) + ")")
            applyBleed(enemy)
        #-------------
        turn += 1
    player.lastAction = [""]
    player.lastAbilityUsed = [""]
    player.bleed = 0
    player.attack = player.maxattack
    player.defense = player.maxdefense
    player.AP = player.maxAP
    if player.hp > 0:
        player.hp = player.maxhp
        UIModule.clear()
        print((player.name + " survived!"))
        UIModule.wait()
    else:
        UIModule.clear()
        print((player.name + " died!"))#Need lose function
        UIModule.wait()
        UIModule.clear()
        

#This checks what the enemy will do by checking the turn counter vs it's lists of actions
#It then displays text to the player about what the enemy will do while getting the enemy
#ready to perform it
def turnCheck(turn, enemy, player):
    guardText = (UIModule.color.blue + " (Blockable)" + UIModule.color.endColor 
    + UIModule.color.yellow) if enemy.ability.guardable == True else ""
    intentWarnings = {
        "superAttack" : "unleash a devastating attack",
        "guard" : "guard itself",
        "debuff" : "use " + enemy.ability.name + guardText
        }
    vulnerableText = ""
    normalTurn = True
    turnLists = ["superTurn", "guardTurn", "debuffTurn"]
    battleIntents = ["superAttack", "guard",  "debuff"]
    for index,list in enumerate(turnLists, 0):
        if turn in getattr(enemy, list):
            intent = battleIntents[index]
            if intent == "superAttack" or intent == "debuff":
                #Think of a better way to tie vulnerability to these intentions
                enemy.vulnerable = True
                vulnerableText = "\n!!It looks vulnerable to attacks!!\n"
            setattr(enemy, intent, True)
            normalTurn = False
            print(UIModule.color.yellow + "\n!!" + enemy.name + " is going to " + intentWarnings[intent] + "!!\n" +
            vulnerableText + UIModule.color.endColor)
    if normalTurn == True:
        print("\n!" + enemy.name + " is going to attack!\n")


#This checks if the player can use abilities then displays them.It also handles situations where
#abilities cannot be selected
def getAbilities(player, enemy):
    if player.timeLoop != 0:
        player.AP += 1
        AbilityModule.useAbility(player.lastAbilityUsed[0], player, enemy)
        player.canUseAbilities = True
    if player.canUseAbilities == False:
        UIModule.clear()
        print((player.name + " cannot use abilites right now."))
        UIModule.wait()
        return 0
    if player.timeLoop == 0:
        AbilityModule.displayAbilities(player, enemy)
    if player.abilityUsed == False:
        return 0
    player.abilityUsed = False

def guard(player, enemy):
    player.guard = True

#This takes the player input on the battle menu and executes a function associated with
#the selected option
#it returns 0 if the player's selection did nothing, allowing them to repeat the choice
def applyMenuChoice(player, enemy, choice):
    if menuOptions[player.currentOptions[int(choice) - 1]](player, enemy) == 0:
        return 0
    else:
        player.lastAction[0] = player.currentOptions[int(choice) - 1]
menuOptions = {
        "Attack" : dealDamage,
        "Abilities" :  getAbilities,
        "Guard" : guard
    } 

def applyDurationDecay(character):
    for index in range(0,len(character.statDuration)):
        character.statDuration[index] -= 1
        if character.statDuration[index] == 0:
            #this reverses the stat change whose duration just ended
            setattr(character, character.statEffects[index], getattr(character,
            character.statEffects[index]) - character.statChanges[index])
            character.statDuration[index] = False
            character.statEffects[index] = False
            character.statChanges[index] = False
    #This removes all the leftover data from the ability since it's duration has ended
    filter(None, character.statEffects)
    filter(None, character.statDuration)
    filter(None, character.statChanges)

def applyBleed(character):
    character.hp -= character.bleed
    UIModule.clear()
    print(character.name + " is bleeding!") 
    input()
    print("It loses " + str(character.bleed) + " health!")
    UIModule.wait()
    if character.hp <= 0:
        UIModule.clear()
        print((character.name + " bled out!"))
        UIModule.wait()

def retry(player):
    while(True):
        UIModule.clear()
        print("Retry last battle?")
        print("\n1) Yes")
        print("\n2) Give Up")
        choice = input()
        if choice  == "1":
            player.hp = player.maxhp
            return True
        if choice  == "2":
            return False
        else:
            continue