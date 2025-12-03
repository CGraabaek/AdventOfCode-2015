import hashlib

print("Advent Of Code - Day 4")


PUZZLEINPUT = 'ckczppom'

# TESTCASE1 = 'abcdef'
# TESTCASE2 = 'pqrstuv'


key = ''
key2 = ''

for i in range(100000000000000000):
    full_input = PUZZLEINPUT+str(i)
    h = hashlib.md5(full_input.encode())
    h = h.hexdigest()
    # Uncomment this for part 1
    # if h[:5] == '00000': 
    #     key = full_input
    #     break
    if h[:6] == '000000':
        key2 = full_input
        break

print(f'Part 1: Key is {key}')
print(f'Part 2: Key is {key2}')
