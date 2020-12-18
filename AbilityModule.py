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
default = Ability("None", "attack", "-", 0, None, False, "user",
" this text should never appear", "This enemy has no abilities")
shred = Ability("Shred","bleed", "+", 2, None, True, "opponent",
" has been shredded!","Increase enemy's bleed by 2. Each bleed deals 1 damage per turn.")
Eviscerate = Ability("Eviscerate", "bleed", "+", 4, None, True, "opponent",
" has been torn apart!","Increase enemy's bleed by 4. Each bleed deals 1 damage per turn.")
disembowel = Ability("Disembowel", "bleed", "+", 5, None, True, "opponent",
" has been gutted!", "Increase enemy's bleed by 5. Each bleed deals 1 damage per turn." )
heal = Ability("Heal", "hp", "+", 15, None, False, "user",
" healed!", "Restore 15 HP.")
rejuvinate = Ability("Rejuvinate", "hp", "+", 30, None, False, "user",
" feels rejuvinated!", "Restore 30 HP.")
revitalize = Ability("Revitalize", "hp", "+", 45, None, False, "user",
" has been revitalized!", "Restore 45 HP.")
strengthen = Ability("Strengthen", "attack", "+", 2, None, False, "user",
" grew stronger!", "Increase your attack power by 2 until end of battle.")
bellow = Ability("Bellow", "attack", "+", 3, None, False, "user",
" ROARED!", "Increase your attack power by 3 until end of battle.")
rage = Ability("Rage", "attack", "+", 5, None, False, "user",
" is seething with power!", "Increase your attack power by 4 until end of battle.")
timeLoop = Ability("Time Loop", "timeLoop", "+", 1, 3, False, "opponent", 
" was put in a time loop!\n\nIt must repeat its last action!",
"Opponent must repeat action used this turn 2 more times!")
weaken = Ability("Weaken", "attack", "-", 4, 3, True, "opponent",
" was weakend for two turns", "Lower opponent's attack power by 4 for two turns." )
shriek = Ability("Shriek", "defense", "-", 2, 3, True, "opponent",
" is trembling for two turns", "Lower opponent's defense by 2 for two turns." )
enrage = Ability("Enrage", "enrage", "+", 1, 3, True, "opponent", " became enraged for two turns!",
"Opponent can only attack for the next 2 turns")

def getAbility(player, ability, enemy):
    UIModule.clear()
    print(enemy.name + " defeated!")
    input()
    print(player.name + " learned how to use the " + ability.name + " ability!")
    input()
    print("(" + ability.name + ") - " + ability.description)
    UIModule.wait()
    player.abilities.append(ability)
    player.allAbilities.append(ability)
    UIModule.clear()

def useAbility(ability, user, opponent):
    target = user if ability.target == "user" else opponent
    if ability.guardable and target.guard:
        UIModule.clear()
        print(target.name + " guarded itself from " + ability.name + "!")
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
    if ability.effect == "hp":
        targetStat = target.hp
        #Prevent healing above maxHP
        if target.hp + ability.magnitude > target.maxhp:
            statChange = (target.maxhp - target.hp)
        else:
            statChange = ability.magnitude
    #Display and implement effects 
    setattr(target, statName, targetStat + statChange)
    UIModule.clear()
    print(user.name + " used " + ability.name)
    input()
    print(target.name + ability.flavor)
    modifier = " + " if statChange >= 0 else " "
    print(statName.title() + modifier + str(statChange))
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
        print(UIModule.color.lightBlue + (str(n) + ") " + "Back") + UIModule.color.endColor)
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
        print(enemy.name + " defeated! Choose one ability to get!")
        for index,ability in enumerate(abilitiesList):
            oldAbility = ""
            hasAbility = "Gain"
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
                hasAbility = "Upgrade"
                oldAbility = ability.name + " -> "
                ability = abilityPlus(ability)
            if noDuplicate == False:
                break
            responseBank.append(str(n))
            print("\n" + str(n) + ") " + hasAbility + " ability (" + oldAbility 
            + ability.name + ")\nUse to " + ability.description)
            n += 1
        if noDuplicate == False:
            #delete the ability from the list and start again
            del abilitiesList[abilityDuplicate]
            continue
        response = input()
        UIModule.clear()
    choice = abilities[int(response)-1]
    if choice not in player.allAbilities:
        #if the player does not have the chosen ability
        player.abilities.append(choice)
        player.allAbilities.append(choice)
        return
        #if the player already has the chosen ability  
    while choice in player.allAbilities:
        if choice in player.abilities:
            index = player.abilities.index(choice)
        choice = abilityPlus(choice)
    player.abilities[index] = choice
    player.allAbilities.append(choice)

    
UIModule.clear()

abilityLevelUp = {
    strengthen : bellow,
    bellow : rage,
    shred : Eviscerate,
    Eviscerate : disembowel,
    heal : rejuvinate,
    rejuvinate : revitalize
}
def abilityPlus(ability):
    return abilityLevelUp.get(ability, ability)