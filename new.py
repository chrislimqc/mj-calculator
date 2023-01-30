print("Welcome to mj no chips, used to calculate money owed in place of chips")
running = True
state = "0"
buyIn = 200
players = ["d", "n", "s", "b"]
menuChoices = {"1": "HU", "2": "gang", "3": "yao", "4": "show", "5": "redo names", "6": "show history"}
score = {}
history = ["N: start game"]

def startScore(players, buyIn):
    for name in players:
        score[name] = buyIn
    print(score)

def calculateScore(mode, winner, shooter, tai):
    print("mode is {}, winner is {}, shooter is {}, tai is {}".format(mode, winner, shooter, tai))
    history.append("mode is {}, winner is {}, shooter is {}, tai is {}".format(mode, winner, shooter, tai))
    if mode == "zi moh":
        score[winner] += tai * 2 * 4
        for name in players:
            if name != winner:
                score[name] -= (tai * 2)

    elif mode == "an yao" or  mode == "an gang": #an yao or an gang
        score[winner] += 4 * 4
        for name in players:
            if name != winner:
                score[name] -= 4

    elif mode == "shoot":
        score[winner] += tai * 2 * 4
        score[shooter] -= (tai * 2 * 4)
    
    elif mode == "gang":
        score[winner] += 1 * 2 * 3
        score[shooter] -= (1 * 2 * 3)


    elif mode == "yao bieren": #yao bieren
        score[winner] += 2
        score[shooter] -= 2
    

    


while running:

    #END
    if state == "gg":
        print("done")
        running = False

    #menu
    elif state == "menu":
        print("Menu <3")
        choice = input("choices are \n1. Sombody HU \n2. Somebody Gang \n3. Yao \n4. show score \n5. edit names \n6. show history")
        if choice.isdigit() and int(choice) < 7 and int(choice) > 0:
            print("choice is {}".format(choice))
            state = menuChoices[choice]
            print("state is {}".format(state))
            
        else:
            print("invalid choice")

    elif state == "HU":
        winner = input("who won")
        winMode = input("zi moh or shoot")
        tai = int(input("how many tai"))

        if winMode == "shoot":
            shooter = input("who shoot")
        else:
            shooter = "nil"
        
        history.append("H: somebody hu")
        calculateScore(winMode, winner, shooter, tai)
        print(score)
        state = "menu"

    elif state == "gang":
        winner = input("who gang")
        shooter = input("who shoot, if an gang put nil")
        if shooter == "nil":
            shooter = "nil"
            calculateScore("an gang", winner, shooter, "nil")
        else:
            calculateScore("gang", winner, shooter, "nil")

        print(score)
        state = "menu"
    
    elif state == "yao":
        winner = input("who yao")
        mode = input("an yao ziji or just yao ziji or yao bieren")
        if mode == "an yao":
            calculateScore(mode, winner, "nil", "nil")
        elif mode == "yao": #havent program a diff
            calculateScore(mode, winner, "nil", "nil")
        else:
            shooter = input("yao who?")
            calculateScore(mode, winner, shooter, "nil")

        print(score)
        state = "menu"

    elif state == "show":
        print(score)
        state = "menu"


    
    #entry point
    elif state == "0":
        state = input("to skip configuration enter \"skip\" ")
        print("input is {}".format(state))
        if state == "skip":
            startScore(players, buyIn)
            state = "menu"
        else:
            state = "1"
    
    elif state == "1":
        state = "1"
        buyIn = input("please enter buy In amount")
        if buyIn.isdigit():
            print("Buy in is {}".format(buyIn))
            state = "2"
        else:
            print("please enter a valid number")
            
    elif state == "2":
        print("please enter initials of the 4 players")
        players[0] = input("player 1 is: ")
        players[1] = input("player 2 is: ")
        players[2] = input("player 3 is: ")
        players[3] = input("player 4 is: ")
        print("players are :")
        for name in players:
            print(name)
        
        comfirm = input("enter \"redo\" to redo, \"cont\" to continue")
        if comfirm == "redo":
            state = "redo names"
        elif comfirm == "cont":
            state = "menu"
        else:
            comfirm = input("wtf are you typing, nvm later can change")
            state = "menu"



    
    elif state == "3":
        print("done")
        running = False

    #extra stuff
    elif state == "redo names":
        print("redoing names, which name to change? press the number on the side 0-3")
        print(players)
        nameNo = int(input())
        players[nameNo] = input("new name is?")
        print("ok name changed names are now")
        print(players)
        state = "menu"
    
    elif state == "show history":
        for line in history:
            print(line)
        state = "menu"
    
    else:
        print("state not programmed")
        state = "menu"
        
