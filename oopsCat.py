# create a new Class for Cat using the code we created in the classroom, add a method called
# 'makeSound' which will print out 'meow meow' into the terminal

from oopsCode import Cat

firstKitty = Cat("Kit-Kat", "white", "Tabby")
breed = firstKitty.breed
name = firstKitty.name
colour = firstKitty.colour
print(f"This is {name}, she's a {colour} {breed} cat!")
firstKitty.make_sound()

secondKitty = Cat("Jasper", "brown", "Siamese")
breed = secondKitty.breed
name = secondKitty.name
colour = secondKitty.colour
print(f"This is {name}, she's a {colour} {breed} cat!")
secondKitty.make_sound()
