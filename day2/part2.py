a = open('input.txt', 'r')
file = open('output2.txt', 'w+')
b = 0
def func():
    l,w,h = (int(x) for x in line.split('x'))
    array = [l, w, h]
    c = l*w*h
    array.remove(max(array))
    d = (array[0]+array[1])*2
    answer = c+d
    return answer
for x in range(1000):
    line = a.readline()
    b += int(func())
    if not line:
        break
file.write(str(b))
file.close()