import json
import sys
import csv
import re

#max_lenght = 102


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


def csv_creator( cardList ):

    with open('../data/texts.csv', 'w', encoding='UTF8', newline='') as file:
        header = ['text', 'label']
        writer = csv.writer(file)

        writer.writerow(header)
        #max_length=0
        data = []
        words = []
        for i in cardList:
            text = i.get('oracle_text')
            text = re.sub("\(.*?\)","()",text)

            text = str(int(i.get('cmc'))) + "." + i.get('type_line') + "." + i.get('colors') + "." + i.get('rarity') + "." +\
                   str(i.get('power')) + "." + str(i.get('toughness')) + "." + text
            #if len(text.split()) > max_length:
            #    max_length = len(text.split())
            text = re.sub("[{}(),\"\'—[\]]","",text)
            tmp= [ text , '']
            data.append(tmp)

        writer.writerows(data)
    return True

def retrieve_data():
    with open('../data/oracle-cards-20240220220210.json',encoding="utf8") as json_file:
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

            if i.get('oracle_text') is None:
                text = "None"
            else:
                text = i.get('oracle_text').replace('\n', '.')
                text = text.replace('\"', '')
                if i.get('name') in text:
                    text.replace(i.get('name'), '')
                card_info["oracle_text"] = text

            if(i.get('colors')) == []:
                card_info["colors"]=str(['N'])
            else:
                card_info["colors"] = str(i.get('colors'))


            if i.get('reprints') is not None:
                card_info["reprints"] = i.get('reprints')
            else:
                card_info["reprints"] = 'None'

            card_info["rarity"] = i.get('rarity')

            if i.get('power') is None:
                card_info["power"] = 'None'
            else:
                card_info["power"] = str(i.get('power'))

            if i.get('toughness') is None:
                card_info['toughness'] = 'None'
            else:
                card_info['toughness'] = str(i.get('toughness'))

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

    cardList = retrieve_data()


    name = ''
    while name != '-e':
        name = input("insert card name")
        for i in cardList:
            if i.get('name').lower() == name.lower():
                print(i)

    csv_creator( cardList )
