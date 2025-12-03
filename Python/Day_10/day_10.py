print("Advent Of Code - Day 10")

PUZZLEINPUT = '1321131112'
# PUZZLEINPUT = '1'

def look_and_say(iterations):
    inputs = []
    inputs.append(PUZZLEINPUT)
    for i in range(iterations):
        prev_char =''
        temp = ''
        output = ''
        
        for char in inputs[i]:
            if prev_char == '' or prev_char == char:
                prev_char=char
                temp += char
            else:
                prev_char=char
                output += str(len(temp))+temp[0]
                temp = char

        # Handle the last item         
        output += str(len(temp))+temp[0]
        inputs.append(output)  
        temp = ''
        output = ''
    
    return len(inputs[iterations])


print(f'Part 1: {look_and_say(40)}')
print(f'Part 2: {look_and_say(50)}')