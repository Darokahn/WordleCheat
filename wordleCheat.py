import re

def blank_state():
    return {
        'l': '_____',
        'y': ['']*5,
        'g': ''
        }

def get_guess(current_state):
    word = input("what word did you guess? ")
    pattern = input("what pattern was it, using 'l' as lime(green), 'y' as yellow, and 'g' as gray?\n")
    for count in range(5):
        if pattern[count] == 'y':
            current_state['y'][count] += word[count]
        elif pattern[count] == 'l':
            temp = list(current_state['l'])
            temp[count] = word[count]
            temp = "".join(temp)
            current_state['l'] = temp
        elif pattern[count] == 'g':
            current_state['g'] += word[count]
    return current_state

def exclude(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    for char in chars:
        alphabet.remove(char)
    return "".join(alphabet)

def get_pattern(current_state):
    l = current_state['l']
    y = current_state['y']
    g = current_state['g']
    fullpattern = ""
    for count in range(5):
        pattern = ''
        excludes = ''
        if l[count] != '_':
            pattern = l[count]
        else:
            excludes = y[count]
            excludes += g
            pattern = exclude(excludes)
            pattern = f'[{pattern}]'
        fullpattern += pattern
    return fullpattern

def check_database(pattern, yellows):
    matches = []
    with open("new_dict.txt", "r") as dictionary:
        line = "1"
        while line:
            line = dictionary.readline()
            line = line.replace("\n", "")
            if not re.match(pattern, line):
                continue
            matches_yellows = []
            for char in yellows:
                matches_yellows.append(char in line)
            if False in matches_yellows:
                continue
            matches.append(line)
    return matches

def letter_frequencies():
    frequencies = {}
    with open("letterfrequencies.txt", "r") as file:
        for line in file.readlines():
            if line == "\n":
                continue
            line = line.replace("\n", "")
            line = line.strip()
            letter, frequency = line.split(" ")
            frequency = float(frequency)
            frequencies.update({letter: frequency})
    return frequencies

def sort_matches(matches, frequencies):
    dicti = {}
    for match in matches:
        letter_occurrences = {}
        score = 0
        for letter in match:
            denom = 1
            if letter in letter_occurrences:
                letter_occurrences[letter] *= 2
            else:
                letter_occurrences.update({letter: 1})
            denom = letter_occurrences[letter]
            letter = letter.upper()
            score += frequencies[letter]/denom
        dicti.update({match: score})
    value = lambda x, d = dicti: dicti[x]
    return sorted(dicti)

state = blank_state()
f = letter_frequencies()
while True:
    state = get_guess(state)
    y = state['y']
    pattern = get_pattern(state)
    matches = check_database(pattern, y)
    matches = sort_matches(matches, f)
    print(matches)



        
