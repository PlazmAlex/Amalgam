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

shred = Ability("Shred","bleed", "+", 1, None, True, "opponent",
" has been shredded!","Increase enemy's bleed by 2. Each bleed deals 1 damage per turn.")
Eviscerate = Ability("Eviscerate", "bleed", "+", 2, None, True, "opponent",
" has been torn apart!","Increase enemy's bleed by 4. Each bleed deals 1 damage per turn.")
heal = Ability("Heal", "maxhp", "*", .7, None, False, "user",
" healed!", "Restore 70% of your max HP.")
rejuvinate = Ability("Rejuvinate", "maxhp", "*", 1, None, False, "user",
" feels rejuvinated!", "Heal all your HP")
strengthen = Ability("Strengthen", "attack", "+", 2, None, False, "user",
" grew stronger!", "Increase your attack power by 2 until end of battle")
bellow = Ability("Bellow", "attack", "+", 3, None, False, "user",
" ROARED!", "Increase your attack power by 3 until end of battle.")

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
        return
    if player.AP < 1:
        UIModule.clear()
        print("No ability points left")
        UIModule.wait()
        return
    else:
        useAbility(player.abilities[int(choice)-1], player, enemy)

def abilityUpgrade(player,abilities,enemy):
    response = 0
    responseBank = []
    while response not in responseBank:
        n = 1
        print(enemy.name + " defeated! Choose an ability!")
        for ability in abilities:
            if ability in player.abilities:
                ability = abilityPlus(ability)
            responseBank.append(str(n))
            print("\n" + str(n) + ") " + enemy.loot[n-1] + ":\n Gain ability (" + ability.name + ")\n-Use to " + ability.description)
            n += 1
        response = input()
        UIModule.clear()
    choice = abilities[int(response)-1]
    if choice in player.abilities:
        player.abilities[player.abilities.index(choice)] = abilityPlus(choice)
    else:
        player.abilities.append(choice)
UIModule.clear()

abilityLevelUp = {
    shred : Eviscerate,
    heal : rejuvinate,
    strengthen : bellow
}
def abilityPlus(ability):
    return abilityLevelUp.get(ability, ability)