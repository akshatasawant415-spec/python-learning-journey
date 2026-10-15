class Animal:
    def eat(self):
        print("Bread")
class Dog(Animal):
    pass
d=Dog()
d.eat()

class Animal:
    def eat(self):
        print("Bread")
class Dog(Animal):
    def bark(self):
        print("WOW!!")
d=Dog()
d.eat()
d.bark()

class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print("Car started")
class Car(Vehicle):
    def __init__(self, brand,model):
        super().__init__(model)
c=Car("Toyota","corolla")
print(c)
c.start()

class Parent:
    def start(self):
        print("Vehicle stared")
class Child(Parent):
    def start(self):
        print("BMW started")
c=Child()
c.start()

