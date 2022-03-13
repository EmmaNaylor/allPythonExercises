from person import Person


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



