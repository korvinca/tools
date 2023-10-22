hash_set = set()
hash_set.add("test1")

if "test5" not in hash_set:
    hash_set.add("test5")

if "test1" in hash_set:
    print("true")

hash_set.remove("test1")

if "test1" not in hash_set:
    print("false")

#Dictionary
dict = {}
dict["test1"] = 23
print(dict)