from pathlib import Path

bashscript = Path('call_parrot.sh')
rickroll = Path('.rick')

if not rickroll.is_file():
    print(
"""
At long last, you arrive at the secret island. You pull your boat up onto the
beach and start to get your bearings. You notice a man in the distance.
He appears to be... dancing?

"Hullo!" he calls out as you approach. "What brings you to my island?"

"I seek a missing parrot. His magical abilities are of great renown, and he
is sorely needed in his home kingdom," you reply.

The man continues dancing. "Well, I don't know about any magic parrot,"
he says, "but I can give you a spell that I use whenever I'm looking for
something!"

He produces a scroll and hands it to you. You take it and begin to cast
the spell.

Hint: use "bash call_parrot.sh" to run the shell script. If you need to
exit once it's running, hit Ctrl-C.
"""
    )
    with open(bashscript, 'w') as f:
        f.write('touch %s\ncurl ascii.live/rick' % rickroll)
else:
    print(
"""
The man laughs. "Haha! Just my little joke. Here is the spell you should
actually use!"

curl parrot.live

You roll your eyes and try the new spell. Show the instructor the result!
"""
    )