from collections import Counter

speech = ("this is a sample text with several words in which"
          " i am not sure i have repeated any word even though"
          " there are several words in "
          "this several words text. I think this iS absurd")

counter = Counter(speech.split())

for word, count in sorted(counter.items()):
    print(f'{word:<12} {count}')
