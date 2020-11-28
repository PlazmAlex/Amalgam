class Ability:
    def __init__(self, name, effects, modifier, magnitude, duration):
        self.name = name
        self.effects = effects
        self.modifiers = modifiers
        self.magnitude = magnitude
        self.duration = duration
    
def instantiateAbilities():
    shred = Ability("Shred",[bleedLevel], ["+"], [1], None)
    doubleEviscerate = Ability("Double Eviscerate", [bleedLevel], ["+"], [2], None)
    heal = Ability("Heal", [HP], ["*"], [1.7], None)
    rejuvinate = Ability("Rejuvinate", [HP], ["*"], [2], None)
    strengthen = Ability("Strengthen"), [], 
    bellow = Ability("Bellow")
    timeLoop = Ability("Time Loop")