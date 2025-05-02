from pathlib import Path
import os

torch = Path('torch.txt')
gemstones = ['gemstone1.txt', 'gemstone2.txt', 'gemstone3.txt', 'gemstone4.txt', 'gemstone5.txt']

if torch.is_file():
    # Reveal gemstone files
    for g in gemstones:
        if not Path(g).is_file():
            # Copy gemstone files
            with open(Path('.Gemstones/%s' % g), 'r') as f:
                content = f.read()
            with open(Path(g), 'w') as f:
                f.write(content)
            # os.rename('.%s' % g, g)
    print(
"""
Under the light of your torch, five gemstones glitter against the dark walls
of the cavern. You think you should be able to find a stone for the witch here
- but which one?

Hint: use the man command to look up the documentation for ls. There is a flag
that will list the size of a file next to its name. Remember that you're
looking for a file that's exactly 85 bytes.
"""
    )
else:
    if all([g in os.listdir() for g in gemstones]):
        # Hide gemstone files
        for g in gemstones:
            if Path(g).is_file():
                os.remove(g)
    print(
"""
You turn a corner and are greeted with pitch darkness. You can't even see your
own hand in front of your face, let alone search for these gemstones. You 
probably should have lit your own torch using the torches at the cave's 
entrance.

Hint: copy the torch.txt file from the previous directory into this one.
"""
    )