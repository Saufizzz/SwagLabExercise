# SyntaxError
# IndentationError

# This line of code will take an input using the input() function
# print("Hello " + input("What is your name") + "!")
#
# name = input("What is your name?")
# print("Hi " + name + "!")
# print(len(name))
#
# username = input("What is your username")
# length = len(username)
# print(username, length)
#
#

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? \n $"))
tips = int(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill?\n"))
total_amount = total_bill * (tips/100 + 1.0) / people
print(round(total_amount, 2))



#Pizza

print("welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L?")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
price = 0

if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price += 3
else:
    print("No size available")

if extra_cheese == "Y":
    price += 1

print(f"Total amount you have to pay: ${price}")






