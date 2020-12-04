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

shred = Ability("Shred","bleed", "+", 2, None, True, "opponent",
" has been shredded!","Increase enemy's bleed by 2. Each bleed deals 1 damage per turn.")
Eviscerate = Ability("Eviscerate", "bleed", "+", 4, None, True, "opponent",
" has been torn apart!","Increase enemy's bleed by 4. Each bleed deals 1 damage per turn.")
heal = Ability("Heal", "maxhp", "*", .7, None, False, "user",
" healed!", "Restore 70% of your max HP.")
rejuvinate = Ability("Rejuvinate", "maxhp", "*", 1, None, False, "user",
" feels rejuvinated!", "Restore all of your HP")
strengthen = Ability("Strengthen", "attack", "+", 2, None, False, "user",
" grew stronger!", "Increase your attack power by 2 until end of battle")
bellow = Ability("Bellow", "attack", "+", 3, None, False, "user",
" ROARED!", "Increase your attack power by 3 until end of battle.")
timeLoop = Ability("Time Loop", "timeLoop", "+", 1, 3, False, "opponent", 
" was put in a time loop!\n\nIt must repeat its last action!",
"Opponent must repeat action used this turn 2 more times!")

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
    targetStat = getattr(target, statName)
    newStat = int(operators[ability.modifier](targetStat, ability.magnitude))
    statChange = newStat - targetStat
    #---
    #Healing detour
    #needed to alter how healing is handled since it's calculated based on max value first
    if ability.effect == "maxhp":
        statName = "hp"
        targetStat = target.hp
        #Prevent healing above maxHP
        if target.hp + newStat > target.maxhp:
            statChange = (target.maxhp - target.hp)
        else:
            statChange = newStat 
    #Display and implement effects 
    setattr(target, statName, targetStat + statChange)
    UIModule.clear()
    print(target.name + ability.flavor)
    print(statName.title() + " + " + str(statChange))
    UIModule.wait()
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
            print(str(n) + ") " + x.name + "\n   -" + x.description + "\n")
            n = n + 1
        print(UIModule.color.blue + (str(n) + ") " + "Back") + UIModule.color.endColor)
        choice = input()
    if int(choice) == len(player.abilities) + 1:
        return 0
    if player.AP < 1:
        UIModule.clear()
        print("No ability points left")
        UIModule.wait()
        return 0
    else:
        useAbility(player.abilities[int(choice)-1], player, enemy)

def abilityUpgrade(player,abilities,enemy):
    #Lots of convolution happening here, let's break it down
    #if all abilities have never been acquired before, everything goes as normal
    #but if an ability has been gotten before, it needs to upgrade to a better version
    #it then check if the player alreday has that upgraded ability
    #if so this repeats until there is no more upgrades
    #at that point the ability is no longer presented as an option
    abilitiesList = abilities
    response = 0
    responseBank = []
    while response not in responseBank:
        UIModule.clear()
        n = 1
        print(enemy.name + " defeated! Choose an ability to gain!")
        for index,ability in enumerate(abilitiesList):
            noDuplicate = True
            abilityDuplicate = None
            while ability in player.allAbilities:
                #if the player already has the given ability
                if ability == abilityPlus(ability):
                    #if the ability cannot be upgraded anymore
                    noDuplicate = False
                    abilityDuplicate = index
                    break
                #upgrade the ability
                ability = abilityPlus(ability)
            if noDuplicate == False:
                break
            responseBank.append(str(n))
            print("\n" + str(n) + ") " + "Gain ability (" + ability.name + ")\nUse to " + ability.description)
            n += 1
        if noDuplicate == False:
            #delete the ability from the list and start again
            del abilitiesList[abilityDuplicate]
            continue
        response = input()
        UIModule.clear()
    choice = abilitiesList[int(response)-1]
    if choice not in player.abilities:
        #if the player does not have the chosen ability
        player.abilities.append(choice)
        player.allAbilities.append(choice)
    while choice in player.abilities:
        #if the player already has the chosen ability
        player.abilities[player.abilities.index(choice)] = abilityPlus(choice)
        #upgrade the ability and replace the old one
        player.allAbilities.append(abilityPlus(choice))
        choice = abilityPlus(choice)
        if choice == abilityPlus(choice):
            #if the ability cannot be upgraded anymore
            break
UIModule.clear()

abilityLevelUp = {
    strengthen : bellow,
    shred : Eviscerate,
    heal : rejuvinate
}
def abilityPlus(ability):
    return abilityLevelUp.get(ability, ability)