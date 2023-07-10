import random

user_win = 0
computer_win = 0

option = ["rock", "paper", "scissor"]
while True:
    user_input = input("type rock/paper/scissor  or q for quit ").lower()
    if user_input == "q":
        break
    
    if user_input not in option:
        continue
    
    random_number = random.randint(0,2)
    computer_input = option[random_number]
    print("computer_input is : ", computer_input)
    
    if user_input =="rock" and computer_input =="scissor":
       
        print("You win")
        user_win+= 1
    
    elif user_input == "paper" and computer_input =="rock":
        print("You win")
        user_win+= 1
        
    elif user_input == "scissor" and computer_input == "paper":
        print("You win")
        user_win+= 1
        
    elif (user_input =="rock" and computer_input == "rock") | (user_input== "paper" and computer_input == "paper") | (user_input == "scissor" and computer_input== "scissor"):
        print("draw match")
        
    else:
        print("computer win ")
        computer_win+=1
    
print("you win ", user_win, "games")
print("computer_win", computer_win, "games")
    
    
    
    