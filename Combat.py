class battle:

    def dealDamage(self, attacker, defender):
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
        main.clear()
        print((critical + devestate + attacker.name + " dealt " + str(damage) + " damage to " + defender.name + "!"))
        main.wait()
        if defender.hp < 0:
            defender.hp = 0


    def battle(self, player, enemy):
        turn = 1
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
                    #only show players last choice as an available option
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