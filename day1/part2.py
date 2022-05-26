a = open('input.txt', 'r'). read()
file = open('output2.txt', 'w+')
b = 0
f = 0
for c in a:
    f += 1
    if (c == '('):
        b += 1
    if (c == ')'):
        b -= 1
    if (b == -1):
      break
file.write(str(f))
file.close()