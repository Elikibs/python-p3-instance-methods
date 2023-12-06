#!/usr/bin/env python3

class Person:
    # Class body goes here
    def __init__(self, name):
        self.name = name

    #Instance method definition
    def talk(self):
        print("Hello World!")

    def walk(self):
        print(f"{self.name} is walking")

elisha = Person("Elisha")
elisha.talk()
elisha.walk()
