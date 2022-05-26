import itertools
a = open('input.txt', 'r')
file = open('output1.txt','w+')
b = 999999
c = {}
locations = []
for i in range(28):
    stroka = a.readline()
    array = stroka.split()
    otkuda = array[0]
    kuda = array[2]
    doroga = int(array[4])
    c[otkuda + kuda] = doroga
    c[kuda + otkuda] = doroga
    locations.append(otkuda)
    locations.append(kuda)
locations = set(locations)
for i in itertools.permutations(locations):
    dlina = 0
    for gorod1, gorod2 in zip(i[:-1], i[1:]):
        dlina += c[gorod1 + gorod2]
    if dlina < b:
        b = dlina
file.write(str(b))
file.close()