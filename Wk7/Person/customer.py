from person import Person
from random import randint


class Customer(Person):

    def __init__(self, name, gender, age, task, product):
        Person.__init__(self, name, gender, age)
        self.task = task
        self.product = product

    def __str__(self):
        return f"Hi, I'm {self._name}, I'm looking to {self.task} some {self.product}"

    def ask_for_help(self):
        if self.task == "return":
            print(f"Please can someone tell me where I can return my {self.product}?")

        elif self.task == "buy":
            print(f"Please can you tell me where I can find some {self.product}")

        else:
            print("Looks like I came to the wrong place...")

    def browse(self):
        for i in range(0, 3):
            print("I am browsing")
        print("I always browse thrice in case of items hidden at the back...")

    def __len__(self):
        return randint(2, 61)

    def length_of_wait(self):
        wait = len(self)
        print(f"I have been waiting here for {wait} minutes! Please can I get some service!")
