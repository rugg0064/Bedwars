from os import system
from math import ceil

def findBlockTable(alias):
	for blockTable in blockPrices:
		for tableAlias in blockTable[1]:
			if(tableAlias == alias):
				return blockTable
	return None

#Name, Aliases, Q, P, Iron/Gold/Emerald (0/1/2)
blockPrices = [
	["WOOL", ["WOOL","WO", "W"], 16, 4, "Iron"],
	["CLAY", ["CLAY","C","CL"], 16, 12, "Iron"],
	["WOOD", ["WOOD","WD"], 16, 4, "Gold"],
	["GLASS", ["GLASS","G"], 4, 12, "Iron"],
	["ENDSTONE", ["ENDSTONE","E","END"], 12, 24, "Iron"],
	["OBSIDIAN", ["OBSIDIAN", "O"], 4, 4,"Emerald"]
]

blocks = []
system('cls')

usr = " "
while (usr==" " or usr.upper() != ""):
	for a in blockPrices:
		for i, b in enumerate(a[1]):
			print(b, end = "")
			if(i <= len(a[1])-2):
				print(" - ", end = "")
		print()
	usr = input("").upper()
	if(block := findBlockTable(usr)):
		blocks.append(block)
	system('cls')

def calcBlocks(layer):
	if layer<0:
		return 0
	else:
		return (6+((layer-1)*4)) + calcBlocks(layer-1)

print("(Individual prices don't carry to a second layer)")
blockCounts = [0] * len(blockPrices)
for k, block in enumerate(blocks):
	i = k + 1
	blockCountIndex = None
	for j, blockTable in enumerate(blockPrices):
		if(block == blockTable):
			blockCountIndex = j
	amount = calcBlocks(i)
	blockCounts[blockCountIndex] += amount
	individualPrice = ceil(amount / block[2]) * block[3]
	print("%s - %4d blocks - %s %s" % (block[0].ljust(8," "), amount, individualPrice, block[4]))


totalPrices = {}
print("Total prices (including carry over)")
for i in range(0, len(blockCounts)):
	table = blockPrices[i]
	cost = ceil(blockCounts[i] / table[2]) * table[3]
	if(cost > 0):
		resource = blockPrices[i][4]
		if(not resource in totalPrices.keys()):
			totalPrices[resource] = cost
		else:
			totalPrices[resource] += cost
	
for key in totalPrices.keys():
	print("%s - %d" % (key.ljust(7, " "), totalPrices[key]))
input()