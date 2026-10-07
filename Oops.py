#  all OOP Concepts in One File
#Object Oriented programming

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

p1 = Person("Yogesh", 21)
p1.introduce()


# 2. Inheritance
class Animal:
    def speak(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

Dog().speak()
Cat().speak()


# 3. Polymorphism
class Bird:
    def move(self):
        print("Bird flies in the sky.")

class Fish:
    def move(self):
        print("Fish swims in water.")

def show_movement(creature):
    creature.move()

show_movement(Bird())
show_movement(Fish())


# 4. Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Balance:", account.get_balance())


# 5. Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car engine starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a kick.")

Car().start()
Bike().start()
