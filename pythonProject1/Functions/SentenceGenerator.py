import random

articles: list = ["the" , "a", "one", "some", "any"]
nouns: list = ["mansion", "car", "ship", "thief", "Lawyer"]
verbs: list = ["drove", "jumped" , "ran", "walked", "skipped"]
prepositions: list = ["on", "beside", "by", "under"]

# sentence = random.choice(articles)
for _ in range (20):
    sentence = "{} {} {} {} {} {}.".format(
    random.choice(articles),
    random.choice(nouns),
    random.choice(verbs),
    random.choice(prepositions),
    random.choice(articles),
    random.choice(nouns),
    ).capitalize()
    print(sentence)