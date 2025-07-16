class Addition:
    first = 0
    second = 0
    answer = 0

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def display(self):
        print("First number is :" + str(self.first))
        print("Second number is :" + str(self.second))
        print("Sum of 2 numbers :" + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second


obj1 = Addition(30, 50)

obj2 = Addition(45, 69)

obj1.display()
obj1.calculate()

obj2.display()
obj2.calculate()
