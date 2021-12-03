PUZZLEINPUT = open('input.txt', 'r').read().strip().split("\n")

import re

nice_strings = []
naughty_strings = []

naugthy_words = ['ab','cd','pq','xy']

def validate_vowel(text):
    total_count = 0
    for vowel in "aeiou":
        count = text.count(vowel)
        total_count += count
    
    if total_count > 2:
        return True
    else: 
        return False

def check_for_naughty_word(text):
    for nw in naugthy_words:
        if nw in text:
            return True
    return False

def check_doubleletter(text):
    regexp = re.compile(r"(.)\1")
    match = re.search(regexp, text)
    if match:
        # print(str, "<- match for double", match.group(1))
        return True
    else:
        return False

def validate_string(text):
    vowels_ok = validate_vowel(text)
    is_naugthy = check_for_naughty_word(text)
    has_doubleletter = check_doubleletter(text)

    if vowels_ok and not is_naugthy and has_doubleletter:
        nice_strings.append(line)
    else:
        naughty_strings.append(line)

for line in PUZZLEINPUT:
    # print(f'{line} {check_existence(line)} ({validate_vowel(line)}) has double letter {check_doubleletter(line)} has naughty letter ({check_for_naughty_word(line)})')
    validate_string(line)

print(f'Part 1: {len(nice_strings)} nice strings')