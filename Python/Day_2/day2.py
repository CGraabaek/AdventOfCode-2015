import re
print("Advent Of Code - Day 2")

PUZZLEINPUT = open('input.txt', 'r').readlines()
match = regex_pattern = r"([0-9]+)x([0-9]+)x([0-9]+)"
total = 0
ribbon_total = 0

for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)
    l = int(match.group(1))
    w = int(match.group(2))
    h = int(match.group(3))

    extra = min((2*l*w)/2 , (2*w*h)/2, (2*h*l)/2)
    total += 2*l*w + 2*w*h + 2*h*l + extra
    
    ribbon_array = []
    ribbon_array.append(l)
    ribbon_array.append(w)
    ribbon_array.append(h)
    
    ribbon_array.sort()
    ribbon = 2*ribbon_array[0]+2*ribbon_array[1]
    bow = l*w*h

    ribbon_total += ribbon + bow

print("Part 1: " + str(total))
print("Part 2: " + str(ribbon_total))