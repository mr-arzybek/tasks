import re
from collections import Counter

def most_common_word(sentence):
    words = re.findall(r'\w+', sentence)
    word_count = Counter(words)
    return word_count.most_common(1)[0]
sentence =str(input("введите предложение : "))
most_common = most_common_word(sentence)
print(f'слово  "{most_common[0]}" было использовано {most_common[1]} раз')



