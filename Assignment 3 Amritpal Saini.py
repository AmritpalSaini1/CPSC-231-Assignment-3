# Amritpal Saini, Lecture 2, 30039983
#I believe Parts 1, 2, and 3 are solved correctly
#line 244 has the commented print statement to look at the final hat if the trained AI, it is specific for 10 nuts but
#the numbers can be changed accordingly

import random

def turn(player, total):
    #Turn function is used to shorten the program. This is used for all instances of a player inputting their selection
    #Got this code from https://stackoverflow.com/questions/41832613/python-input-validation-how-to-limit-user-input-to-a-specific-range-of-integers
    #Player is for naming purposes. It allows to tell the difference between player one and two for player vs player

    print("There are", total, " nuts on the board") #For the User Interface of the game
    #lines 13 to 39 are from the website stated above. It is used for limiting the user input for
    #the number of nuts the player can take and also the options for replaying the game.
    while True:
        try:
            play = int(input(player + " : How many nuts do you take (1-3)? "))
            if play < 1 or play > 3:
                raise ValueError  # this will send it to the print message and back to the input option
            else:
                total -= play
                if total < 1:
                    while True:
                        try:
                            replay = int(input(
                                player + ''', you lose.
                                play again? (1 = yes, 0 = no) 
                                '''))
                            if replay == 1:
                                MainMenu()
                            elif replay == 0:
                                quit()
                            else:
                                raise ValueError
                            break
                        except ValueError:
                            print("Invalid integer. The number must be in the range of 0-1.")

            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 1-3.")
    return total

def PvP(nuts):
    #PvP stands for Player vs Player. The parameter, "nuts" is used to know the total and as a counter for when to end the game
    total = nuts
    while (total > 0): #While the total is more than 0, keep the game between the two players going
        total = turn("Player 1", total)
        total = turn("Player 2", total)
    return

def AIList(nuts):  # given in the assignment, used for making the 2D lists
    hats = []
    for i in range(nuts):
        row = [1, 1, 1]
        hats += [row]
    return hats

def select(p, nuts):  # given in the assignment, modified to allow for 2D lists
    # assumes p is a list of three positive integers
    total = p[nuts-1][0] + p[nuts-1][1] + p[nuts-1][2]
    r_int = random.randint(1, total)
    if (r_int <= p[nuts-1][0]):
        move = 1
    elif (r_int <= p[nuts-1][0] + p[nuts-1][1]):
        move = 2
    else:
        move = 3
    return move

def PvUnAI(nuts, hats): #Name is short for Player vs Untrained Artifical Intellegence
    #nuts again are used for total and hat is used for the 2D list
    total = nuts
    newHat = hats #There are two Hats because one is left untouched if the AI was to lose the game
    OrgHat = hats
    while (total > 0): # while there are nuts on the table, keep playing
        turn = 1 #used to move the turn back and forth between AI and Player
        if (turn == 1):
            print("There are", total, " nuts on the board")  # For the User Interface of the game
            # lines 13 to 39 are from the website stated above. It is used for limiting the user input for
            # the number of nuts the player can take and also the options for replaying the game.
            #same as the turn function but because this AI learns over time, I had to make a second menu which could only
            #be accessed through writing the whole code out.
            while True:
                try:
                    play = int(input("Player 1 : How many nuts do you take (1-3)? "))
                    if play < 1 or play > 3:
                        raise ValueError  # this will send it to the print message and back to the input option
                    else:
                        total -= play
                        turn += 1
                        if total < 1:
                            while True:
                                try:
                                    replay = int(input(
                                        '''Player, you lose.
                                        play again? (1 = yes, 0 = no) 
                                        '''))
                                    if replay == 1:
                                        newHat = OrgHat
                                        Menu2(newHat)
                                    elif replay == 0:
                                        quit()
                                    else:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print("Invalid integer. The number must be in the range of 0-1.")

                    break
                except ValueError:
                    print("Invalid integer. The number must be in the range of 1-3.")
        if (turn == 2): #This is the untrained AI making it's move.
            print("There are", total, " nuts on the board")
            AIMove = select(hats, total)
            total -= AIMove
            newHat[nuts - 1][AIMove - 1] += 1
            print("AI selects", AIMove)
            if total > 0:
                turn -= 1
            else:
                while True:
                    try:
                        replay = int(input(
                            '''AI loses.
                            play again? (1 = yes, 0 = no) 
                            '''))
                        if replay == 1:
                            Menu2(OrgHat)
                        elif replay == 0:
                            quit()
                        else:
                            raise ValueError
                        break
                    except ValueError:
                        print("Invalid integer. The number must be in the range of 0-1.")

def TrainingAI(nuts, hat1, hat2): #This function is used to train the AI. nuts are again for counter purposes
    #hat1 and hat2 are 2D lists for the game to use for the sake of learning.
    #as the trainer and training progress, their winning hats are replace the previous hats
    training = hat1
    trainer = hat2
    trainingNew = hat1
    trainerNew = hat2
    for i in range(100000): #The two AI's play 100000 times
        turn = 1
        total = nuts
        while total > 0:
            if turn == 1:
                AIMove1 = select(trainer, total - 1)
                trainerNew[total - 1][AIMove1 - 1] += 1 #The edits to the hat are done right away
                total -= AIMove1
                if total > 0:
                    turn += 1
                elif total < 1: #If Trainer loses, the edits are replaced with the last winning copy of the trainer
                    trainerNew = trainer
                    training = trainingNew

            if turn == 2: #same as above, but for training instead of trainer
                AIMove2 = select(training, total - 1)
                total -= AIMove2
                training[total - 1][AIMove2 - 1] += 1
                if total > 0:
                    turn -= 1
                elif total < 1:
                    trainer = trainerNew
                    trainingNew = training
    return training

def PvTAI(nuts): #Short for player vs Trained AI, nuts used as a counter
    hat = AIList(nuts) #hat generated to run the TrainingAI function
    print("Training AI, please wait...") #used to make the wait seem normal.
    TrainedHat = TrainingAI(nuts, hat, hat) #Because the return on TrainingAI is the training hat
    total = nuts
    while (total > 0):
        total = turn("Player 1", total) #Funtion used from above to simplify code, equals total so player moves are registered
        print("There are", total, " nuts on the board")
        AIMove = select(TrainedHat, total) #function from above, used to select the move of the AI
        total -= AIMove #move is subtracted from the total to progress the game
        print("AI selects", AIMove)
        if total < 1:
            while True: #code from the top to limit user inputs
                try:
                    replay = int(input(
                        '''Player 1, you lose.
                        play again? (1 = yes, 0 = no) 
                        '''))
                    if replay == 1:
                        MainMenu()
                    elif replay == 0:
                        quit()
                    else:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid integer. The number must be in the range of 0-1.")

def MainMenu(): ## This function for players to select between Player v Player, Player v Untrained AI and Player v Trained AI
    while True:
        try:
            nuts = int(input('''
            Welcome to the game of nuts!
            How many nuts are there on the table initially (10-100)?
                     '''))
            if nuts < 10 or nuts > 100:
                raise ValueError
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 10-100.")
    hats = AIList(nuts)

    mode = int(input('''
    Options:
     Play against a friend (1)
     Play against the computer (2)
     Play against the trained computer (3)
    Which option do you take (1-3)?
    '''))
    if mode == 1:
        PvP(nuts)
    elif mode == 2:
        PvUnAI(nuts, hats)
    elif mode == 3:
        PvTAI(nuts)
    else:
        MainMenu()

def Menu2(hats): #same as above but takes hat as a parameter in case the untrained AI wins
    while True:
        try:
            nuts = int(input('''
            How many nuts are there on the table initially (10-100)?
                     '''))
            if nuts < 10 or nuts > 100:
                raise ValueError
            break
        except ValueError:
            print("Invalid integer. The number must be in the range of 10-100.")
    mode = int(input('''
    Options:
     Play against a friend (1)
     Play against the computer (2)
     Play against the trained computer (3)
    Which option do you take (1-3)?
    '''))
    if mode == 1:
        PvP(nuts)
    elif mode == 2:
        PvUnAI(nuts, hats)
    elif mode == 3:
        PvTAI(nuts)
    else:
        Menu2(hats)

MainMenu()

#print(TrainingAI(10, AIList(10), AIList(10)))