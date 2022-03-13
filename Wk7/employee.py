from person import Person


class Employee(Person):

    def __init__(self, name, gender, age, role, shift):
        Person.__init__(self, name, gender, age)
        self._role = role
        self._shift = shift

    def state_role(self):
        print(f"I am a {self._role}")

    def __len__(self):
        return self._age - 18

    def length_of_service(self):
        sl = len(self)
        print(f"I have been working here for around {sl} years")

    def hours(self):
        print(f"I work {self._shift}")

    def on_duty(self):
        from check_time import check_shift
        hours = check_shift()
        if hours == self._shift:
            print("I'm on duty")
        else:
            print("Sorry I'm off duty, I can't help you right now")


    def tasks(self):

        if self._role == "cleaner":
            skills = ("clean",)
        elif self._role == "checkout worker":
            skills = ("check out your items", "run price checks")
        elif self._role == "shelf stacker":
            skills = ("stack the shelves", "rotate our stock")
        elif self._role == "customer service assistant":
            skills = ("help with whatever you need",)
        else:
            skills = ""
        print("I can " + (' and '.join(x for x in skills)))

    def __str__(self):
        return f"Hi! My name's {self._name}, I'm a {self._role}"

