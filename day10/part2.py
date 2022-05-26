from itertools import groupby
a = open('input.txt', 'r'). read()
file = open('output2.txt', 'w+')
for i in range(50):
    a = ''.join([str(len(list(g))) + k for k, g in groupby(a)])
file.write(str(len(a)))
file.close()