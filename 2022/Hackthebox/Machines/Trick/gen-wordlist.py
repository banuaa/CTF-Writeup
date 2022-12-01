file = open('custom-wordlist.txt', 'r').readlines()
pad = 'preprod-'
new = ''
for i in file:
	new += pad+i

with open('custom-wordlist2.txt', 'w') as f:
	f.write(new)