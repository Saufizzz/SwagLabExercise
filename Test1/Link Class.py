class Robot():
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def IntroduceYourself(self):
        print("My name is " + self.name)
        print("My color is " + self.color)
        print("I am " + str(self.age) + " years old ")

r1 = Robot("tom", "red", 30)
r2 = Robot("jerry", "blue", 40)

r1.IntroduceYourself()
r2.IntroduceYourself()

class Person():
    def __init__(self,n , p , c):
        self.name = n
        self.personality = p
        self.condition = c

    def eating(self):
        self.condition = True

    def not_eating(self):
        self.condition = False

p1 = Person("Saufi", "handsome", True)
p2 = Person("Syuhada", "slim", False)

p1.robot_owned = r1 #use previous object to link with current object
p1.robot_owned.IntroduceYourself()