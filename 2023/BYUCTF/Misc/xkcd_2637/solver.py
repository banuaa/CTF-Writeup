from pwn import *

io = remote("byuctf.xyz", 40014)

# io.recvuntil(b"Get 500 problems correct to get the flag!\n")

io.recvuntil(b"get the flag!\n")
calc = io.recv().decode().split("=")[0]
print(calc)
answer = eval(calc)
print(answer)

io.sendline(str(answer).encode())


print(io.recv())

io.close()