import re

string = "The quick brown fox jumps over the lazy dog."

# re.sub(pattern, replace, string, count=0, flags=0)
# Replace all occurrences of "the" with "a" using a regular expression

new_string = re.sub("the", "a", string)
print(new_string)

new_string = re.sub(r"\b[tT]\w*e\b", "a", string)
print(new_string)

a = "  hello  apple  " # > 'hello  apple'
b = "  hello  apple  " # > 'helloapple'
c = "  hello  apple  "

print(a.strip())
print(a.replace(" ", ""))
print(" ".join(a.split()))