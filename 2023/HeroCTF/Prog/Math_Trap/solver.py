#!/usr/bin/env python3
from pwn import *

def Calc(arg1,arg2,opr):
	result = ""
	if opr == "+":
		result = arg1 + arg2
	elif opr == "-":
		result = arg1 - arg2
	elif opr == "*":
		result = arg1 * arg2
	else:
		result = arg1 // arg2
	return result

p = remote('static-01.heroctf.fr', 8000)

p.recvuntil(b"Can you calculate these for me ?\n\n")

for i in range(100):
	print(i)
	calc = p.recvline().decode().split()
	try:
		answer = str(Calc(int(calc[0]), int(calc[2]), calc[1])).encode()
		print(f"The answer is : {answer}")
		
		p.sendline(answer)

	except:
		pass

	p.recvline()

print(p.recv().decode())