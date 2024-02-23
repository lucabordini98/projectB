import json
import sys


keywords = ['Enchant', 'Flying', 'Food', 'Adapt', 'Treasure', 'Reach', 'Equip', 'Connive', 'Enrage',
            'Cycling', 'Bloodthirst', 'Trample', 'Kicker', 'Vigilance', 'Corrupted', 'Role token',
            'Menace', 'Flash', 'Prowess', 'Revolt', 'Crew', 'Infect', 'First strike', 'Fight', 'Persist',
            'Multikicker', 'Awaken', 'Ninjutsu', 'Hexproof', 'Heroic', 'Scry', 'Exalted', 'Discover',
            'Cohort', 'Haste', 'Bestow', 'Surveil', 'Renown', 'Landwalk', 'Forestwalk', 'Devoid', 'Protection',
            'Amass', 'Addendum', 'Morbid', 'Explore', 'Compleated', 'Unearth', 'Double strike', 'Lifelink',
            'Investigate', 'Threshold', 'Prototype', 'Deathtouch', 'Indestructible', 'Graft', 'Transform',
            'Defender', 'Manifest', 'Rebound', 'Evoke', 'Escape', 'Overload', 'Clash', 'Descend', 'Channel',
            'Bushido', 'Magecraft', 'Madness', 'Modular', 'Sunburst', 'Islandwalk', 'Offering', 'Changeling',
            'Aftermath', 'Mill', 'Proliferate', 'Alliance', 'Populate', 'Reinforce', 'Fuse', 'Chroma', 'Ripple',
            'Undying', 'Living weapon', 'Suspend', 'Exert', 'Collect evidence', 'Conspire', 'Landcycling',
            'Basic landcycling', 'Typecycling', 'Tribute', 'Landfall', 'Megamorph', 'Mountainwalk', 'Vanishing',
            'Incubate', 'Pack tactics', 'Shroud', 'Retrace', 'Coven', 'Dash', 'Bloodrush', 'Ward', 'Ascend',
            'Blitz', 'Cleave', 'Extort', 'Boast', 'Hexproof from', 'Affinity', 'Metalcraft', 'Unleash', 'Convoke',
            'Entwine', 'Disturb', 'Ingest', 'Bargain', 'Domain', 'Flashback', 'Disguise', 'Monstrosity', 'Toxic',
            'Transmute', 'Mentor', 'Venture into the dungeon', 'Delve', 'Training', 'Delirium', 'Mutate',
            'Spell mastery', 'Kinship', 'Foretell', 'Fear', 'Grandeur', 'Reconfigure', 'Support', 'Adamant', 'Evolve',
            'Radiance', 'Morph', 'Level Up', 'Celebration', 'Daybound', 'Nightbound', 'Flanking', 'Split second',
            'Afterlife', 'Read Ahead', 'Intimidate', 'Spectacle', 'Scavenge', 'Converge', 'Bolster', 'Meld', 'Buyback',
            'Enlist', 'Epic', 'Improvise', 'Riot', 'Soulshift', 'Echo', 'Battle Cry', 'Casualty', 'Hideaway',
            'Battalion', 'Suspect', 'Cipher', 'Legendary landwalk', 'Fathomless descent', 'Raid', 'Miracle',
            'Swampcycling', 'Constellation', 'Splice', 'Rampage', 'Soulbond', 'Companion', 'Backup', 'Champion',
            'Surge', 'Fabricate', 'Devour', 'Mountaincycling', 'Exploit', 'Detain', 'Outlast', 'Annihilator', 'Afflict',
            'Fateful hour', 'Learn', 'Craft', 'Hellbent', 'Replicate', 'Swampwalk', 'Dredge', 'Ferocious', 'Inspired',
            'Forecast', 'Rally', 'For Mirrodin!', 'Strive', 'Storm', 'Fateseal', 'Imprint', 'Escalate', 'Recover', 'Wither',
            'Eternalize', 'Embalm', 'Wizardcycling', 'Cascade', 'Goad', 'Emerge', 'Formidable', 'Totem armor', 'Haunt',
            'Skulk', 'Undergrowth', 'Slivercycling', 'Shadow', 'Cumulative upkeep', 'Islandcycling', 'Plainscycling',
            'Forestcycling', 'Fortify', 'Transfigure', 'Assemble', 'Cloak', 'Plainswalk', 'Jump-start', 'Prowl',
            'Nonbasic landwalk', 'Sweep', 'Aura Swap', 'Gravestorm']

'''
print('[')

text = ""
            #print('\t\t{')
            #print('\t\t{')
            #print('\t\t{')
            #print('\t\t\t\"mana_cost\":', '\"' + str(i.get('mana_cost'))+ '\",')
            #print('\t\t\t\"cmc\":', '\"' + str(i.get('cmc')) + '\",')
            #print('\t\t\t\"type_line\":', '\"' + i.get('type_line') + '\",')
            #print('\t\t\t\"oracle_text\":', '\"' + text + '\",')
            #print('\t\t\t\"colors\":', json.dumps(i.get('colors')), ',')
            #print('\t\t\t\"reprint\":', '\"' + str(i.get('reprint')) + '\",')
            #print('\t\t\t\"rarity\":', '\"' + i.get('rarity') + '\",')
           #print('\t\t\t\"power\":', '\"' + str(i.get('power')) + '\",')
            #print('\t\t\t\"toughness\":', '\"' + str(i.get('toughness')) + '\",')
                 #print('\t\t\t\"prices\":', '\"L\"', '\n\t\t},')
                        #print('\t\t\t\"prices\":', '\"M\"', '\n\t\t},')
                        #print('\t\t\t\"prices\":', '\"H\"' '\n\t\t},')
                        #print('\t\t\t\"prices\":', json.dumps(i.get('prices')), '\n\t\t},')
    #print('\t]')



'''


def retrievedata():
    with open('oracle-cards-20240220220210.json') as json_file:
        json_load = json.load(json_file)

    file = open('out.txt', 'w')
    orig_stdout = sys.stdout
    sys.stdout = file
    all_cards = []
    for i in json_load:

        if i.get('legalities').get('modern') == 'legal':
            card_info = dict({})

            card_info["name"] = i.get('name').replace('\"', '')
            card_info["cmc"] = i.get('cmc')
            card_info["type_line"] = i.get('type_line')
            card_info["keywords"] = i.get('keywords')
            if i.get('oracle_text') is None:
                text = "None"
            else:
                text = i.get('oracle_text').replace('\n', '.')
                text = text.replace('\"', '')
            card_info["oracle_text"] = text
            card_info["colors"] = i.get('colors')
            card_info["reprints"] = i.get('reprint')
            card_info["rarity"] = i.get('rarity')
            card_info["power"] = i.get('power')
            card_info["toughness"] = i.get('toughness')
            if i.get('prices').get('eur') is None or float(i.get('prices').get('eur')) < 1:
                card_info["price"] = 'L'
            else:
                if 1 <= float(i.get('prices').get('eur')) < 4:
                    card_info["price"] = 'M'
                else:
                    card_info["price"] = 'H'
            all_cards.append(card_info)

    sys.stdout = orig_stdout
    file.close()
    return all_cards


if __name__ == '__main__':

    cardList = retrievedata()
    name = ''
    while name != '-e' :
        name = input("insert card name")
        for i in cardList:
            if i.get('name').lower() == name.lower():
                print(i)

