"""
This script takes an English message in MESSAGE.txt and converts it into
Morse code, outputting to CODE.txt
"""

morse_key = {}
with open('KEY.txt', 'r') as f:
    for l in f.readlines():
        key, val = l.split('\s+')
        morse_key[key] = val

print(morse_key['A'])