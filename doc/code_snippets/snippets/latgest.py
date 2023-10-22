largest = None
print('Before:', largest)

list_int = [3, 41, 12, 9, 74, 15]

for itervar in list_int:
    if largest is None or itervar > largest :
        largest = itervar
    print('Loop:', itervar, largest)
print('Largest:', largest)
