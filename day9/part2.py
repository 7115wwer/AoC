import itertools
a = open('input.txt', 'r')
file = open('output2.txt','w+')
b = 0
c = {}
locations = []
for i in range(28):
    z = a.readline()
    array = z.split()
    x = array[0]
    k = array[2]
    d = int(array[4])
    c[x + k] = d
    c[k + x] = d
    locations.append(x)
    locations.append(k)
locations = set(locations)
for i in itertools.permutations(locations):
    dlina = 0
    for gorod1, gorod2 in zip(i[:-1], i[1:]):
        dlina += c[gorod1 + gorod2]
    if dlina > b:
        b = dlina
file.write(str(b))
file.close()