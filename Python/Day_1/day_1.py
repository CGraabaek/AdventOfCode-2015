from collections import Counter
print("Advent Of Code - Day 1")

PUZZLEINPUT = open('input.txt', 'r').read()
## Part 1
b = Counter(PUZZLEINPUT)
up = b.get('(')
down = b.get(')')

total = up - down
print("Part 1: " + str(total))

# Part 2
floor = 0
for idx, char in enumerate(PUZZLEINPUT):
    if char == '(':
        floor += 1
    else:
        floor -= 1

    if(floor == -1):
        print("Part 2: " + str(idx+1))
        break
    