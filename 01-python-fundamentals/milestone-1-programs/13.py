#polymorphism
class Animal:
    def sound(self):
        print("Some sound")
class Dog:
    def sound(self):
        print("Woof")
d=Dog()
d.sound()

class Dog:
    def sound(self):
        print("Woof")
class Cat:
    def sound(Self):
        print("Meow")
class Cow:
    def sound(self):
        print("Beep")

things=[Dog(),Cat(),Cow()]
for thing in things:
    thing.sound()

class Payment:
    def pay(self):
        print("pay")
class UPI(Payment):
    def pay(self):
        print("Upi payment")
class CreditCard(Payment):
    def pay(self):
        print("Credit card payment")
Methods=[Payment(),UPI(),CreditCard()]
for method in Methods:
    method.pay()

class Vehicle:
    def start(Self):
        print("vehicle started")
class Car(Vehicle):
    def start(self):
        print("Car started")
class Bike(Vehicle):
    def start(Self):
        print("Bike started")
vehicles=[Car(),Bike()]
for vehicle in vehicles:
    vehicle.start()
