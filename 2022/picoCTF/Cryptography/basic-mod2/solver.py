from Crypto.Util.number import *
from string import ascii_uppercase, digits

with open("message.txt", "r") as f:
	file = f.read()

char = ascii_uppercase + digits + "_"
flag = "picoCTF{"
for i in file.split():
	mod = pow(int(i), -1, 41)
	if mod <= 26:
		flag += char[mod-1]
	elif mod >= 27 <= 36:
		flag += char[mod-1]
	else:
		flag += char[37]

print(flag+"}")
	