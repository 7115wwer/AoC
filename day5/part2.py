a = open('input.txt', 'r')
file = open('output2.txt', 'w+')
b = 0
def f1() :
    for i in stroka :
        for p in stroka :
            if stroka.count(i+p) >= 2 :
                return True
    return False
def f2() :
    for i in range(len(stroka)-2) :
        if stroka[i] == stroka[i+2] :
            return True
    return False
for i in range(1000) :
    stroka = a.readline()
    if (f1() == True and f2() == True) :
        b += 1
file.write (str(b))
file.close ()