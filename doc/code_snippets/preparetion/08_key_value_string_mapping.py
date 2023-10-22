# Read the number of entries in the phone book
n = int(input())

# Create an empty phone book dictionary
phone_book = {}

# Read and store phone book entries
for _ in range(n):
    entry = input().split()
    name, phone = entry[0], entry[1]
    phone_book[name] = phone

# Read and process queries until there is no more input
try:
    while True:
        query = input()
        if query in phone_book:
            print(query + "=" + phone_book[query])
        else:
            print("Not found")
except EOFError:
    pass
