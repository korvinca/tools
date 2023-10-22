"""
Update cash
"""


def update_cache(cache,m,n,v = None):
    if m == "get":
        cache[n] = 0
    else:
        cache[n] = v
    #     if len(cash) < n:
    #         cash.add(k)
    # elif m == "put":
    #     for i in cash:
    #         if k == i:
    #             cash.update(k)
    #             return cash
    #     if len(cash) < n:
    #         cash.update(k)
    #     else:
    #         cash.pop(k[0])
    #         cash.update(k)
    return cache

cache = {}
cache[1] = 0
cache[2] = 0
cache[3] = 0

print(cache)
return_cache = update_cache(cache, "get", 1)
print(str(return_cache))

return_cache = update_cache(cache, "put", 2, 10)
print(str(return_cache))