import os
import ClassFile
import sys
while(True):
    mageEffect = False
    def wait():
        input("\n\nPress enter to continue")
    def clear():
        os.system('cls')
    def clearLine():
        print("noyj")
    print("*********\n*Amalgam*\n*********")
    wait()
    def initialize_game():
        clear()
        response = input("Enter number to select menu option\n\n1) New Run\n2) Class\n")
        os.system('cls')
        
        if response == "2":
            print("No other classes unlocked")
            wait()
            initialize_game()
            
        elif response == "1": 
            global SaveOne
            name = ""
            n = 1
            while (len(name) > 15 or len(name) < 1):
                clear()
                if n < 2:
                    limit = ""
                else:
                    limit = "(15 character limit)"
                name = input("Please name your Amalgam %s\n" % limit)
                n += 1
            clear()
            SaveOne = ClassFile.SaveFile(name)
            print(("Alright " + SaveOne.name + ", time to begin your adventure."))
            input()
        else:
            initialize_game()
            
    def dealDamage(attacker, defender):
        critical = ""
        devestate = ""
        if defender.guard == True:
            clear()
            print((defender.name + " guarded!\n"))
            defense = defender.defense * 3
            wait()
        else:
            defense = defender.defense
        damage = attacker.attack - defense
        if attacker.superAttack == True:
            damage = damage * 3
            devestate = "!!Devastating Attack!!\n\n"
            attacker.superAttack = False
        elif defender.vulnerable == True:
            damage = damage * 2
            critical = "!!!Critical Strike!!!\n\n"
        if damage <= 0:
            damage = 1
        defender.hp = defender.hp - damage
        clear()
        print((critical + devestate + attacker.name + " dealt " + str(damage) + " damage to " + defender.name + "!"))
        wait()
        if defender.hp < 0:
            defender.hp = 0
    def shred(player, enemy):
        if enemy.guard == True:
            clear()
            print((enemy.name + " guarded!\n"))
            wait()
            clear()
            return
        enemy.bleedLevel += 1
        clear()
        print((enemy.name + " has been shredded!"))
        wait()
    def shredE(player, enemy):
        if player.guard == True:
            clear()
            print((player.name + " guarded!\n"))
            wait()
            clear()
            return
        player.bleedLevel += 1
        clear()
        print((player.name + " has been shredded!"))
        wait()
    def doubleeviscerate(player,enemy):
        if enemy.guard == True:
            clear()
            print((enemy.name + " guarded!\n"))
            wait()
            clear()
            return
        enemy.bleedLevel += 2
        clear()
        print((enemy.name + " was torn apart!"))
        wait()    
    def useAbilityEnemy(player,enemy):
        enemyAbilityLib = {
            "Shred": shredE,
            "Time Loop" : timeLoopE
        }
        enemyAbilityLib.get(enemy.ability)(player,enemy)
    def heal(player, enemy):
        clear()
        heal = int(round(player.maxhp * 0.70) + 1)
        player.hp = player.hp + heal
        print((player.name + " healed " + str(heal) + " HP!"))
        wait()
        if player.hp > player.maxhp:
            player.hp = player.maxhp
    def rejuvinate(player,enemy):
        clear()
        heal = int(player.maxhp)
        player.hp = player.hp + heal
        print((player.name + " restored " + "all" + " HP!"))
        wait()
        if player.hp > player.maxhp:
            player.hp = player.maxhp
    def strengthen(player, enemy):
        player.attack = player.attack + 2
        clear()
        print((player.name + " grew stronger!\n\nAttack + 2"))
        wait()
    def bellow(player, enemy):
        player.attack = player.attack + 3
        clear()
        print((player.name + " ROARED!!\n\nAttack + 3"))
        wait()
    def timeLoopE(player,enemy):
        player.timeLoop += 3
        clear()
        print((enemy.name + " put " + player.name + " in a time loop for 2 turns!"))
        wait()
    def useAbility(ability, player, enemy):
        abilityLib = {
            "Shred": shred,
            "Heal": heal,
            "Strengthen": strengthen,
            "Double Eviscerate": doubleeviscerate,
            "Rejuvinate": rejuvinate,
            "Bellow": bellow
        }
        abilityLib.get(ability)(player, enemy)
        player.abilityUsed = True
        player.lastAbilityUsed[0] = ability
        player.AP -= 1
    def getAbilities(player, enemy):
        if len(player.abilities) < 1:
            clear()
            print ("No Abilities")
            wait()
            return
        choice = ""
        options = []
        for x in range(1,(len(player.abilities)+2)):
            options.append(str(x))
        while (choice not in options):
            clear()
            n = 1
            for x in player.abilities:
                print((str(n) + ") " + x))
                n = n + 1
            print((str(n) + ") " + "Return"))
            choice = input()
        if int(choice) == len(player.abilities) + 1:
            return
        if player.AP < 1:
            clear()
            print("No ability points left")
            wait()
            return
        else:
            #player.abilityUses[int(choice)-1] = player.abilityUses[int(choice)-1] - 1 THIS IS FOR SUBTRACTING A USE FROM INDIVIDUAL ABILITIES
            useAbility(player.abilities[int(choice)-1], player, enemy)

    def resethp(player, enemy):
        player.hp = player.maxhp
        enemy.hp = enemy.maxhp
    def resetdefense(player, enemy):
        player.defense = player.maxdefense
        enemy.defense = enemy.maxdefense
    def resetattack(player, enemy):
        player.attack = player.maxattack
        enemy.attack = enemy.maxattack
        
    def battle(player, enemy):
        turn = 1
        lastAction = ""
        enemyBleed = ""
        playerBleed = ""
        while enemy.hp > 0 and player.hp > 0:
            clear()
            #Display info
            print(("Turn: " + str(turn)))
            if mageEffect == True:
                if turn in range(1,100,2):
                    print(("\n!!!!" + enemy.name + " prevents abilities on odd turns!!!!\n"))
                    player.canUseAbilities = False
            if turn in enemy.superTurn:
                print(("\n!!!" + enemy.name + " is preparing a devastating attack!!!\n\n"))
                enemy.superAttack = True
                enemy.vulnerable = True
            elif turn in enemy.guardTurn:
                print(("\n!" + enemy.name + " is guarding!\n\n"))
                enemy.guard = True
            elif turn in enemy.debuffTurn:
                if mageEffect == True:
                    print(("\n!!" + enemy.name + " is going to create a time loop!!\n\n"))
                else:
                    print(("\n!!" + enemy.name + " is going to debuff " + player.name + "!!\n\n"))
                enemy.debuff = True
                enemy.vulnerable = True
            #-------------------
            #Time Loop Check
            #if player.timeLoop == 0:  
            print("Enter number to select battle option\n\n")  
            print((player.name + "'s HP (" + str(player.hp) + "/" + str(player.maxhp) +
            ")  AP (" + str(player.AP) + ") " + playerBleed +
            "\n\n" + enemy.name + "'s HP (" + str(enemy.hp) + "/" + str(enemy.maxhp) + ")" + enemyBleed +
            "\n"))
            n = 1
            for x in player.currentOptions:
                if player.timeLoop != 0:
                    if x != player.currentOptions[int(choice)-1]:
                        continue
                print((str(n) + ") " + x))
                n += 1
            if player.timeLoop != 0:
                while input() != "1":
                    #Looking for a better way to reset screen on incorrect input
                    clear()
                    print(("Turn: " + str(turn)))
                    if mageEffect == True:
                        if turn in range(1,100,2):
                            print(("\n!!!!" + enemy.name + " prevents abilities on odd turns!!!!\n"))
                            player.canUseAbilities = False
                    if turn in enemy.superTurn:
                        print(("\n!!!" + enemy.name + " is preparing a devastating attack!!!\n\n"))
                        enemy.superAttack = True
                        enemy.vulnerable = True
                    elif turn in enemy.guardTurn:
                        print(("\n!" + enemy.name + " is guarding!\n\n"))
                        enemy.guard = True
                    elif turn in enemy.debuffTurn:
                        if mageEffect == True:
                            print(("\n!!" + enemy.name + " is going to create a time loop!!\n\n"))
                        else:
                            print(("\n!!" + enemy.name + " is going to debuff " + player.name + "!!\n\n"))
                        enemy.debuff = True
                        enemy.vulnerable = True
                    #-------------------
                    #Time Loop Check
                    #if player.timeLoop == 0:  
                    print("Enter number to select battle option\n\n")  
                    print((player.name + "'s HP (" + str(player.hp) + "/" + str(player.maxhp) +
                    ")  AP (" + str(player.AP) + ") " + playerBleed +
                    "\n\n" + enemy.name + "'s HP (" + str(enemy.hp) + "/" + str(enemy.maxhp) + ")" + enemyBleed +
                    "\n"))
                    n = 1
                    for x in player.currentOptions:
                        if player.timeLoop != 0:
                            if x != player.currentOptions[int(choice)-1]:
                                continue
                        print((str(n) + ") " + x))
                    continue
            else:
                choice = input()
            #-------------
            #Menu Choice
            if choice == str(player.currentOptions.index("Attack")+1):
                dealDamage(player, enemy)
            elif choice == str(player.currentOptions.index("Abilities")+1):
                if player.timeLoop != 0:
                    player.AP += 1
                    useAbility(player.lastAbilityUsed[0], player, enemy)
                    player.canUseAbilities = True
                if player.canUseAbilities == False:
                    clear()
                    print((player.name + " cannot use abilites right now."))
                    wait()
                    continue
                if player.timeLoop == 0:
                    getAbilities(player, enemy)
                if player.abilityUsed == False:
                    continue 
                player.abilityUsed = False
            elif choice == str(player.currentOptions.index("Guard")+1): 
                player.guard = True
            else:
                continue
            #--------------
            #Enemy Action
            if enemy.hp > 0 and enemy.guard == False and enemy.debuff == False:
                dealDamage(enemy, player)
            elif enemy.debuff == True:
                useAbilityEnemy(player, enemy)
                
            #------------
            #End of Turn effects
            if player.timeLoop > 0:
                clear()
                print((player.name + " is stuck in a time loop!"))
                wait()
                player.timeLoop -= 1
            player.canUseAbilities = True
            player.guard = False
            enemy.guard = False
            enemy.vulnerable = False
            enemy.debuff = False
            if (player.bleedLevel > 0) and (enemy.hp > 0):   
                playerBleed = (" BLEED(LV " + str(player.bleedLevel) + ")")
                player.hp = player.hp - player.bleedLevel * 2
                clear()
                print((player.name + " bled for " + str(player.bleedLevel * 2) + " damage!"))
                wait()
                if player.hp <= 0:
                    clear()
                    print((player.name + " bled out!"))
                    wait()
            if enemy.bleedLevel > 0:
                enemyBleed = (" BLEED(LV " + str(enemy.bleedLevel) + ")")
                enemy.hp = enemy.hp - enemy.bleedLevel * 2
                clear()
                print((enemy.name + " bled for " + str(enemy.bleedLevel * 2) + " damage!"))
                wait()
                if enemy.hp <= 0:
                    clear()
                    print((enemy.name + " bled out!"))
                    wait()
            #-------------
            turn = turn + 1
        player.lastAbilityUsed = [""]
        player.bleedLevel = 0
        enemy.bleedLevel = 0
        resetattack(player, enemy)
        resetdefense(player, enemy)
        player.AP = player.maxAP
        if player.hp > 0:
            resethp(player, enemy)
            clear()
            print((player.name + " survived!"))
            wait()
        else:
            resethp(player, enemy)
            clear()
            print((player.name + " died!"))#Need lose function
            wait()
            sys.exit(0)
            

    def wait():
        input("\n\nPress enter to continue")
        
    def clear():
        os.system('cls')
        
    clear()
    initialize_game()


    #CHAPTER 1
    clear()
    print((SaveOne.name + " breaks from of his egg to breathe his first breath."))
    wait()
    clear()
    print("The hands of fate have other plans, however...")
    wait()
    clear()
    print("A rat seeks to claim your newfound mortality.")
    wait()
    Rat = ClassFile.enemy("Rat",25,3,1,[3,4,9,12],[],[],None,["no loot"])
    battle(SaveOne, Rat)

    def abilityUpgrade(player,abilities,enemy):
        response = 0
        responseBank = []
        n = 1
        while response not in responseBank:
            for ability in abilities:
                responseBank.append(str(n))
                print(enemy.name + " defeated! Choose an ability!")
                print("\n" + n + ")" + enemy.loot[n] + "\n" + ability.name + " - " + ability.description)
                n += 1
                continue
            response = input()
            clear()
        player.abilities.append(abilities[int(response)-1])
    clear()



    #Chapter 2
    clear()
    print("A wild Pig appears!")
    wait()
    pigSTurns = [2,7,8,10,12,16,20]
    pigGTurns = []
    Pig = ClassFile.enemy("Pig",35,4,1,pigSTurns,pigGTurns,[],None,["no loot"])
    battle(SaveOne, Pig)

    def levelUp(player,hp,attack,defense,AP):
        print("Pig Defeated! Level Up!")
        input()
        player.maxhp += hp
        player.hp = player.maxhp
        print("HP + " + str(hp))
        input()
        player.maxattack += attack
        player.attack = player.maxattack
        print("Attack + " + str(attack))
        input()
        player.maxdefense += defense
        player.defense = player.maxdefense
        print("Defense + " + str(defense))
        input()
        player.maxAP += AP
        player.AP = player.maxAP
        print("Max AP + " + str(AP))
    clear()
    levelUp(SaveOne,20,4,1,1)
    wait()

    #Chapter 3
    
    orcSTurns = [2,7,13,15,16,17]
    orcGTurns = [3,4,8,9,14]
    Orc = ClassFile.enemy("Young Orc",40,9,3,orcSTurns,orcGTurns,[],None,["no loot"])
    battle(SaveOne, Orc)


    def secondUpgrade(player):
        response = 0
        responseBank = ["1","2","3"]
        while response not in responseBank:
            print("Orc defeated! Choose an Ability or Upgrade!")
            
            if "Shred" in player.abilities:
                description = ("Double Eviscerate - Increase enemy's bleed level by 2.")
            else:
                description = ("Shred - Increase enemy's bleed level by 1. Each level deals 2 damage per turn.")
            print(("\n1)Equip Orc's Sword\n%s" % description))
            
            if "Heal" in player.abilities:
                description = ("Rejuvinate - Heal all HP")
            else:
                description = ("Heal - Restore 70% of max HP.")
            print(("\n2)Absorbs Orc's soul\n%s" % description))
            
            if "Strengthen" in player.abilities:
                description = ("Bellow - Buff attack by 3 until end of battle.")
            else:
                description = ("Strengthen - Buff attack by 2 until end of battle.")
            print(("\n3)Feel the Orc's rage\n%s" % description))
            response = input()
            if response == "1":
                if "Shred" in player.abilities:
                    player.abilities[(player.abilities.index("Shred"))] = "Double Eviscerate"
                else:
                    player.abilities.append("Shred")
            elif response == "2":
                if "Heal" in SaveOne.abilities:
                    player.abilities[player.abilities.index("Heal")] = "Rejuvinate"
                else:
                    player.abilities.append("Heal")
            elif response == "3":
                if "Strengthen" in player.abilities:
                    player.abilities[player.abilities.index("Strengthen")] = "Bellow"
                else:
                    player.abilities.append("Strengthen")
            clear()
            continue
    clear()
    secondUpgrade(SaveOne)
    #Chapter 4
    slothSTurns = [6,15,18,23,26,30,35,38,41,42,43,44,45]
    slothGTurns = [4,5,9,14,16,20,21,24,25,31,32,33,34,36,37]
    slothDTurns = [1,2,3,7,8,10,11,12,13,17,19,22,27,28,29,39,40]
    SavageSloth = ClassFile.enemy("Savage Sloth", 100, 10, 1,
    slothSTurns, slothGTurns, slothDTurns,"Shred",["no loot"])
    battle(SaveOne, SavageSloth)
    clear()
    
    levelUp(SaveOne,55,3,2,1)

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
    mageEffect = True
    temporalMage = ClassFile.enemy("Temporal Mage",191,13,2,
    mageSTurns, mageGTurns, mageDTurns, "Time Loop", ["no loot"])
    wait()
    battle(SaveOne, temporalMage)

    clear()
    print((SaveOne.name + " defeated " + temporalMage.name + "!"))
    wait()

    clear()
    print("Temporal mage class unlocked!!")
    wait()

    clear()
    print("But not yet...\nComing soon!")
    wait() 
