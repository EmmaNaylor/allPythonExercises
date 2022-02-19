from random import randint

# MVP - generates 6 random numbers and stores them in a set (to prevent duplicates)

result = set()
draw = 0

while len(result) < 6:
    draw = randint(1, 50)
    result.add(draw)
print(*result, sep=' ', end=' ')
