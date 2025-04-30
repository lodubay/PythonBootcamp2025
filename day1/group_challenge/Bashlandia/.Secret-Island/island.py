from pathlib import Path

rickroll = Path('./.rick')

if not rickroll.is_file():
    print(
"""
At long last, you arrive at the secret island. You pull your boat up onto the
beach and start to get your bearings. You notice a man in the distance.
He appears to be... dancing?

"Hullo!" he calls out as you approach. "What brings you to my island?"

"I seek a missing parrot. His magical abilities are of great renown, and he
is sorely needed in is home kingdom," you reply.

The man continues dancing. "Well, I don't know about any magic parrot,"
he says, "but whenever I'm looking for something, I use this spell:

curl ascii.live/rick

Then whatever I need usually falls right into my lap!"

You stare at the man. Could it really be so simple?

Try the dancing man's spell.
"""
    )
    with open(rickroll, 'w') as f:
        f.write('')
else:
    print(
"""
The man laughs. "Haha! Just my little joke. Here is the spell you should
actually use!"

curl ascii.live/parrot

You roll your eyes and try the new spell.
"""
    )