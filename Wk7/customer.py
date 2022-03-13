from person import Person


class Customer(Person):

    def __init__(self, name, gender, age, task, product):
        Person.__init__(self, name, gender, age)
        self._task = task
        self._product = product

    def __str__(self):
        return f"Hi, I'm {self._name}, I'm looking to {self._task} some {self._product}"

    def ask_for_help(self):
        if self._task == "return":
            print(f"Please can someone tell me where I can return my {self._product}?")

        elif self._task == "buy":
            print(f"Please can you tell me where I can find some {self._product}")

        else:
            print("Looks like I came to the wrong place...")

