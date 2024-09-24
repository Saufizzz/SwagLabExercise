# class are user defined blueprint prototype
# e.g calculators need have sum, multiplication, subtraction, constant operation
# class will have methods, class variable, instance variable, constructor
# object for your classes
# must called object class and variable outside of the class
# basically function when used in class called methods
# self keyword is mandatory for calling variable names into methods
# instance and class variable havve whole different purposes
# constructor name should be __init__



class calculator:
    num = 100 # class variable which is constant3
# what is self? -method which automatically called when created object for any class
# constructor must start with def __init__

    def __init__(self, a, b):
        self.firstNum = a
        self.secondNum = b
        print(" I am called automatically when object is created ")


    def getData(self):
        print(" I am now executing as method in class ")

    def calculate(self):
        return self.firstNum + self.secondNum + calculator.num

obj = calculator(2,3)
obj.getData()
print(obj.calculate())

obj1 = calculator(4,5)
obj1.getData()
print(obj1.calculate())


class WeightCalculator():
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def bmi(self):
        return self.weight / (self.height**2)

obj2 = WeightCalculator(53,1.6)
print(obj2.bmi())
