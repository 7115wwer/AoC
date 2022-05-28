a = open('input.txt','r').read().split()
file = open('output1.txt', 'w+')
n = int(a[0])
del a[0]
b=list(a)
p = 0
i = 1
r = 0
l = 0
h = 0
j = 0
print(a)
while i<n:#начинаем цикл пока, чтобы перебрать все возможные варианты
    k = str(a[0])
    i = i +1
    for g in range(len(a)): # Здесь мы находим наименьшее число и его индекс в массиве
        if a[g] != 'r' or 'l' :
            k = a[0]
            if k>a[g]:
                k = a[g]
                p = g
    if a[p + 1] == 'l' or a[p + 1] == 'r': #Здесь мы выбираем варианты, когда люди уже возвращаются, чтобы соответсвовать условиям
        if a[p + 2] == 'l':
            l = l + 1
            a[p] = a[p] + str(100000) #В подобных строчках мы прибавляем число больше максимального, чтобы они больше не разбирались в цикле
        else:
            r = r + 1
            a[p] = a[p] + str(100000)
    else: # Здесь уже отбор со случаями, когда люди заходят на сцену
        if a[p + 2] == 'l':
            if l > 0:
                l = l - 1
                a[p] = a[p] + str(100000)
            else:
                h = h + 1
                a[p] = a[p] + str(100000)
        else:
            if r > 0:
                r = r - 1
                a[p] = a[p] + str(100000)
            else:
                j = j + 1
                a[p] = a[p] + str(100000)
file.write(str(h))
file.write(str(' '))
file.write(str(j))
file.close()