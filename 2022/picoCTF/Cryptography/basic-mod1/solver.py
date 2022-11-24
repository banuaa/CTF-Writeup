from string import ascii_uppercase, digits

file = open("message.txt", "r").read().split()

char = ascii_uppercase+digits+"_"
flag = "picoCTF{"
for i in file:
	mod = (int(i) % 37)
	if mod <= 25:
		flag += char[mod]
	elif mod >= 26 <= 35:
		flag += char[mod]
	else:
		flag += char[mod]
print(flag+"}")