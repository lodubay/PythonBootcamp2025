from pathlib import Path
import os

echo = Path('echo.txt')
cavern = 'Cavern'

if echo.is_file() and os.path.getsize(echo) > 0:
    # Show cavern
    if not Path(cavern).is_dir():
        os.rename('.%s' % cavern, cavern)
    # Get echo
    phrase = ''
    with open(echo, 'r') as f:
        phrase = f.read()
    phrase = phrase.replace('\n', '')
    print(
f"""
Your words echo back to you from the deep:

"{phrase}..."

"{phrase}..."

"{phrase}..."

You wait a moment, but there is no answer. It seems like no one is home.
You press on into the caverns.
"""
    )
else:
    # Hide cavern
    if Path(cavern).is_dir():
        os.rename(cavern, '.%s' % cavern)
    print(
"""
You come across the entrance to a mine. It seems to be abandoned, but a pair of
torches burn at either side of the open gate. You call out and hear your words
echo back to you from the depths.

Use the echo command and the ">" pipe to write anything you want into a file
called "echo.txt".
"""
    )