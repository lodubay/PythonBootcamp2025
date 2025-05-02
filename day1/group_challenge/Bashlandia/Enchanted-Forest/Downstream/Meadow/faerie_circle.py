from pathlib import Path
import os

circle = Path('.circle')
flamecap = Path('flamecap.txt')
evils = ['flamecap1.evil', 'flamecap2.evil', 'flamecap3.evil', 
         'flamecap4.evil', 'flamecap5.evil', 'flamecap6.evil']

if circle.is_file():
    print(
"""
You approach the circle of mushrooms carefully, keen on finding a suitable
flamecap to harvest. But suddenly, your foot catches on a gnarled root
and you stumble headlong into the faerie circle!

You look around as one by one, the mushrooms on the edge of the faerie circle
start to twist and grow. Illusory flames dance across their caps as the
mushrooms uproot themselves and start to march toward you!

You steel yourself. There isn't much time, but maybe a well-placed spell
can knock out all of the evil mushrooms before they're upon you.

Hint: use the * wildcard to remove multiple files at once!
"""
    )
    # create evil mushrooms
    for evil in evils:
        with open(evil, 'w') as f:
            f.write('')
    # remove faerie circle
    os.remove(circle)
else:
    if '.evil' in ''.join(os.listdir()):
        print(
"""
The horde of mushrooms closes in. It's not too late to cast your spell!

Hint: use the * wildcard to remove multiple files at once! For example,
*.txt refers to all files with the .txt extension.
"""
        )
    else:
        print(
"""
As the awakened mushrooms close in, you utter a single spell. An icy blast
emanates away from you in all directions, shredding the monsters that were
encircling you. As the sound of the spell fades, no trace of the creatures
remains.

You look down and see a solitary mushroom poking out from the grass. A
flamecap, just as the witch requested! With a quick stroke of a knife, you
harvest the mushroom.

Hint: move the flamecap to the witch's cauldron.
"""
        )
        with open(flamecap, 'w') as f:
            f.write('')
