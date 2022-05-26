a = open('input.txt', 'r'). read()
file = open('output2.txt', 'w+')
x1 = 0
y1 = 0
x2 = 0
y2 = 0
massiv = []
for i in a[0::2] :
    f = [x1,y1]
    if (i == '^') :
        y1 += 1
    if (i == '>') :
        x1 += 1
    if (i == 'v') :
        y1 -= 1
    if (i == '<') :
        x1 -= 1
    massiv.append(f)
for g in a[1::2] :
    f = [x2,y2]
    if (g == '^') :
        y2 += 1
    if (g == '>') :
        x2 += 1
    if (g == 'v') :
        y2 -= 1
    if (g == '<') :
        x2 -= 1
    massiv.append(f)
piska = []
for q in massiv :
    if q not in piska :
        piska.append(q)
file.write (str(len(piska)))
file.close ()