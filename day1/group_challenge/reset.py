"""
This script resets the terminal quest to its initial state.
"""
import os
from pathlib import Path

def main():
    confirm = input(
"""
Would you like to reset your progress in this quest? This cannot be undone.
yes/no: """
    )
    if confirm.lower() == 'yes':
        reset_game()
    

def reset_game():
    files_to_rename = {
        'Bashlandia/Enchanted-Forest/Downstream/': 'Bashlandia/Enchanted-Forest/.Downstream/',
        'Bashlandia/Enchanted-Forest/Upstream/': 'Bashlandia/Enchanted-Forest/.Upstream/',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/Cavern/': 'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/',
    }
    files_to_remove = [
        'Bashlandia/Enchanted-Forest/staff.txt',
        'Bashlandia/Enchanted-Forest/spellbook.txt',
        'Bashlandia/Enchanted-Forest/spare_robes.txt',
        'Bashlandia/Enchanted-Forest/dagger.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Tower/dragonscale.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/echo.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/torch.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/gemstone1.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/gemstone2.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/gemstone3.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/gemstone4.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/.Cavern/gemstone5.txt',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap1.evil',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap2.evil',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap3.evil',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap4.evil',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap5.evil',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap6.evil',
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/flamecap.txt',
        'Bashlandia/Enchanted-Forest/.Downstream/Swamplands/clue.txt',
        'Bashlandia/.Secret-Island/call_parrot.sh',
        'Bashlandia/.Secret-Island/.rick'
    ]
    dirs_to_remove = [
        'Bashlandia/Enchanted-Forest/Boat/',
        'Bashlandia/Enchanted-Forest/.Downstream/Swamplands/Cauldron/'
    ]
    files_to_create = [
        'Bashlandia/Enchanted-Forest/.Downstream/Meadow/.circle',
        'Bashlandia/Enchanted-Forest/.Upstream/Mine/torch.txt',
        'Bashlandia/Enchanted-Forest/.Upstream/Tower/runes.lock',
    ]

    for f, newf in files_to_rename.items():
        if Path(f).exists():
            os.rename(f, newf)
    for f in files_to_remove:
        if Path(f).is_file():
            os.remove(f)
    for d in dirs_to_remove:
        if Path(d).is_dir():
            for f in os.listdir(d):
                os.remove(Path(d) / f)
            os.rmdir(d)
    for f in files_to_create:
        if not Path(f).is_file():
            with open(Path(f), 'w') as file:
                file.write('')


if __name__ == '__main__':
    main()
