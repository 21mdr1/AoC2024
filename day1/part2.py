input = open("../input/test/test-input1.txt", "r").read()

left_list = [ int(x.split("   ")[0]) for x in input.split("\n") ]
right_list = [ int(x.split("   ")[1]) for x in input.split("\n") ]

right_appearances = dict()

for id in right_list:
    right_appearances[id] = right_appearances.get(id, 0) + 1

similarity_score = sum([ x*right_appearances.get(x, 0) for x in left_list ])

print(similarity_score)