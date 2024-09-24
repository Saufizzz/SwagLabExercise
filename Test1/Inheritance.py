#inheritance is acquiring properties of parent class
# same concept as epic and user stories e.g epic is parent and user stories is child
from OOps import calculator, WeightCalculator


class Child(calculator):
    num2 = 200

    def __init__(self):
        calculator.__init__(self,10,10)

    def GetCompleteData(self):
        return self.num2 + self.num + self.calculate()


class ChildBMI(WeightCalculator):
    def __init__(self):
        WeightCalculator.__init__(self, 53, 1.6)

    def GetCompleteBMI(self):
        return self.bmi()

obj = Child()
print(obj.GetCompleteData())

obj1 = ChildBMI()
print(obj1.GetCompleteBMI())