"""
Savannah Obregon
CS 1213
02/26/16
Assignment 36
"""


sticks = int(input("Rules:\nPlayers can only pick up to 3 sticks each turn. The player who picks up the last stick loses!\n\nHow many sticks would you like there to be in the pile? Choose a number between 5 and 50: ")) #ask user for how many sticks

for i in range (sticks):
    if sticks < 5 or sticks > 50: #specify that the number has to be between 5 and 50
        print("That number is not between 5 and 50. Please try again.") #give the user an error message
        sticks = int(input("How many sticks would you like there to be in the pile? Choose a number between 5 and 50: ")) #print new input statement
 
if sticks % 4 == 1: #if the remainder of the user's input divided by 4 is 1...
    print ("You can go first.") #let the user go first 
    while sticks != 0: #while the remainding sticks are not equal to 0
        print (" ") #print empty space
        if sticks == 1: #if the number of sticks is one...
            print ("There is currently", sticks, "stick on the pile.") #print statement for one stick
        else:
            print ("There are currently", sticks, "sticks on the pile.") #print statement for multiple sticks
        print ("Current status of the pile:") #update status of the pile
        for i in range (1, 3): #range for the amount of picks the user can have (1-3 picks)
            for j in range (sticks): #run three times for sticks
                if i > 1:
                    print("|", end="") #print the | symbol for how many sticks
            print ("*", end="") #print a * for beginning and end of pile
        print (" ")#print empty spaces
        print (" ")
        
        #if sticks % 4 == 1:
        pick = int(input("How many sticks would you like to pick up? ")) #ask for user pick
        while pick < 1 or pick > 3 or pick > sticks: #if the users pick is less than 1 or greater than 3 or greater than the amount of sticks in the pile...
            print("Invalid choice. You can choose up to 3 sticks. Please try again.") #print error statemtent for the user
            pick = int(input("How many sticks would you like to pick up? ")) #print new input statement 
        sticks -= pick #update how many sticks are on the pile by saying the number of sticks is the sticks minus user pick
        if sticks == 0: 
            print ("\nYou picked up the last stick. I won!") #print computer winning statement
            break #come out of while loop
        print (" ") #print empty space
        if sticks == 1: #if sticks is 1...
            print ("There is currently", sticks, "stick on the pile.") #print statement for 1 stick
        else:
            print ("There are currently", sticks, "sticks on the pile.") #print statement for multiple sticks
        print ("Current status of the pile:") #update status of the pile
        for a in range (1, 3): #in the range of amount of picks user gets
            for b in range (sticks): #3 time in the range of sticks
                if a > 1: #if sticks is greater than 1
                    print("|", end="") #print | for each stick 
            print ("*", end="") #print * for the pile
        print (" ")#print empty space
        #deciding computer choice
        if sticks % 4 == 0: #if the number of sticks divided by 4 is 0
            comp_pick = 3 #computer pick is 3 sticks
        elif sticks % 4 == 3: #if the number of sticks divided by four has a remainder of 3
            comp_pick = 2 #the computer will choose two sticks
        else:
            comp_pick = 1 #the computer will choose one stick

        if comp_pick == 1: #when the computer pick is 1
            print ("\nI will pick up",comp_pick,"stick.") #print statement for when there is one stick
        else:
            print ("\nI will pick up",comp_pick,"sticks.") #print statement for when there is multiple sticks
        #print (" ") #print empty space
        sticks -= comp_pick #remaining number of sticks
else:
    print ("I will go first.") #print i will go first if user doesn't go first because of number of sticks %4 != 1
    while sticks > 0: #when there are sticks
        print(" ") #print empty space
        if sticks == 1: #when sticks is one
            print ("There is currently", sticks, "stick on the pile.") #print statement for one stick
        else:
            print ("There are currently", sticks, "sticks on the pile.") #print statement for multiple sticks
        print ("Current status of the pile: ") #update the status of the pile
        for a in range (1, 3): #for each item in the three sticks you can pick
            for b in range (sticks): #check to see how many sticks should be displayed
                if a > 1: 
                    print("|", end="") #print how many sticks there are
            print ("*", end="") #print * for pile
        print(" ") #empty space
        if sticks % 4 == 0:#finding the computers pick
            comp_pick = 3
        elif sticks % 4 == 3:
            comp_pick = 2
        else:
            comp_pick = 1

        if comp_pick == 1:
            print ("\nI will pick up",comp_pick,"stick.") #print statement
        else: 
            print ("\nI will pick up",comp_pick,"sticks.") #print statement 
        
        print (" ") #empty space
        sticks -= comp_pick #the number of sticks is now sticks minus the amount the comp_pick
        if sticks == 1:
            print ("There is currently", sticks, "stick on the pile.")
        else:
            print ("There are currently", sticks, "sticks on the pile.") #update status of the pile
        print ("Current status of the pile:")
        for i in range (1, 3): #for each item in the amount of sticks you can pick
            for j in range (sticks): #three times in the range of how many sticks are on the pile
                if i > 1:
                    print("|", end="") #print the amount of sticks on the pile
            print ("*", end="") #print * for the pile

        print (" ")
        print (" ")#print empty space
        pick = int(input("How many sticks would you like to pick up? ")) #get input from the user
        while pick < 1 or pick > 3 or pick > sticks: #if the number they enter is not in the range of sticks or more than amount of picks (3)
            print ("Invalid choice. Please try again.") #print error statement 
            pick = int(input("How many sticks would you like to pick up? ")) #ask for input again
        sticks -= pick #number of sticks is subtracted from user input
        if sticks == 0: #when there are 0 sticks
            print ("\nYou picked up the last stick. I won!") #print winning/ending statement
            break #end of loop





        

        
    
