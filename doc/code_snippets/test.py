def update_string(url, a, b):
    res = url + '{' + a + '}search{' + b + '}'
    print(res)

# known_worlds = ['trace']

# know_l = ['t','r','a','c','e']
# new_in = 'react' #get_anagrams('nuno') # --> []
# p =[]
# for i in know_l: # i = 't'
#     for j in new_in: # new_in.split() = ['n', 'u', 'n', 'o'] ; j = 'n'
#         if i == j:
#             p = p.insert(i) # p = []
#     if p == known_worlds[0]: # 
#         known_words.append(new_in)
# print(known_worlds[0])

in_url = "https://www.test.com/api&search"
a = "one"
b = "two"
update_string(in_url,a,b)