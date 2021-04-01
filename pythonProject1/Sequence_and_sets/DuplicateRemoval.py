# (Counting Duplicate Words) Write a script that uses a dictionary to determine and
# print the number of duplicate words in a sentence. Treat uppercase and lowercase letters
# the same and assume there is no punctuation in the sentence. Use the techniques you
# learned in Section 6.2.7. Words with counts larger than 1 have duplicates.

from collections import Counter

speech = ("This is a sample text with several words in which"
          " i am not sure i have repeated any word even Though"
          " there are Several words in "
          "this several words text. I think this iS absurD")
speech = speech.lower()
speech_counter = {}

counter = Counter(speech.split())
for word, count in sorted(counter.items()):
    if count > 1:
        print(f'{word} has {count} duplicates')

