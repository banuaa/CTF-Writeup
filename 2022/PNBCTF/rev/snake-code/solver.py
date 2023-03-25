file = open('flag.enc', 'r').read()
enc = []
for i in file:
	chr_e = int(ord(i) ^ 69) % 5000
	enc.append(chr(chr_e))

flag = ''.join(enc)
print(flag)