class Cat:
    # property
    color = 'white'

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        print(self.name, "is eating ", self.food)


print(Cat.color)

c = Cat('Tom')
c.eat('fish')
