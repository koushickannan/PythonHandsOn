class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name : " , self.name)
        print("Age : " , self.age)


class Employee(Person):
    def __init__(self, name, age, role, state):
        self.role = role
        self.state = state

        Person.__init__(self, name, age)

        print("Role : ", self.role)
        print("State : ", self.state)


a = Employee("Davis", 35, "QA", "Dallas")
a.display()
