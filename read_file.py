# Open file to read - longer way by reading all characters into an open file
# openFile = open("pelican.txt", "r")
#
# readAllChars = openFile.read()
# print(type(readAllChars))
# print(readAllChars)
#
# openFile.close()

print("\n\n")

# Open file - shorter way to read the whole file into a string
lines = open("pelican.txt").read()
print(type(lines))  #data type is str
print(lines)
print("\n\n")

# Split the whole file into a string and create a list from it
splitLines = open("pelican.txt").read().splitlines()
print(splitLines)
print(len(splitLines))
print("\n\n")

# # # Produce a list but new line (\n) characters remain
# lineList = open("pelican.txt").readlines()
# print(lineList)
# print("\n\n")
#
with open("pelican.txt", "r") as openFile:
    for line in openFile:
        print(line, end="")

