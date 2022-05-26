a = open('input.txt', 'r')
file = open('output1.txt', 'w+')
b = 0
def func():
    l,w,h = (int(x) for x in line.split('x'))
    array = [l, w, h]
    area = 2* l * w + 2 * w * h + 2 * h * l
    array.remove(max(array))
    smallarea = array[0]*array[1]
    answer = area+smallarea
    return answer
for x in range(1000):
    line = a.readline()
    b += int(func())
    if not line:
        break
file.write(str(b))
file.close()