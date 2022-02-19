# Open and append to a file called pelican.txt (txt is auto so does not need to be defined)
openFile = open("pelican.txt", "a")

# Append a line to the file using the write method
firstLine = openFile.write("A wonderful bird is the pelican,\n")
# Append a second line to the file using the write method
secondLine = openFile.write("His bill holds more than his belican.\n")

# Append a llist to the file using the writelines method
moreAddedLines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
openFile.writelines(moreAddedLines)

# \n are required to create new lines between each file of the poem (affects the layout of the txt document)

openFile.close()
