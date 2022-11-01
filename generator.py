import random



def get_random_word(words):
    return random.choice(words)


names=["Vasil", "Preslava", "Tony", "Slavi"]
places=["Sliven", "Shumen", "Dobrich", "Pleven"]
verbs=["eats", "holds", "throws", "brings", "carries", "collects", "steals"]
nouns=["stones", "cake", "money", "apples", "napkins", "bottles", "laptop"]
adverbs=["slowly", "quickly", "diligently", "warmly", "sadly",  "happily"]
details=["at home", "near the river", "in the park", "at school", "in the hospital"]

while True:
    random_name=get_random_word(names)
    random_place=get_random_word(places)
    random_verb=get_random_word(verbs)
    random_noun=get_random_word(nouns)
    random_adverb=get_random_word(adverbs)
    random_detail=get_random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun}.")
    input("Press [Enter] to generate a random sentence.")