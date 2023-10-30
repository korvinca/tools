# Option 1 for
def fib(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

res = [0]
count = 1
while count <= 10:
    res.append(fib(count))
    count += 1
print(res)

# Option 2 while
res = [0]
fib1 = 0
fib2 = 1
i = 0
while i < 10:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i += 1
    res.append(fib1)
print(res)

# Option 3 recrusia
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
res = [0]
count = 1
while count <= 10:
    res.append(fibonacci(count))
    count += 1

print(res)