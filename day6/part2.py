import numpy as np
g = open('input.txt', 'r')
file = open('output2.txt', 'w+')
array = np.zeros((1000, 1000))
for s in g:
    a = s.split()
    if a[0] == 'turn':
        x, y = a[2].split(',')
        z, w = a[4].split(',')
        x, y, z, w = int(x), int(y), int(z), int(w)
        if a[1] == 'on':
            array[x:z+1, y:w+1] += 1
        elif a[1] == 'off':
            array[x:z+1, y:w+1] += -1
            array[array < 0] = 0
    else:
        x, y = a[1].split(',')
        z, w = a[3].split(',')
        x, y, z, w = int(x), int(y), int(z), int(w)
        array[x:z+1, y:w+1] += 2

file.write(str(np.sum(array)))
file.close()