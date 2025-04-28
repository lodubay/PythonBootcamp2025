from pathlib import Path
import os

cauldron = Path('Cauldron/')
ingredients = ['dragonscale', 'flamecap', 'finger']
clue = Path('clue.txt')

if not cauldron.is_dir():
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
and the finger of a dead saint. Bring these to me, and I will help you."

You blink, and the witch vanishes. The cauldron bubbles merrily.
"""
    )
elif not all([Path('Cauldron/%s.txt' % i).is_file() for i in ingredients]):
    print(
"""
You return to the hut, but there is no sign of the witch. It seems she will
only return once you gather the dragon scale, mushroom cap, and dead saint's
finger and deposit them in the cauldron.
"""
    )
elif not clue.is_file():
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
"""
    )
    with open(clue, 'w') as f:
        f.write(
"""
There is much you know about this land, but some places remain hidden to you.
Return to Bashlandia and use this command to reveal the location of the island
where the Magic Parrot hides:

ls -a
"""
        )
    for i in ingredients:
        os.remove('Cauldron/%s.txt' % i)
    os.rmdir('./Cauldron')
else:
    print(
"""
Try as you might, you cannot find the clearing where you encountered the
witch before. Something tells you this isn't the last you've seen of her...
"""
    )
