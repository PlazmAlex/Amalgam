import operator
import UIModule
class Ability:
    def __init__(self, name, effect, modifier, magnitude, duration, guardable, target, flavor,description):
        self.name = name
        self.effect = effect        
        self.modifier = modifier
        self.magnitude = magnitude
        self.duration = duration
        self.guardable = guardable
        self.target = target
        self.description = description
        self.flavor = flavor

    #timeLoop = Ability("Time Loop")

def useAbility(ability, user, opponent):
    target = user if ability.target == "user" else opponent 
    if ability.guardable and target.guard:
        UIModule.clear()
        print(target.name + " guarded the ability!")
        user.abilityUsed = True
        user.lastAbilityUsed[0] = ability
        user.AP -= 1
        UIModule.wait()
        return   
    #Pull information from ability object
    statName = ability.effect
    targetStat = (getattr(target, ability.effect))
    newStat = operators[ability.modifier](targetStat, ability.magnitude)
    statChange = newStat - targetStat
    #---
    UIModule.wait
    #Healing detour
    #needed to alter how healing is handled since it's calculated based on max value first
    if ability.effect == "maxhp":
        print("hp bug")
        UIModule.wait()
        targetStat = target.hp
        statName = "hp"
        #Prevent healing above maxHP
        if target.hp + newStat > target.maxhp:
            statChange = target.hp + newStat - target.maxhp
        else:
            statChange = newStat 
    else: 
        #Display changes 
        targetStat += statChange
        UIModule.clear
        #WHY IS THIS NOT PRINTING
        print(user.name + ability.flavor)
        UIModule.wait
        UIModule.clear
        print(statName.title() + " + " + str(statChange))
        UIModule.wait
        if ability.duration != None:
            #Track ability effects in character class
            target.statEffects.append(statName)
            target.statChanges.append(statChange)
            target.statDuration.append(ability.duration)
    user.abilityUsed = True
    user.lastAbilityUsed[0] = ability
    user.AP -= 1

operators = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.floordiv
    }

def displayAbilities(player, enemy):
    if len(player.abilities) < 1:
        UIModule.clear()
        print ("No Abilities")
        UIModule.wait()
        return
    choice = ""
    options = []
    for x in range(1,(len(player.abilities)+2)):
        options.append(str(x))
    while (choice not in options):
        UIModule.clear()
        n = 1
        for x in player.abilities:
            print((str(n) + ") " + x.name))
            n = n + 1
        print((str(n) + ") " + "Return"))
        choice = input()
    if int(choice) == len(player.abilities) + 1:
        return
    if player.AP < 1:
        UIModule.clear()
        print("No ability points left")
        UIModule.wait()
        return
    else:
        print("calling useAbility")
        useAbility(player.abilities[int(choice)-1], player, enemy)

def abilityUpgrade(player,abilities,enemy):
    response = 0
    responseBank = []
    n = 1
    while response not in responseBank:
        for ability in abilities:
            responseBank.append(str(n))
            print(enemy.name + " defeated! Choose an ability!")
            print("\n" + str(n) + ")" + enemy.loot[n] + "\n" + ability.name + " - " + ability.description)
            n += 1
            continue
        response = input()
        UIModule.clear()
    player.abilities.append(abilities[int(response)-1])
UIModule.clear()