from Crypto.Util.number import *
from Crypto.Cipher import AES
from sympy import *
from pwn import *
import hashlib

io = remote("group.chal.uiuc.tf", 1337)
io.recvuntil(b"business??\n[$] Public:\n")
g = io.recvline().decode("utf-8").replace("[$]     ", "").replace("\n", "")
p = io.recvline().decode("utf-8").replace("[$]     ", "").replace("\n", "")
A = io.recvline().decode("utf-8").replace("[$]     ", "").replace("\n", "")

# if k == 1 or k == p - 1 or k == (p - 1) // 2:
k = totient(p.split("p = ")[1])

io.sendline(str(k).encode())
io.recvuntil(b"Ciphertext using shared 'secret' ;)\n")

c = io.recvline().decode("utf-8").replace("[$]     ", "").replace("\n", "")

io.close()

g = int(g.split("g = ")[1])
p = int(p.split("p = ")[1])
A = int(A.split("A = ")[1])
c = int(c.split("c = ")[1])

S = pow(A, k, p)

print(f"[+] K = {k}")
print(f"[+] S = {S}")

key = hashlib.md5(long_to_bytes(S)).digest()
print(f"[+] Key = {key}")
cipher = AES.new(key, AES.MODE_ECB)
flag = cipher.decrypt(long_to_bytes(c)).decode("utf-8")
print(f"[+] Flag = {flag}")