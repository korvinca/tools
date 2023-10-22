# Code #2
# Code #2
A = "the sky is blue"
words = A.split()  # Split the string into words

reversed_words = words[::-1]  # Reverse the list of words
reversed_sentence = ' '.join(reversed_words)  # Join the reversed words back into a string
print(reversed_sentence)

#2

l = []  # empty list
new_str = ""
count = 0 

for i in words:  # iterate to reverse the list
    l.insert(0, i) # reversing the list

for i in l:
    if count != 0:
        new_str += " "
    new_str += str(i) # # Iterate over index for element in words:
    count += 1

print(new_str)

#3
new_str = " "
print(new_str.join(l))
