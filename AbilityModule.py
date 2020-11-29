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
    doubleEviscerate = Ability("Double Eviscerate", "bleedLevel", "+", 2, None, True, "opponent", " has been torn apart!")
    heal = Ability("Heal", "maxhp", "*", .7, None, False, "user", " healed!")
    rejuvinate = Ability("Rejuvinate", "maxhp", "*", 1, None, False, "user", " feels rejuvinated!")
    strengthen = Ability("Strengthen", "attack", "+", 2, None, False, "user", " grew stronger!")  
    bellow = Ability("Bellow", "attack", "+", 3, None, False, "user", " ROARED!")
    #timeLoop = Ability("Time Loop")

def useAbility(ability, user, opponent):
    target = user if ability.target == "user" else opponent 
    if ability.guardable and target.guard:
        UIModule.clear()
        print(target.name + " guarded the ability!")
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

modifiers = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.floordiv
    }