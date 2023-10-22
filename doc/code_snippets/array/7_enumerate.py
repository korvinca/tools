numbers = [45, 22, 14, 65, 97, 72]

for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif numbers[i] % 3 == 0:
        numbers[i] = 'fizz'
    elif numbers[i] % 5 == 0:
        numbers[i] = 'buzz'

print(numbers)
# #['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']

numbers = [45, 22, 14, 65, 97, 72]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'
print(numbers)
# #['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']