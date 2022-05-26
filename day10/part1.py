from itertools import groupby
a = open('input.txt', 'r'). read()
file = open('output1.txt', 'w+')
for i in range(40):
    a = ''.join([str(len(list(g))) + k for k, g in groupby(a)])
file.write(str(len(a)))
file.close()