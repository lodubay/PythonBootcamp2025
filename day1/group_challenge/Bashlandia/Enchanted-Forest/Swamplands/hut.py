from pathlib import Path
import os

cauldron = Path('Cauldron/')
ingredients = ['dragonscale', 'flamecap', 'gemstone4']
gemstone = cauldron / ('%s.txt' % ingredients[-1])
clue = Path('clue.txt')

if cauldron.is_dir():
    if any([g in os.listdir(cauldron) for g in ['gemstone1.txt', 'gemstone2.txt', 'gemstone3.txt', 'gemstone5.txt']]):
        # Player has provided the wrong gemstone
        print(
"""
The cauldron bubbles intensely for a moment. Suddenly, the gemstone you tossed
in comes hurtling back out toward you. It smacks you in the forehead. Seems
like you found the wrong stone!
"""
        )
    elif all([(cauldron / ('%s.txt' % i)).is_file() for i in ingredients]):
        if clue.is_file():
            # Witch has already given the clue
            print(
"""
Try as you might, you cannot find the clearing where you encountered the
witch before. Something tells you this isn't the last you've seen of her...
"""
            )
        else:
            if len(os.listdir(cauldron)) == len(ingredients):
                # Player has found all the ingredients, witch will give the clue
                print(
"""
As you toss the final ingredient into the cauldron, the bubbling intensifies
and its contents rapidly change color, from light green to sky blue, deep
violet, and finally pitch black. The cauldron begins to shake, and a high-
pitched shriek grows in your ears. You hurridly back away when a brilliant
flash of light temporarily blinds you. When the light fades, you see that
the cauldron and the hut have vanished without a trace.

A small scrap of paper lies on the ground in front of you, its edges charred.
As you read its inscription, you hear a faint cackling echoing around the
clearing - or maybe it's just the wind...

Hint: use the "less" command to print the contents of the file. Hit "Q" to
exit when finished.
"""
                )
                with open(clue, 'w') as f:
                    f.write(
"""
There is much you know about this land, but some places remain hidden to you.
Return to Bashlandia and use this command to reveal the location of the island
where the Magic Parrot hides:

ls -a

Hint: use pwd to get your current location.
"""
                    )
                for i in ingredients:
                    os.remove('Cauldron/%s.txt' % i)
                os.rmdir('./Cauldron')
            else:
                # Player has provided too many ingredients
                print(
f"""
You move to throw the ingredients into the pot, but in a flash the witch
appears in front of you, scowling.

"I was precise in my request - bring me these ingredients three! Yet you seem
to have brought {len(os.listdir())} items instead. The consequences for my
brew could be catastrophic! You must discard the extra items before I allow
you to pass."

Hint: there can only be 3 files within the Cauldron directory. Make sure you
only include the gemstone file that is 8 bytes in size.
"""
                )
    else:
        # Player hasn't found all the ingredients yet
        print(
"""
You return to the hut, but there is no sign of the witch. It seems she will
only return once you gather the dragon scale, mushroom cap, and gemstone
(of exactly 85 bytes) and deposit them in the cauldron.
"""
        )
else:
    # First time encountering the witch
    os.mkdir(cauldron)
    print(
"""
In a small clearing, you come across a small wooden hut. Smoke rises from the
chimney. Outside the hut, an old woman sits in a rocking chair. Next to her,
a large black cauldron bubbles.

"What is your purpose here?" says a voice in your head, although the woman
neither moves nor speaks.

"I seek the Magic Parrot of Bashlandia. It disappeared over a moon ago,"
you reply.

"Ah, the Magic Parrot! Tales of his magnificence have reached me even here,"
she says, turning to look at you but still not moving her mouth.
"Perhaps some lost things do not wish to be found. Nevertheless, I will help
you if you can first help me. For to complete this potion, I need these 
ingredients three: the scale of a gold dragon, the cap of a fiery mushroom,
and a gemstone of precisely 85 bytes. Bring these to me, and I will help you."

You blink, and the witch vanishes. The cauldron bubbles merrily.

Hint: explore the enchanted forest to find the three items. Once you find one,
use mv to move it into the Cauldron directory.
"""
    )
