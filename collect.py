# Example code creates error

# cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke'

# What is wrong with this?
# Each  individual letter in the string 'oke' will create a new list item.
# Resulting in: ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e']

# How should Oke be added at the end of the cheese list?
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += ['Oke']
# OR
cheese.append('Oke')

# How would you add 2 new cheeses to the list with a single command?
cheese.extend(['Red Leicester', 'Brie'])

print(cheese)

tup = 'hello'
print(len(tup))
# print(type(tup))

tup = 'hello',
print(len(tup))
# print(type(tup))

# Issue created as first example lacks a comma - therefore is a string rather than tuple.
# Length of the string is 5 characters / Length of the tuple is 1 item
