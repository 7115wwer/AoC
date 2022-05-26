
a = open('input.txt', 'r')
file = open('output1.txt', 'w+')
b = 0
def f1() :
    c = 'aeiou'
    ans = 0
    for i in range(len(stroka)) :
        if stroka[i] in c :
            ans += 1
    if ans >= 3 :
        return True
    return False
def f2() :
    for i in range(len(stroka)-1) :
        if stroka[i] == stroka[i+1] :
            return True
    return False
def f3() :
    sigl = ['ab','cd','pq','xy']
    for i in range(len(stroka)-1) :
        if (stroka[i] + stroka[i+1] in sigl) :
            return True
    return False
for i in range(1000) :
    stroka = a.readline()
    if (f1() == True and f2() == True and f3() == False) :
        b += 1
file.write (str(b))
file.close ()