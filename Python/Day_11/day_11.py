print("Advent Of Code - Day 10")

PUZZLEINPUT = 'hxbxwxba'

password = PUZZLEINPUT[::-1]
password_length = len(PUZZLEINPUT)
# print(password_length)
new_password = password


def next_alpha(s):
    return chr((ord(s.upper())+1 - 65) % 26 + 65).lower()

def has_double_letter(password):
    return False

def has_increasing_straight(password):
    return False

def has_bad_words(password):
    return False;


for i in range(password_length):
    next_char = next_alpha(new_password[i])
    print(next_char)
    list(new_password)[i] = next_char

print("".join(new_password))
print(password)