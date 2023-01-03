#This Python program simulates the Monty Hall Problem. The Monty Hall Problem is a probability puzzle from
#a game show called "Let's Make A Deal" where the host, Monty Hall, would present three doors, and one
#of those doors contains a prize while the other two contain a goat. After the contestant picks one of the
#doors, Hall would open one of the doors that has a goat and ask the contestant if they would like to stay
#with their chosen door, or change it to the other unopened door. Statistics say if the contestant stays 
#with their current door, they would have a 1 in 3 chance of winning the prize and a 2 in 3 chance of winning 
#a goat. However, should the contestant switch to the other unopened door, they would have a 2 in 3 chance 
#of winning the prize and a 1 in 3 chance of winning a goat.
#If you would like to see another explanation, watch this video: https://www.youtube.com/watch?v=mhlc7peGlGg
#Note: the statistics stored in stats.txt may not reflect the actual stats presented above.

import random #Import the random class.

def playGame(): #The playGame() function, which holds the contents to play the game.
    try: #Try to run the function's contents, and stop if there are any errors.
        play = False #Automatically set the bool variable to false.
        f = open("stats.txt", "r") #Open the stats.txt file to get the previous statistics from the past times the player has played this game.
        ls = int(f.readline()) #;print(ls) #The number of times the player lost while staying with their chosen door.
        ws = int(f.readline()) #;print(ws) #The number of times the player won while staying with their chosen door.
        lw = int(f.readline()) #;print(lw) #The number of times the player lost while switching to the other unopened door.
        ww = int(f.readline()) #;print(ww) #The number of times the player won while switching to the other unopened door.
        f.close() #Close the file from the previous door.
        
        toPlay = input("Hello!\nWelcome to the \"Monty Hall Simulator\"\nThis program simulates the \"Monty Hall Problem\",\nand keeps track of the player's stats.\nWould you like to play?\nType either \"Yes\" or \"Y\" to play.\n").capitalize() #Ask the player if they would like to play the game.

        if toPlay == "Yes" or toPlay == "Y": #If the player chooses to play.
            play = True #Set the play boolean variable to True.

        while play: #While the game is playing, and the player chooses to play if they so desire.
            set1 = ["Prize", "Goat", "Goat"] #The first list of possibilities.
            set2 = ["Goat", "Prize", "Goat"] #The second list of possibilities.
            set3 = ["Goat", "Goat", "Prize"] #The third list of possibilities.
            set4 = [set1, set2, set3] #Putting all of the possibilities into a list.
            set5 = random.choice(set4) #Choosing a random list to play the game.
            set6 = [1, 2, 3] #Listing the number of doors, which will eventually be used for the other unopened door.
            #print(set5) #For debugging purposes.

            door = int(input("Choose your door: 1, 2, or 3:\n")) #Asks the player to pick a door.

            while door > 3 or door < 1: #While the player picks an invalid number.
                door = int(input("That is not a valid answer.\nChoose your door: 1, 2, or 3:\n")) #Keep asking until the player picks a correct option.

            set6.remove(door) #Remove the player's chosen door option from doors for the host to open.
            openDoor = random.randint(1,3) #Choose a door with a goat for the host to open.
            #print(openDoor) #For debugging purposes.

            while (set5[openDoor-1] == "Prize") or (openDoor == door): #While the host accidentally picks an invalid door.
                openDoor = random.randint(1,3) #Choose another door, and leave the loop when a valid door has been picked.
                #print(openDoor) #For debugging purposes.
            
            #print(openDoor) #For debugging purposes.

            set6.remove(openDoor) #Remove the door option the host had opened.
            choiceNew = input(f"Door {openDoor} contains a goat!\nWould you like to switch to door {set6[0]}?\n").capitalize() #Tell the player that one door contains a goat, and ask them if they would like to stay with their chosen door or switch to the other unopened door.

            if choiceNew == "Yes" or choiceNew == "Y": #If the player decides to switch doors.
                if set5[set6[0] - 1] == "Prize": #If the player has chosen the right door.
                    print("Congratulations!\nYou won a prize!") #Congratulate them, and award them a prize.
                    ww += 1 #Update the number of times the player has won while switching doors.
                else: #Otherwise, if the player has chosen the wrong door.
                    print("Sorry! You won a goat!") #Tell the player they won a goat.
                    lw += 1 #Update the number of times the player lost while switching doors.
            else: #Otherwise, if the player decides to stay with their chosen door.
                if set5[door - 1] == "Prize": #If the player chose the right door.
                    print("Congratulations!\nYou won a prize!") #Congratulate them, and award them a prize.
                    ws += 1 #Update the number of times the player won while staying with their chosen door.
                else: #Otherwise, if the player chose the wrong door.
                    print("Sorry! You won a goat!") #Tell the player they won a goat.
                    ls += 1 #Update the number of times the player lost while staying with their chosen door.

            play = False #Automatically set the play boolean variable to False incase the player decides not to play again.
            toPlay = input("Would you like to play again?\nType either \"Yes\" or \"Y\" to play again.\n").capitalize() #Ask the player if they would like to play the game again.
            if toPlay == "Yes" or toPlay == "Y": #If the player decides to play again.
                play = True #Set the play boolean variable to True.

        f1 = open("stats.txt", "w") #Open the stats.txt file to update the statistics.
        f1.write(str(ls) + "\n") #Update the number of times the player lost while staying with their chosen door.
        f1.write(str(ws) + "\n") #Update the number of times the player won while staying with their chosen door.
        f1.write(str(lw) + "\n") #Update the number of times the player lost while switching to the other unopened door.
        f1.write(str(ww) + "\n") #Update the number of times the player won while switching to the other unopened door.
        f1.close() #Close the stats.txt file after updating the statistics.
        #print("Everything ran smoothly!") #For debugging purposes.
    except: #If there is an error.
        print("ERROR IN playGame() FUNCTION!") #Tell the player there is an error in the playGame() function.

playGame() #Call the playGame() function.