print("Advent Of Code - Day 3")

PUZZLEINPUT = open('input.txt', 'r').read()

position = (0,0)
visited_houses = [position,]

# Part 1
for direction in PUZZLEINPUT:
    x, y = position

    if(direction == '^'):
        y+=1
    elif(direction == 'v'):
        y-=1
    elif(direction == '>'):
        x+=1
    elif(direction == '<'):
        x-=1
    else:
        print 'error with ' + direction
        break
    
    position = (x,y)

    if(position not in visited_houses):
        visited_houses.append(position)
    
print("Part 1: " + str(len(visited_houses)))

#position_p2= (0,0)

position_santa = (0,0)
position_robosanta = (0,0)

visited_houses_p2 = []

for idx,direction in enumerate(PUZZLEINPUT):
    if(idx % 2 == 0):
        position_p2 = position_santa
    else:
        position_p2 = position_robosanta

    x,y = position_p2

    if(direction == '^'):
        y+=1
    elif(direction == 'v'):
        y-=1
    elif(direction == '>'):
        x+=1
    elif(direction == '<'):
        x-=1
    else:
        print 'error with ' + direction
        break
    position_p2 = (x,y)
    if(idx % 2 == 0):
        position_santa = (x,y)
    else:
        position_robosanta = (x,y)


    if(position_p2 not in visited_houses_p2):
        visited_houses_p2.append(position_p2)

print("Part 2: " + str(len(visited_houses_p2)))
