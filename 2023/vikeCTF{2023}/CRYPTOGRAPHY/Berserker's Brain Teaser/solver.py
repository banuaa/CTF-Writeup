import random

"""
result = alphabet[(offset + rotation) % len(alphabet)]
result = alphabet[(a + b) % c]

So, the formula is 

(a + b) % c = d
b % c = d - a
b = (d - a) % c
"""

def getKey():
	ciphertext = "zexqSNE"
	plaintext = "vikeCTF"

	offsetPT = [alphabet.find(c.lower()) for c in plaintext]
	offsetCT = [alphabet.find(c.lower()) for c in ciphertext]

	d = offsetCT
	a = offsetPT
	c = len(alphabet)

	key = []
	for i in range(7):
		rotation = (d[i] - a[i]) % c
		key.append(rotation)
		
	return key


alphabet = "abcdefghijklmnopqrstuvwxyz"

ciphertext = "zexqSNE{cVaLuM_xRxBuRs_vE_mTtAe_ToOiN_oEiK}"

flag = ""
key = getKey()

for i, c in enumerate(ciphertext):
	if not c.isalpha():
		flag += c
		continue

	offset = alphabet.find(c.lower())
	rotation = key[i % len(key)]
	
	result = alphabet[(offset - rotation) % len(alphabet)]
	if c.islower():
		flag += result
	else:
		flag += result.upper()

print(flag)