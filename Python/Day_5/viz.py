class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
        return True,match.group(1)
    else:
        return False,""

def format_nice_string(string,character):
    formatted_string = ""
    for letter in string:
        if letter == character or letter in "aeiou":
            formatted_string += bcolors.OKGREEN + letter + bcolors.ENDC    
        else:
            formatted_string += letter
    return formatted_string


def validate_string(text):
    vowels_ok = validate_vowel(text)
    is_naugthy = check_for_naughty_word(text)
    has_doubleletter,letter = check_doubleletter(text)

    if vowels_ok and not is_naugthy and has_doubleletter:
        nice_strings.append(line)
        formatted_string = format_nice_string(line,letter)
        print("[{:<1}]     {:>20}".format(bcolors.OKGREEN+'NICE'+bcolors.ENDC,formatted_string))
    else:
        naughty_strings.append(line)
        print("[{:<1}] {:>17}".format(bcolors.FAIL+'NAUGTHY'+bcolors.ENDC,line))

for line in PUZZLEINPUT:
    validate_string(line)

print(f'Part 1: {len(nice_strings)} nice strings')