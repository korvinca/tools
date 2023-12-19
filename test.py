def simulate(entries):
    """
    :param entries: (list(int)) The numerical record files
    :returns: (list(int)) The record files after running the malware
    """
    hash = []
    tl = entries[0]
    tr = entries[-1]
    res = [tl]
    for i in range(1,len(entries)):
        if entries[i] <= tl or entries[i] < tr:
            hash.append(i)
    print(hash)
    for i in range(1,len(entries)):
        if i in hash:
            res.append(0)
        else:
            res.append(entries[i])
    return res

records = [1, 2, 0, 5, 0, 2, 4, 3, 3, 3]
print(simulate(records))
# Expected output
# [1, 0, 0, 5, 0, 0, 0, 3, 3, 0]