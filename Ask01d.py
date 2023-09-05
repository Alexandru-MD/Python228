from random import choice

name = ""
a = ['A', 's', 'k', '0', '1', 'd']
while len(name) != 7:
    name += choice(a)
print(name)