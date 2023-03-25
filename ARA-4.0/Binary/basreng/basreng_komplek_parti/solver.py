from pwn import *

offset = "A"*(64+8)
offset += "C"*8

print(offset)
