spam = ['apples', 'bananas', 'tofu', 'cats']

# print(str(spam[:-1])) # + ' and ' + spam[-1], sep= ' ')

r = len(spam) -1
for i in range(0, r):
    print(spam[i] +  ', ' , sep= ' ', end='')

print('and ' + spam[-1])
