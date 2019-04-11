import re
print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt', 'r').readlines()
match = regex_pattern = r"([0-9]+)x([0-9]+)x([0-9]+)"
total = 0

for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)
    l = int(match.group(1))
    w = int(match.group(2))
    h = int(match.group(3))

    extra = min((2*l*w)/2 , (2*w*h)/2, (2*h*l)/2)
    total += 2*l*w + 2*w*h + 2*h*l + extra

print("Part 1: " + str(total))