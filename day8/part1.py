import re
a = open('input.txt', 'r')
file = open('output1.txt', 'w+')
cod = 0
b = 0
c = 0
def memory(string):
    mem = string[1:-1]
    mem = mem.replace("\\\\", "x")
    mem = mem.replace("\\\"", "x")
    mem, _  = re.subn('\\\\x..', 'x', mem)
    return len(mem)
def esc(string):
    escaped = string
    escaped = escaped.replace("\\", "\\\\")
    escaped = escaped.replace('"', '\\"')
    escaped = '"' + escaped + '"'
    return len(escaped)
for line in a:
    chars = len(line)
    mem = memory(line)
    escaped = esc(line)
    cod += len(line)
    b += memory(line)
    c += escaped
file.write(str(cod - b))
file.close()