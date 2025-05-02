from pathlib import Path
import os

boat = Path('Boat')
belongings = ['staff.txt', 'spellbook.txt', 'spare_robes.txt', 'dagger.txt']
paths = ['Upstream', 'Downstream']

if boat.is_dir():
    if all([Path(boat / f).is_file() for f in belongings]):
        # Unhide directories
        for path in paths:
            if not Path(path).is_dir():
                os.rename('.%s' % path, path)
        print(
"""
Congratulations, you have solved my river puzzle!

Once you cross to the other side, you can either follow the river upstream, 
into the hills, or downstream, into the riverlands. The choice is yours.
"""
        )
    else:
        print(
"""
You have conjured a rowboat! It's nothing fancy, but it will get the job done.
Now, stow your belongings in it and hop aboard!

Hint: move all the text files into the Boat directory.
"""
        )
else:
    # Hide directories
    for path in paths:
        if Path(path).is_dir():
            os.rename(path, '.%s' % path)
    for fname in belongings:
        # Set up files
        if not Path(fname).is_file():
            with open(fname, 'w') as f:
                f.write('')
    print(
"""
After several days' journey through the forest, you come across a wide river.
You need to cross it, but if you swim, all your stuff will get wet, and that is
unacceptable! Fortunately you are a powerful wizard who can conjure a suitable
boat with a wave of your staff.

Make a directory called "Boat" and move all of your belongings into it.
Then, rerun this script.
"""
    )
    