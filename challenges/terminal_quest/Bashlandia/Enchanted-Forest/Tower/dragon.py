from pathlib import Path

lockfile = Path('runes.lock')
scalefile = Path('dragonscale.txt')

if lockfile.exists():
    print(
"""
You reach a large stone tower at the top of a hill. Its isolation is perplexing.
Gazing at the top of the tower, you spy a glint of gold and a flash of a wing.
The dragon! It looks down at you and speaks:

"My hero! I have been imprisoned in this tower by the evil Princess.
Please, help me escape and you will have my gratitude! Her magic runes keep
me imprisoned, but a powerful mage such as yourself should have no trouble
countering her spells."
    
Remove the runes.lock file to free the dragon. Then rerun this file.
    """)
elif not scalefile.exists():
    with open(scalefile, 'w') as f:
        f.write('')
    print(
"""
With a wave of your staff, the runes around the tower walls fade and disappear.
You hear stones crack above you as the dragon breaks free of the prison.
Its voice booms:

"You have freed me from the clutches of that evil princess! Please accept
one of my scales as a token of my gratitude. Wherever you journey next, know
that you have a friend in the skies."

With a mighty roar, the dragon launches from the ruins of the tower and flies
toward the horizon. You beat a hasty retreat from the castle before the guards
realize what has happened.

Move the dragonscale.txt file to the witch's cauldron.
"""
    )
else:
    print(
"""
Below the ruins of the tower, a team of workers surveys the damage. You should
not linger here long - the princess is no doubt enraged at the dragon's escape.
"""
    )