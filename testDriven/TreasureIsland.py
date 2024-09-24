print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

first_Step = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' \n").lower()
if first_Step == "right":
    print("You fell into a hole. Game Over")
elif first_Step == "left":
    second_Step = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for "
                        "a boat or 'swim' to swim across \n").lower()
    if second_Step == "swim":
        print("You are eaten by sharks. Game Over")
    elif second_Step == "wait":
        third_Step = input("You arrive at the island unharmed. There is a house with 3 doors. \n "
                           "One red, One yellow and one blue. Which colour do you choose? \n").lower()
        if third_Step == "red":
            print("you have entered a red witch house. Game Over!")
        elif third_Step == "blue":
            print("You are trapped in the blue house. Game Over!")
        elif third_Step == "yellow":
            print("You have found the treasure. Congratz")
        else:
            print("You have chosen the wrong path. Game Over")
    else:
        print("Your choice is not listed. Game Over")
else:
    print("Your choice is not listed. Game Over")











