speech = ("this is a sample text with several words in which"
          " i am not sure i have repeated any word even though"
          " there are several words in "
          "this several words text. I think this iS absurd")

speech_count = {}
for word in speech.split():
    if word in speech_count:
        speech_count[word] += 1
    else:speech_count[word] = 1


print(f'{"Word":<12}Count')

for word, count in sorted(speech_count.items()):
    print(f'{word:<12}{count}')
