a = open('input.txt', 'r'). read()
file = open('output1.txt', 'w+')
file.write(str(a.count('(')-a.count(')')))
file.close()