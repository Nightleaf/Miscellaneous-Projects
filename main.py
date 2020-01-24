import random

######################################################################################################
# AUTHOR: Colton Thompson (@NightleafTV)                                                             #
# http://nightleaf.org/                                                                              #
# May 27th, 2019                                                                                     #
#                                                                                                    #
# This script generates a random race/class combination for World of Warcraft CLASSIC.               #
# It also selects two primary professions for the character.                                         #
######################################################################################################

playable_gender = ['male', 'female']
playable_races = ['orc', 'gnome', 'human', 'dwarf', 'tauren', 'troll', 'night elf']
playable_classes = ['paladin', 'warlock', 'warrior', 'druid', 'hunter', 'mage', 'rogue', 'priest']
primary_professions = ['alchemy', 'blacksmithing', 'enchanting', 'engineering', 'herbalism', 'leatherworking',
                       'mining', 'skinning', 'tailoring']
orc_classes = ['hunter', 'rogue', 'shaman', 'warlock', 'warrior']
gnome_classes = ['mage', 'rogue', 'warlock', 'warrior']
human_classes = ['mage', 'paladin', 'priest', 'rogue', 'warlock', 'warrior']
dwarf_classes = ['hunter', 'paladin', 'priest', 'rogue', 'warrior']
tauren_classes = ['druid', 'hunter', 'shaman', 'warrior']
troll_classes = ['hunter', 'mage', 'priest', 'rogue', 'shaman', 'warrior']
nightelf_classes = ['druid', 'hunter', 'priest', 'rogue', 'warrior']

paladin_tree = ['protection', 'retribution', 'holy']
warlock_tree = ['affliction', 'demonology', 'destruction']
warrior_tree = ['arms', 'fury', 'protection']
druid_tree = ['balance', 'feral', 'restoration']
hunter_tree = ['beast mastery', 'marksmanship', 'survival']
mage_tree = ['arcane', 'fire', 'frost']
rogue_tree = ['assassination', 'combat', 'subtlety']
priest_tree = ['discipline', 'holy', 'shadow']
shaman_tree = ['restoration', 'enhancement', 'elemental']

player_gender = random.choice(playable_gender)
player_race = random.choice(playable_races)
player_class = random.choice(playable_classes)
first_primary_profession = random.choice(primary_professions)
second_primary_profession = random.choice(primary_professions)

# Prevent the second profession from being the same as the first profession.
while second_primary_profession == first_primary_profession:
    second_primary_profession = random.choice(primary_professions)

# Prevent a class choice from being selected that a race cannot play.
if player_race == 'orc':
    if player_class not in orc_classes:
        player_class = random.choice(orc_classes)

if player_race == 'gnome':
    if player_class not in gnome_classes:
        player_class = random.choice(gnome_classes)

if player_race == 'human':
    if player_class not in human_classes:
        player_class = random.choice(human_classes)

if player_race == 'dwarf':
    if player_class not in dwarf_classes:
        player_class = random.choice(dwarf_classes)

if player_race == 'tauren':
    if player_class not in tauren_classes:
        player_class = random.choice(tauren_classes)

if player_race == 'troll':
    if player_class not in troll_classes:
        player_class = random.choice(troll_classes)

if player_race == 'night elf':
    if player_class not in nightelf_classes:
        player_class = random.choice(nightelf_classes)

# Choose a specialization for the class.
if player_class == 'druid':
    player_spec = random.choice(druid_tree)
elif player_class == 'hunter':
    player_spec = random.choice(hunter_tree)
elif player_class == 'mage':
    player_spec = random.choice(mage_tree)
elif player_class == 'paladin':
    player_spec = random.choice(paladin_tree)
elif player_class == 'priest':
    player_spec = random.choice(priest_tree)
elif player_class == 'rogue':
    player_spec = random.choice(rogue_tree)
elif player_class == 'shaman':
    player_spec = random.choice(shaman_tree)
elif player_class == 'warlock':
    player_spec = random.choice(warlock_tree)
elif player_class == 'warrior':
    player_spec = random.choice(warrior_tree)

print 'You are playing as a %s %s %s with a %s specialization.' % (
    player_gender, player_race, player_class, player_spec)
print 'Your two primary professions are %s and %s.' % (first_primary_profession, second_primary_profession)
