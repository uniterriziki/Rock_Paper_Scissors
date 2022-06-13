import random
print(" Rock paper scissors game between User 'you' vs Computer \n Rules:Rock vs Paper-paper wins,Paper vs Scissors-scissors wins,Rock vs Scissors-Rock wins, if players make same choice, it is a tie.")
            
p = ["R", "P", "S"]
player = False
while player == False:
    print("Pick one: R for Rock, P for Paper, or S for Scissors")    
    choice = input("you choose: ")    
    if choice == "R":
        choice_name = 'Rock'
    elif choice == "P":
        choice_name = 'Paper'
    elif choice == "S":
        choice_name = 'Scissors'
    else:
        print("Not a valid choice. Check your input and try again")
        print(input("Click 'Enter' to try again")) 
        choice = input("You chose: ")
        player = False

        if choice == "R":
            choice_name = 'Rock'
        elif choice == "P":
            choice_name = 'Paper'
        elif choice == "S":
            choice_name = 'Scissors'    
    print("user choice is: " + choice_name)       
    computer_choice = random.choice(p)    
    if computer_choice== "R":
        computer_choice_name = 'Rock'
    elif computer_choice == "P":
        computer_choice_name = 'Paper'    
    else:
        computer_choice_name = 'Scissors'
    print("Computer choice is: " + computer_choice_name + "\n " )
    print(choice_name + " v/s " + computer_choice_name + "\n")   
   
    if choice == computer_choice:
        print("Both players selected"  " "+ choice_name +". It's a tie!!" + "Play again " +"\n")
    elif choice == "R":
        if computer_choice == "P":
            print("You lose!", computer_choice_name, "covers", choice_name , end = "\n")
            result = "Paper"
        else:
            print("You win!", choice_name, "smashes", computer_choice_name, end = "\n" )
    elif choice == "P":
        if computer_choice == "S":
            print("You lose!", computer_choice_name, "cut", choice_name)
            result = "Scissors"
        else:
            print("You win!", choice_name, "covers", computer_choice_name)
    elif choice == "S":
        if computer_choice == "R":
            print("You lose...", computer_choice_name, "smashes", choice_name)
            result = "Rock"
        else:
            print("You win!", choice_name, "cut", computer_choice_name)       
    
    print("Do you want to play again? (Y/N)")
    ans = input()    
    if ans == 'n' or ans == 'N':
            break

