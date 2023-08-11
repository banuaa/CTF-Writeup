from pwn import xor

with open('output.txt', 'rb') as (f):
    enc = f.read()

a = enc[0:len(enc) // 3]
b = enc[len(enc) // 3:2 * len(enc) // 3]
c = enc[2 * len(enc) // 3:]

c = xor(c, int(str(len(enc))[0]) * int(str(len(enc))[1]))

ac = xor(c,a)
c = xor(b, c)

a = xor(a, int(str(len(enc))[0]) + int(str(len(enc))[1]))
a = xor(c, a)

b = xor(b, c)

print(a + b + ac)