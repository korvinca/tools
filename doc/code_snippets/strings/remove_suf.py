#!/bin/python3
# import re

#1. remove "nd" or "ss" or "ing" from end of the word
#2. if word > 8, cut it to 8

def stemmer(text):
    text = text.split()
    res = ""
    new_list = []
    for word in text:
        if word[-2:] == "nd" or word[-2:] == "ss":
            word = word[:-2]
        elif word[-3:] == "ing":
            # word = re.sub("ing", "", word)
            word = word[:-3]
        if len(word) > 8:
            word = word[:8]
        new_list.append(word)
    # print(str(new_list))
    res = " ".join(new_list)
    return res


if __name__ == '__main__':
    text = "We saw hhgfjhgfjhgfjhgim swimming asscross the pond"
    print(stemmer(text))