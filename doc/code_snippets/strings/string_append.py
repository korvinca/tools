if __name__ == '__main__':
    n = int(input())
    res = ""
    if n == 1:
        res = "1"
    else:
        for i in range(1,n):
            res += str(i)
        res += str(n)
    print(res)