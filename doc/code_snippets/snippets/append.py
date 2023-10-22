#demonstrate list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
c = []
c = a
a.append(b)
print(a)
for i in b:
    print (i)
    c.append(i)
print(c)
