names = ['Gabriel', 'Thais', 'Paulo', 'Rose']

#? Enumerate prints both the index and the value from the list
""" Example:
0 Gabriel
1 Thais
2 Paulo
"""

for name in names:
    print(name)

#? Above is the vanilla code
#* Best practice:

for index, name in enumerate(names):
    print(index, name)

#* It can be started at a chosen number by changing enumerate to
#? enumerate(names, start=1)



