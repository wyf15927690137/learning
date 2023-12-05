class Person:
    def __init__(self, name):
        self.name = name

    def myprint(self):
        print(self.name)


class Person1(Person):
    def __init__(self, age):
        self.age = age

    # def myprint(self):
    #     print(self.name, self.age)

    def myprint(self):
        print(self.age)


class Person2(Person):
    def __init__(self, name, age):
        self.age = age
        # use super() initialize the constructor of superclass, the subclass will inherit the property of superclass
        super().__init__(name)

    def myprint(self):
        print(self.name, self.age)


p1 = Person("A")
p1.myprint()

p3 = Person2("c", 12)
p3.myprint()

# p2 = Person1("B", 15)
p2 = Person1(15)
p2.myprint()
