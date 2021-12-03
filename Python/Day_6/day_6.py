import re
import numpy as np

print("Advent Of Code - Day 6")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

regex_pattern = r"([a-z,\s]+) ([0-9]+),([0-9]+) ([a-z]+) ([0-9]+),([0-9]+)"

## Control lights, fits both Part 1 and Part 2
def control_light_grid(light_array,x_from,x_to,y_from,y_to,command_from,use_brightness):
    for x in range(x_from,x_to+1):
        for y in range(y_from,y_to+1):
            if command_from == 'on':
                if use_brightness:
                    light_array[x,y] += 1;
                else:
                    light_array[x,y] = 1;
            elif command_from == 'off':
                if use_brightness:
                    if light_array[x,y] > 0:
                        light_array[x,y] -= 1;
                else:
                    light_array[x,y]=0
            elif command_from == 'toggle':
                if use_brightness:
                    light_array[x,y] += 2
                else:
                    light_array[x,y] = 1 - light_array[x,y];

def run_light_commands(commands, use_brightness):
    light_array = np.zeros((1000, 1000))

    for line in commands:
        match = re.match(regex_pattern,line)
        command_from = str(match.group(1)).replace('turn ','')
        x_from = int(match.group(2))
        y_from = int(match.group(3))
        x_to = int(match.group(5))
        y_to = int(match.group(6))
        control_light_grid(light_array,x_from,x_to,y_from,y_to,command_from,use_brightness)    
    
    return light_array
    
def count_lights_on(ligths):
    unique, counts = np.unique(ligths, return_counts=True)    
    return counts[1]

def get_total_brightness(ligths):
    total_brightness = np.sum(ligths)    
    return total_brightness
    

lights_p1 = run_light_commands(PUZZLEINPUT,False)
lights_p2 = run_light_commands(PUZZLEINPUT,True)

print(f'Part 1: {count_lights_on(lights_p1)} lights are on')
print(f'Part 2: Total Brightness is {int(get_total_brightness(lights_p2))}')