"""
This script takes an English message in MESSAGE.txt and converts it into
Morse code, outputting to CODE.txt
"""
import os

filedir = os.path.dirname(__file__)

# Read Morse Code key
morse_key = {}
with open(os.path.join(filedir, 'KEY.txt'), 'r') as f:
    for l in f.readlines():
        key, val = l.split('\t')
        morse_key[key] = val.split('\n')[0]
# Add a space
morse_key[' '] = ' '

# Read message
message = []
with open(os.path.join(filedir, 'MESSAGE.txt'), 'r') as f:
    message = f.readlines()
message = ''.join(message)

# Encode message (strings)
encoded = []
for char in message:
    encoded.append(morse_key[char.upper()])
print(' '.join(encoded))