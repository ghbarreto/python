from random import choice

a = 700
for i in range (1, 1000):
    a = choice([0, i])

print(a)