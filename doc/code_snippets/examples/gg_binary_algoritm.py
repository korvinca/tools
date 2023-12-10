# Определите функцию f(a, x), 
# которая возвращала бы x, ближайшее наименьшее число или -1 в случае ошибки.
def f(a, x):
    if a is None or len(a) == 0 or x > a[-1] or x < a[0]:
        return -1
    else:
        answer = -1
        low = 0
        high = len(a) - 1
        while low <= high:
            mid = int((low + high) / 2)
            print(a[mid])
            if a[mid] == x:
                return x
            elif a[mid] < x:
                answer = a[mid]
                low = mid + 1
            else:
                high = mid - 1
    return answer
a = [ 3, 4, 6, 9, 10, 12, 14, 15, 17, 19, 21 ]
a = [ 20 ]
b = None
x = ""
print(f(a, 20))
# print(f(a, 12))
# print(f(a, 13))
# print(f(a, 19))
# print(f(a, 22))
# print(f(a, 3))
# print(f(a, 2))
# print(f(a, 21))
# print(f(a, -1))
# print(f(a, 0))
# print(f([], x))
# print(f(b, x))