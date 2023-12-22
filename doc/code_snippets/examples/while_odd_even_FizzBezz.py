def fizzBuzz(n):
    # Write your code here
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        if i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        if i % 3 != 0 and i % 5 != 0:
            print(i)
        i += 1
        
if __name__ == '__main__':
    # n = int(input().strip())
    n = 15
    fizzBuzz(n)