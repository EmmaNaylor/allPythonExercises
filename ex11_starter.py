#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

# HYPHENS LENGTH OF BELGIUM STRING - OPTION 1
print("-" * len(Belgium))

# # HYPHENS LENGTH OF BELGIUM STRING - OPTION 2 - (LESS EFFICIENT)
# hyphens = ""
# for character in Belgium:
#     hyphens += "-"
# print(hyphens)

# REPLACE COMMAS WITH COLONS - OPTION 1
colonBelgium = Belgium.replace(",", ":")
print(colonBelgium)

# REPLACE COMMAS WITH COLONS - OPTION 2 (LESS EFFICIENT)

# belgList = Belgium.split(",")
# belgColon = ":".join(belgList)
# print(belgColon)

# SECOND FIELD + FOURTH FIELD IN STRING ADDED TOGETHER

belgList = Belgium.split(",")
combinedPopulation = int(belgList[1]) + int(belgList[3])
print(combinedPopulation)

