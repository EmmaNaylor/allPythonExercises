class Person:

    def __init__(self, name, gender, age):
        self._name = name
        self._gender = gender
        self._age = age

    def _name(self):
        return self._name

    def introduce(self):
        print(f"I am {self._name}")

    def state_gender(self):
        print(f"I am {self._gender}")

    def state_age(self):
        try:
            self._age + 1
        except TypeError as err:
            print("------------ :( --------------")
            print(f"Oops, something went wrong when you called: state_age(self). "
                  f"Please enter {self._name}'s age as a number. The error was captured as: {err}")

    def breathe(self):
        print("I am breathing")

    @property
    def nick_name(self):
        """Set a new name"""
        print(self._name)
        return self._name

    @nick_name.setter
    def nick_name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        print(self._age)
        return self._age

    @property
    def gender(self):
        print(self._gender)
        return self._gender
