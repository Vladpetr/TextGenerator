from collections import defaultdict, Counter
from nltk import trigrams
from random import choice, choices
import re


def load_text(file_name_):
    with open(file_name_, encoding='utf-8') as file_:
        return file_.read().split()


trigrams_list = list(trigrams(load_text(input())))

trigrams_dict = defaultdict(list)
for head, mid, tail in trigrams_list:
    trigrams_dict[head + " " + mid].append(tail)

trigrams_dict = {head: dict(Counter(tail)) for head, tail in trigrams_dict.items()}
capital_heads = dict(filter(lambda elem: elem[0][0].isupper(), trigrams_dict.items()))

no_punc_heads = dict(filter(lambda elem: not re.match(".*[.?!]", elem[0].split()[0]), capital_heads.items()))


for _ in range(10):
    first_word = "".join(choice(list(no_punc_heads.keys())))
    chain_words = [word for word in first_word.split()]
    while True:
        if re.match(".*[.?!]", first_word.split()[1]):
            if len(chain_words) >= 5:
                break

        next_word = choices(list(trigrams_dict[first_word].keys()), weights=list(trigrams_dict[first_word].values()))
        chain_words.extend(next_word)
        second = first_word.split()[1]

        word_comb = [second, next_word[0]]

        first_word = " ".join(map(str, word_comb))


    print(" ".join(chain_words))