def Summation(n):
    if n <= 0 :
        # End of recrusion
        return 0
    else:
        # Keep going recrusion
        # print(n)
        return n + Summation(n - 1)

def Factorial(n):
    if n <= 1 :
        # End of recrusion
        return 1
    else:
        # Keep going recrusion
        # print(n)
        return n * Factorial(n - 1)
    
def Exponentiation(n, p):
    if p <= 0 :
        # End of recrusion
        return 1
    else:
        # Keep going recrusion
        # print(n)
        return n * Exponentiation(n, p - 1)

print(Summation(5))
print(Factorial(5))
print(Exponentiation(5, 5))
