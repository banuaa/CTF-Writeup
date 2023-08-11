#!/usr/bin/python3

import random

# ===================================================================================================
# random.seed(''.join([str(random.randint(0x0, 0x9)) for i in range(random.randint(3, 6))]))
# theKey = [random.randint(0, 255) for i in range(len(flag))]
# theEnc = "".join([hex(((random.choice(theKey)) ^ ord(flag[i]))<<1) for i in range(len(flag))])
# open('out.txt', 'w').write(theEnc)
# ===================================================================================================

encflag = [
    0x5e, 0x1d4, 0x194, 0xcc, 0xca, 0x13a, 0x134, 0xea, 0xd4, 0x19a,
    0x122, 0x156, 0x1c4, 0xca, 0x88, 0x9c, 0x168, 0x122, 0x22, 0x1d2,
    0xd0, 0x1b0, 0x1c0, 0xd2, 0xb8, 0x1a, 0xea, 0x106, 0x108, 0xd2,
    0x7e, 0x1ce, 0x92, 0x1b0, 0x8a, 0x76, 0x1ac, 0x142, 0x1fe, 0xd2,
    0x12a, 0x14c, 0x34, 0x4c, 0x1d0, 0x106, 0x44, 0x34, 0x7a, 0x1b0
]

for i in range(999999):
	random.seed(str(i))
	theKey = [random.randint(0, 255) for i in range(len(encflag))]
	stored = ""
	for j in range(len(encflag)):
		stored += (chr((encflag[j] >> 1) ^ random.choice(theKey)))
		if "flag" in stored:
			print(stored)