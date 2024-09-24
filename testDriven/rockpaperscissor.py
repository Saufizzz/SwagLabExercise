import random

game = ["Rock", "Paper", "Scissor"]

user_choice = input("what is your choice? \n"
                    "Rock \n"
                    "Paper \n"
                    "Scissor")
computer_choice = random.choice(game)
print(computer_choice)

if user_choice == "Rock":
    if computer_choice == "Scissor":
        print("user wins")
    elif computer_choice == "Paper":
        print("user loses")
    elif computer_choice == "Rock":
        print("tie")
if user_choice == "Paper":
    if computer_choice == "Scissor":
        print("user loses")
    elif computer_choice == "Paper":
        print("tie")
    elif computer_choice == "Rock":
        print("user win")
if user_choice == "Scissor":
    if computer_choice == "Scissor":
        print("tie")
    elif computer_choice == "Paper":
        print("user win")
    elif computer_choice == "Rock":
        print("usr loses")



