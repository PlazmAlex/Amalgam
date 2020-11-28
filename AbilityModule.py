import operator
class Ability:
    def __init__(self, name, effect, modifier, magnitude, duration, gaurdable, target):
        self.name = name
        self.effects = effects
        self.modifiers = modifiers
        self.magnitude = magnitude
        self.duration = duration
        self.gaurdable = gaurdable
        self.target = target
    
def instantiateAbilities():
    shred = Ability("Shred","bleedLevel", "+", 1, None, True, "opponent")
    doubleEviscerate = Ability("Double Eviscerate", "bleedLevel", "+", 2, None, True, "opponent")
    heal = Ability("Heal", "maxhp", "*", .7, None, False, "user")
    rejuvinate = Ability("Rejuvinate", "maxhp", "*", 1, None, False, "user")
    strengthen = Ability("Strengthen", "attack", "+", 2, None, False, "user")  
    bellow = Ability("Bellow", "attack", "+", 3, None, False, "user")
    #timeLoop = Ability("Time Loop")

def useAbility(ability, user, opponent):
    #target could possibly be choosable, need to accomodate that if it's implemented
    target = user if ability.target == "user" else opponent
        targetStat = (getattr(target, ability.effect)
        newStat = modifiers[ability.modifier(targetStat, ability.magnitude)
        #without much more breadth added to the stat system max hp cannot be altered with abilities
        if ability.effect[ == "maxhp":
            targetStat = target.hp
            if target.hp + newStat > target.maxhp:
                #INCOMPLETE FIX SOON STAT CHANGES NOT APPLIES AND NOT RECORED IN STATCHANGES in the case of heal
                statChange = target.hp + newStat - target.maxhp
                return
            else:
                statChange = newStat
                return
        if ability.duration != None:
            statChange = newStat - targetStat
            target.statChanges.append(statChange)
            target.duration.append(ability.duration)
modifiers = 
{
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.floordiv
}