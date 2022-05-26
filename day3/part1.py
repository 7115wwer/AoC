a = open('input.txt', 'r'). read()
file = open('output1.txt', 'w+')
x = 0
y = 0
b = []
for i in a :
    f = [x,y]
    if (i == '^') :
        y += 1
    if (i == '>') :
        x += 1
    if (i == 'v') :
        y -= 1
    if (i == '<') :
        x -= 1
    b.append(f)
c = []
for g in b :
    if g not in c :
        c.append(g)
file.write (str(len(c)))
file.close ()