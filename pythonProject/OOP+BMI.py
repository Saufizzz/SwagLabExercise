#How to construct constructors
# Class Variables are variable which created under class
#Instances variable are created inside a method

class BMI:
    # self variable parameters are mandatory all the time when you declare a method inside a class.
    # when we added 2 arguments during runtime/obj creation, we must match with the constructor num of parameters specified
    #Basically create a blueprint of BMI.
    #Constructor needs parameter which will we used for argument for object creation
    

    def __init__(self, weight, height):
         self.weight = weight
         self.height = height

    def BMI_Calc(self):
        BMI_Calc = self.weight / (self.height / 100) ** 2
        return BMI_Calc

    def person(self):
        name = input("What is your name")
        result = f"{name}, your BMI is : {self.BMI_Calc()}"
        return result

obj = BMI(56,160)
obj2 = BMI(70,160)
result1 = obj.person()
result2 =obj2.person()
print(result1,result2)