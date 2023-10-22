a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
res = []
n = 1

for i in a :
    l = str(a[-n])
    res.append(l)
    n += 1

print(res)

