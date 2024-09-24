#list is datatype that allows multiple values and can combine different datatype
fruit = ["banana", " watermelon", "papaya"]
print([fruit[1]])
print(fruit[1:3]) # the latter index will only shows the previous index number values
fruit.insert(4, "durian") # need to insert (index number, value)
fruit[1] = "strawberry" #update value by assigning index number to the variable
fruit.append("coconut") #add value at the end of the list
del fruit[0] #delete values
print(fruit)

#tuple is dataype that works exactly the same as list but it is immutable(unable to change/update)

game = ("Final Fantasy IV","Final Fantasy IX","Final Fantasy X")
print(game[1])
#game.append["Final Fantasy XX"] (this will show error that tuple object has no attribute append)


#dictionary is dataype that involves key:value pair
address = {"saufi" : "kajang", "syuhada" : "langkap", 3 : "bangi", "duwe" : 4}
print(address[3])
print(address["syuhada"])

#building empty dictionary

dict = {}
dict["first_name"] = "Muhammad"
dict["last_name"] = "Saufi"
dict["father_name"] = "Shaharudin"
dict["mother_name"] = "Sharifah"
print(dict["first_name"])