class Person:

    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age

    def introduce(self):
        print(f"I am {self._name}")

    def state_gender(self):
        print(f"I am {self._gender}")

    def state_age(self):
        print(f"I am {self._age} years old")

    def walk(self):
        print("I am walking")
