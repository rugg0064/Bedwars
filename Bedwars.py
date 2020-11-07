from os import system
from math import ceil
import sys
import os
def contains(list1,string1):
	string1 = string1.upper()
	for i in list1:
		if i==string1:
			return True
		else:
			continue
	return False
def convert(l1):
	converted = []
	for i in l1:
		for l in range(len(alias)):
			if contains(alias[l],i):
				converted.append(alias[l][0])
				continue
	return converted

alias = [["WOOL","WO", "W"],
["CLAY","C","CL"],
["WOOD","WD"],
["GLASS","G"],
["ENDSTONE","E","END"]]

blocks = []
system('cls')
while (usr:=input("Wool - W\nClay - C\nWood - Wd\nGlass - G\nEndstone - E\nBlock: ").upper()) !="":
	system('cls')
	blocks.append(usr)
blocks = convert(blocks)

def calcblocks(layer):
	if layer<0:
		return 0
	else:
		#print("in this")
		return (6+((layer-1)*4)) + calcblocks(layer-1)

#Name, Q, P, Iron/Glass (1/0)
blockprices = [["WOOL",16,4,0],
["CLAY", 16, 12, 0],
["WOOD", 16, 4, 1],
["GLASS",4,12,0],
["ENDSTONE",12,24,0]]
print("N BLOCK     AMNT PRICE CURRENCY")
totalpriceiron = 0
totalpricegold = 0
for i in range(len(blocks)-1,-1,-1):
	output = ("%s" % str(i+1)) + " "*(3-len(str(i+1)))
	output = output + "%s" % blocks[i] + " "*(10-len(blocks[i]))
	amount = calcblocks(i+1)
	output = output + str(amount) + " "*(4-len(str(amount)))
	for j in range(len(blockprices)):
		if blocks[i] == blockprices[j][0]:
			cost = ceil(amount/blockprices[j][1])*blockprices[j][2]
			output = output + str(cost) + (" "*(4-len(str(cost))))
			if blockprices[j][3]==0:
				output = output + "Iron"
				totalpriceiron = totalpriceiron + cost
			else:
				output = output + "Gold"
				totalpricegold = totalpricegold + cost
	print(output)
print("total ironx:", totalpriceiron)
print("total gold:", totalpricegold)
input()