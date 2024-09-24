# object oriented programming

class Dog:

    def Bark(self):
        print("bark")

    def meow(self):
        return "meow"


d = Dog()   # create instance
d.Bark()    # method inside class
print(d.meow())

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name, age)

    def getname(self):  #retrieve name function
        return self.name
    def getage(self):   #retrieve age function
        return self.age
    def setage(self,age):   #modify the age
        self.age = age


saufi = Person("Saufi", 25)
Syuhada = Person("Syu",24)
print(Syuhada.getage())
Syuhada.setage(25)
print(Syuhada.getage())

