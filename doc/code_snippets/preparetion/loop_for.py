S = "abcdefg"
res_1 = ""
res_2 = ""
c = 1
for i in S :
    if c % 2 != 0:
        res_1 = res_1 + i
    else:
        res_2 = res_2 + i
    c += 1
print(res_1, res_2)