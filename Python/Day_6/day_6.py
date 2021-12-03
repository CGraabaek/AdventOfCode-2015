import re
import numpy as np

print("Advent Of Code - Day 6")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

regex_pattern = r"([a-z,\s]+) ([0-9]+),([0-9]+) ([a-z]+) ([0-9]+),([0-9]+)"

light_array = np.zeros((1000, 1000))

for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)
    command_from = str(match.group(1)).replace('turn ','')
    x_from = int(match.group(2))
    y_from = int(match.group(3))
    x_to = int(match.group(5))
    y_to = int(match.group(6))
    
    for x in range(x_from,x_to+1):
        for y in range(y_from,y_to+1):
            if command_from == 'on':
                light_array[x,y] = 1;
            elif command_from == 'off':
                light_array[x,y] = 0;
            elif command_from == 'toggle':
                light_array[x,y] = 1 - light_array[x,y];
            

unique, counts = np.unique(light_array, return_counts=True)
print(dict(zip(unique, counts)))

print(f'Part 1: {counts[1]} lights are on')