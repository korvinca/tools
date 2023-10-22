"""
python3 find the penultimate (next to last) word of a sentence
"""

sentence = "This is an example sentence to find the penultimate word."
words = sentence.split()
if len(words) >= 2:
    penultimate_word = words[-2]
    print("The penultimate word is:", penultimate_word)
else:
    print("The sentence doesn't have a penultimate word.")