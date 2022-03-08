class Cat:
    name = ""
    colour = ""
    fav_toy = ""

    def __init__(self, name, colour, breed):
        self.name = name
        self.colour = colour
        self.breed = breed

    def make_sound(self):
        if self.breed == "Siamese":
            print("Meooooooow!")
        else:
            print("Mee-ooo-w!")
