t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t)
t[1:3] = ['x', 'y']
print(t)

t.append('d')
print(t)

t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)

#deleting element
x = t.pop(1)
print(t)
print(x)

del t[1]
print(t)

t.remove('d')
print(t)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
del t[1:3]
print(t)