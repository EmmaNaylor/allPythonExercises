from random import randint

# # MVP - generates 6 random numbers and stores them in a set (to prevent duplicates)
#
# result = set()
# draw = 0
#
# while len(result) < 6:
#     draw = randint(1, 50)
#     result.add(draw)
# print(*result, sep=' ', end=' ')

# Upgraded version:
# Generates 6 random numbers and stores them in a set to create your lucky dip ticket.
# Generates a different set of 6 random numbers to create the lotto result.
# As each lotto number (draw) is defined a comparison is run to check if draw is in list
#     If yes - the loop is skipped.
#     If no - the number is announced as well as a 'doh'/'yay' depending on whether there is a match to your luckydip
#         matches variable also +1 so that final matches can be counted
# When length of results reaches 6 the final numbers are announced
# The total matches between your luckydip and the results are confirmed
# Your prize is confirmed based on number of matches

luckyDip = set()

while len(luckyDip) < 6:
    dip = str(randint(1, 50))
    luckyDip.add(dip)

result = set()
drawRemain = 0
draw = 0
prize = ["Nada", "a lucky dip for the next game!", "£200", "£3500", "£2.9million"]
matches = 0

print("\nIt's time for tonight's lotto draw! \n")
print(f"Tonight's lucky winners will receive their share of £{prize[-1]}! \n")
print("You clutch your ticket to your chest... your luckyDip numbers for tonight are:")
print(*luckyDip, sep=' ', end=' ')
print("\n\n\n ********** The draw begins! **********\n")

while len(result) < 6:

    draw = str(randint(1, 50))
    if draw in result:
        continue
    else:
        print(f"The next ball is... {draw}!")
        result.add(draw)
        if draw in luckyDip:
            print("Yay!")
            matches += 1
        else:
            print("Doh!")

print("\nSo... in no particular order... tonight's lucky numbers are:")
print(*result, sep=' ', end=' ')

if matches == 0:
    print(f"\n\nYou got {matches} matches - better luck next time!")
elif matches < 6:
    print(f"\n\nNice! you got {matches} matches - you've won...{prize[matches]}!")
else:
    print(f"You did it! You're tonight's jackpot winner! You've won {matches}")
print("\nI look forward to seeing you at the next draw!")
