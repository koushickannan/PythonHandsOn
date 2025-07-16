class myClass:

    def __init__(self, name=None):
        if name is None:
            print("Default constructor called")
        else:
            self.name = name
            print("The name is :" + self.name)

    def method(self):
        if hasattr(self, 'name'):
            print("Method called with name : " + self.name)
        else:
            print("Method called without name")


obj1 = myClass()
obj1.method()

obj2 = myClass("Ava")
obj2.method()
