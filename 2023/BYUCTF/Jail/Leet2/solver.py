import re

a = 0
while a < 10000000:
    inp = hex(a)
    a += 1
    if re.search(r'[123456789]', inp) or re.search(r'\(', inp) or eval(inp) != 1337:
        print('Nope')
    else:
        print(inp)
        print(FLAG)
        break