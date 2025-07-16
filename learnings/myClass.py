class myClass:
    def __int__(self):
        self.my_attr = 10


obj1 = myClass()
obj2 = myClass()
obj2.my_attr = "35"
obj1.my_attr = obj2.my_attr + "20"

print(obj1.my_attr)
