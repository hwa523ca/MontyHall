#This Python program simulates the Monty Hall Problem. The Monty Hall Problem is a probability puzzle from
#a game show called "Let's Make A Deal" where the host, Monty Hall, would present three doors, and one
#of those doors contains a prize while the other two contain a goat. After the contestant picks one of the
#doors, Hall would open one of the doors that has a goat and ask the contestant if they would like to stay
#with their chosen door, or change it to the other unopened door. Statistics say if the contestant stays 
#with their current door, they would have a 1 in 3 chance of winning the prize and a 2 in 3 chance of winning 
#a goat. However, should the contestant switch to the other unopened door, they would have a 2 in 3 chance 
#of winning the prize and a 1 in 3 chance of winning a goat.
#This version uses tkinter for GUI, so the user wouldn't have to type constantly, nor anything wrong.
#If you would like to see another explanation, watch this video: https://www.youtube.com/watch?v=mhlc7peGlGg
#Note: the statistics stored in stats.txt may not reflect the actual stats presented above.

import tkinter as tk #Import tkinter as the GUI for this file; please note, tkinter is refered as tk for convenience.
from tkinter import messagebox #Import the messagebox function from tkinter.
import random #Import random

class MontyHall: #Create the MontyHall Class to store the contents of the game.

    def __init__(self): #Initiate the constructor.
        self.first_goat_found = False #If the first goat, from a door that was not chosen, was found, set it to True, but we are initially setting it to False since the first goat has not been found yet.
        self.game_finished = False #If the game is finished, set it to True, but we are initially setting it to False since the game has not been played yet.
        self.game_playing = False #If the game is ongoing, set it to True, but if it's not, set it to False.
        self.game_saved = True #If the statistics have been saved, set it to True; otherwise, set it to False. Initially set it to true because the user has not played the game yet.
        self.game_loaded = False #If the statistics have not been loaded yet, set it to False; otherwise, set it to True.
        self.prize_location = random.randint(1,3) #Choose a door for the prize to hide.
        self.ls = 0 #The number of times the player lost while staying with their chosen door.
        self.ws = 0 #The number of times the player won while staying with their chosen door.
        self.lw = 0 #The number of times the player lost while switching to the other unopened door.
        self.ww = 0 #The number of times the player won while switching to the other unopened door.
        self.previous_door = 0 #The previous door the player chose.

        self.root = tk.Tk() #Initiate the GUI by calling the tkinter class.
        self.root.geometry("800x400") #Set the dimensions of the window.
        self.root.title("Monty Hall Simulator") #Name the title of the window.

        self.menubar = tk.Menu(self.root) #Create a menu bar.

        self.gamemenu = tk.Menu(self.menubar, tearoff=0) #Declare a menu bar.
        self.gamemenu.add_command(label="Load Statstics", command=self.load_statistics) #Create a button called Load Statistics that loads the previously saved statistics.
        self.gamemenu.add_command(label="Save Statstics", command=self.save_statistics) #Create a button called Save Statistics that saves the current statistics.
        self.gamemenu.add_command(label="Check Statstics", command=self.check_statistics) #Create a button called Check Statistics that displays the current statistics.
        self.menubar.add_cascade(menu=self.gamemenu, label="Settings") #Name the title of the menu bar Settings.
        self.root.config(menu=self.menubar) #Configure the menu bar.

        self.label = tk.Label(self.root, text="Monty Hall Problem Simulator", font=('Arial', 18)) #Insert a label to inform the user they're using the Monty Hall Simulator.
        self.label.pack(padx=10, pady=10) #Display the label with the pack method.

        self.buttonframe = tk.Frame(self.root) #Initiate a button frame to set a series of buttons.
        self.buttonframe.columnconfigure(0, weight=1) #First button, used as Door Number 1.
        self.buttonframe.columnconfigure(1, weight=1) #Second button, used as Door Number 2.
        self.buttonframe.columnconfigure(2, weight=1) #Third button, used as Door Number 3.

        self.door1 = tk.Button(self.buttonframe, text="Door 1", font=('Arial', 18), command=self.choose_door_1) #Initiate a button for Door Number 1.
        self.door1.grid(row=0, column=0, sticky=tk.W+tk.E) #Display the button with the pack method.

        self.door2 = tk.Button(self.buttonframe, text="Door 2", font=('Arial', 18), command=self.choose_door_2) #Initiate a button for Door Number 2.
        self.door2.grid(row=0, column=1, sticky=tk.W+tk.E) #Display the button with the pack method.

        self.door3 = tk.Button(self.buttonframe, text="Door 3", font=('Arial', 18), command=self.choose_door_3) #Initiate a button for Door Number 3.
        self.door3.grid(row=0, column=2, sticky=tk.W+tk.E) #Display the button with the pack method.

        self.buttonframe.pack() #Display the button frame with the pack method.

        self.label2 = tk.Label(self.root, text="Choose one of three doors", font=('Arial', 18)) #Insert a label to inform the user what has happened when playing the simulator.
        self.label2.pack(padx=10, pady=10) #Display the label with the pack method.

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing) #When the user wishes to close the window.

        self.root.mainloop() #Run the program.

    def load_statistics(self): #Function that loads the statistics.
        if self.game_playing == False:
            f = open("stats1.txt", "r") #Open the stats1.txt file to get the previous statistics from the past times the player has played this game.
            self.ls = int(f.readline()) #The number of times the player lost while staying with their chosen door.
            self.ws = int(f.readline()) #The number of times the player won while staying with their chosen door.
            self.lw = int(f.readline()) #The number of times the player lost while switching to the other unopened door.
            self.ww = int(f.readline()) #The number of times the player won while switching to the other unopened door.
            f.close() #Close the file.
            self.game_saved = False #Set the game saved boolean to False because the game has not been saved yet.
            self.game_loaded = True #Set the game loaded boolean to True because the previous statistics have been loaded.

    def save_statistics(self): #Function that saves the statistics.
        if self.game_playing == False: #If the game is not being played.
            if self.game_loaded == False: #If the game has not been loaded yet.
                if messagebox.askyesno(title="Statistics not loaded", message="The statistics from the previous game have not been loaded.\nDo you wish to continue?"): #If the user decides to go ahead and overwrite the statistics.
                    self.save() #Call the save function.
            else: #Otherwise.
                self.save() #Call the save function.

    def save(self):
        f = open("stats1.txt", "w") #Open the stats1.txt file to get the previous statistics from the past times the player has played this game.
        f.write(str(self.ls) + "\n") #Update the number of times the player lost while staying with their chosen door.
        f.write(str(self.ws) + "\n") #Update the number of times the player won while staying with their chosen door.
        f.write(str(self.lw) + "\n") #Update the number of times the player lost while switching to the other unopened door.
        f.write(str(self.ww)) #Update the number of times the player won while switching to the other unopened door.
        f.close() #Close the stats1.txt file after updating the statistics.
        self.game_saved = True #Set the game saved boolean to True because the game has been saved.

    def check_statistics(self): #Function to display the statistics.
        if self.game_playing == False: #If the game is not playing right now.
            self.label2.config(text=f"Times the player lost while staying with their cosen door: {self.ls}\nTimes the player won while staying with their cosen door: {self.ws}\nTimes the player lost while switching to the other unopened door: {self.lw}\nTimes the player won while switching to the other unopened door: {self.ww}") #Change label 2 to tell inform the user of the statistics.

    def reset(self): #The reset function.
        self.reset_button.destroy() #Destroy the initial reset button that was displayed before this function was called.
        self.prize_location = random.randint(1,3) #Choose a new random door to hide the prize in.
        self.first_goat_found = False #Reset the boolean condition where the first goat was found.
        self.game_finished = False #Reset the boolean condition where the game was finished.
        self.door1.config(text="Door 1", command=self.choose_door_1) #Change the text of Button/Door 1 to say Door 1.
        self.door2.config(text="Door 2", command=self.choose_door_2) #Change the text of Button/Door 2 to say Door 2.
        self.door3.config(text="Door 3", command=self.choose_door_3) #Change the text of Button/Door 3 to say Door 3.
        self.label2.config(text="Choose one of three doors") #Change label 2 to prompt user to choose one of three doors.
        self.game_saved = False #Set the game saved boolean to False because the game has not been saved yet.
    
    def submit_door(self, dn:int): #Submit door function.
        if self.first_goat_found == False and self.game_finished == False: #If the user is choosing one door for the first time.
            self.game_playing = True #Set the boolean variable where the game is ongoing to True.
            goat_door = random.randint(1,3) #Choose a random unchosen Door for the host to open.

            while goat_door == dn or goat_door == self.prize_location: #While the Door is not a door that the user chose, nor the one that contains a prize.
                goat_door = random.randint(1,3) #Choose another Door.

            if goat_door == 1: #If the first goat is in Door 1.
                self.door1.config(text="Goat", command=self.null_command) #Tell the user the Door contains a Goat, and change the button command to null in case they accidentally select this Door.
            elif goat_door == 2: #Otherwise, if the first goat is in Door 2.
                self.door2.config(text="Goat", command=self.null_command) #Tell the user the Door contains a Goat, and change the button command to null in case they accidentally select this Door.
            elif goat_door == 3: #Otherwise, if the first goat is in Door 3.
                self.door3.config(text="Goat", command=self.null_command) #Tell the user the Door contains a Goat, and change the button command to null in case they accidentally select this Door.

            self.first_goat_found = True #Set the boolean variable where the first Goat was found to True.
            self.previous_door = dn
            self.label2.config(text=f"A goat was found in Door {goat_door}.\nChoose the second door.") #Change the second label to inform the user about the first Goat's location, and prompt them to choose another Door.

        elif self.first_goat_found == True and self.game_finished == False: #Otherwise, if the fist Goat was already found and the game is not finished.
            self.game_finished = True #Set the boolean variable where the game is finished to True.
            self.game_playing = False #Set the boolean variable where the game is ongoing to False.

            if self.prize_location == 1: #If the prize was found in the first Door.
                self.door1.config(text="Prize") #Tell the user the Door contains the Prize.
                self.door2.config(text="Goat") #Tell the user the Door contains a Goat.
                self.door3.config(text="Goat") #Tell the user the Door contains a Goat.
            elif self.prize_location == 2: #Otherwise, if the prize was found in the second Door.
                self.door1.config(text="Goat") #Tell the user the Door contains a Goat.
                self.door2.config(text="Prize") #Tell the user the Door contains the Prize.
                self.door3.config(text="Goat") #Tell the user the Door contains a Goat.
            elif self.prize_location == 3: #Otherwise, if the prize was found in the third Door.
                self.door1.config(text="Goat") #Tell the user the Door contains a Goat.
                self.door2.config(text="Goat") #Tell the user the Door contains a Goat.
                self.door3.config(text="Prize") #Tell the user the Door contains the Prize.

            if dn == self.prize_location: #If the user guessed correctly about the prize's location.
                self.label2.config(text=f"Congratulations!\nYou found the prize!") #Congratulate the user.
                if self.previous_door == dn: #If the user stayed with the previous door.
                    self.ws += 1 #Increment the number of times the user stayed with their previous door and won.
                else: #Otherwise.
                    self.ww += 1 #Increment the number of times the user switched doors and won.
            else: #Otherwise.
                self.label2.config(text=f"Sorry!\nThe prize was in Door {self.prize_location}") #Tell the user they guessed wrong.
                if self.previous_door == dn: #If the user stayed with the previous door.
                    self.ls += 1 #Increment the number of times the user stayed with their previous door and lost.
                else: #Otherwise.
                    self.lw += 1 #Increment the number of times the user switched doors and lost.

            self.reset_button = tk.Button(self.root, text="Click To\nPlay Again", font=('Arial', 18), command=self.reset) #Generate contents for the reset button.
            self.reset_button.pack(padx=10, pady=0) #Generate the reset button by using the pack function.
        self.game_saved = False #Set the game saved boolean to False because the game has not been saved yet.

    def choose_door_1(self): #Choose Door 1 Function.
        self.submit_door(1) #Choose Door 1 as the inital Door.

    def choose_door_2(self): #Choose Door 2 Function.
        self.submit_door(2) #Choose Door 2 as the inital Door.

    def choose_door_3(self): #Choose Door 3 Function.
        self.submit_door(3) #Choose Door 3 as the inital Door.

    def null_command(self): #Null command to replace when a Door was initially chosen.
        pass #Do nothing.

    def on_closing(self): #Before the user quits, ask them if they want to quit in the case they haven't saved.
        if self.game_saved == False: #If the statistics have not been updated yet.
            if messagebox.askyesno(title="Quit?", message="You haven't saved the statistics yet.\nAre you sure you want to quit?"): #Prompt the user if they want to quit.
                self.root.destroy() #Quit the program if they answer Yes.
        else: #Otherwise.
            self.root.destroy() #End the program.

MontyHall() #Call the function to run the program.