input = open("../input/input1.txt", "r").read() # string

list1 = sorted([int(x.split("   ")[0]) for x in input.split("\n")])
list2 = sorted([int(x.split("   ")[1]) for x in input.split("\n")])

difference = sum([ abs(list1[i] - list2[i]) for i in range(len(list1)) ])
print(difference)