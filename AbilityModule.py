import operator
import UIModule
class Ability:
    def __init__(self, name, effect, modifier, magnitude, duration, guardable, target, flavor):
        self.name = name
        self.effect = effect        
        self.modifiers = modifiers
        self.magnitude = magnitude
        self.duration = duration
        self.guardable = guardable
        self.target = target

def instantiateAbilities():
    shred = Ability("Shred","bleedLevel", "+", 1, None, True, "opponent", " has been shredded!")
    Ability.abilities.append(shred)
    doubleEviscerate = Ability("Double Eviscerate", "bleedLevel", "+", 2, None, True, "opponent", " has been torn apart!")
    Ability.abilities.append(doubleEviscerate)
    heal = Ability("Heal", "maxhp", "*", .7, None, False, "user", " healed!")
    Ability.abilities.append(heal)
    rejuvinate = Ability("Rejuvinate", "maxhp", "*", 1, None, False, "user", " feels rejuvinated!")
    Ability.abilities.append(rejuvinate)
    strengthen = Ability("Strengthen", "attack", "+", 2, None, False, "user", " grew stronger!")
    Ability.abilities.append(strengthen)
    bellow = Ability("Bellow", "attack", "+", 3, None, False, "user", " ROARED!")
    Ability.abilities.append(bellow)
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
    newStat = modifiers[ability.modifier](targetStat, ability.magnitude)
    statChange = newStat - targetStat
    #---

    #Healing detour
    #needed to alter how healing is handled since it's calculated based on max value first
    if ability.effect == "maxhp":
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
        print(user.name + ability.flavor)
        UIModule.wait
        UIModule.clear
        print(statName.Title() + " + " + statChange)
        UIModule.wait
        if ability.duration != None:
            #Track ability effects in character class
            target.statEffects.append(statName)
            target.statChanges.append(statChange)
            target.statDuration.append(ability.duration)
    user.abilityUsed = True
    user.lastAbilityUsed[0] = ability
    user.AP -= 1

modifiers = {
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
            print((str(n) + ") " + x))
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
        useAbility(player.abilities[int(choice)-1], player, enemy)