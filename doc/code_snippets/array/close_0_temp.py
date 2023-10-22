

def closestToZero(ts):
    ts.sort()
    print(len(ts))
    # print(ts)
    for i in ts:
        if i > 0:
            pos_inx = ts.index(i)
            # print(i)
            neg_ing = ts[pos_inx-1]*-1
            # print(neg_ing)
            if neg_ing > i :
                return i
            else :
                return ts[pos_inx-1]
            break

ts = [7,-10,13,8,4,-7.2,-12,-3.7,3.5,-9.6,6.5,-1.7,-6.2,7]

result = closestToZero(ts)
print(result)
