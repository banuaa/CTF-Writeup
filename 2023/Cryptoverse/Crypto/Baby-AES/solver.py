from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import itertools

KEY_LEN = 2
BS = 16

iv = bytes.fromhex("1df49bc50bc2432bd336b4609f2104f7")
ct = bytes.fromhex("a40c6502436e3a21dd63c1553e4816967a75dfc0c7b90328f00af93f0094ed62")

def get_key(iv, ct):
    for key in itertools.product(range(256), repeat=KEY_LEN):
        key = pad(bytes(key),16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = cipher.decrypt(ct)
        if pt.startswith(b"cvctf"):
            return key

key = get_key(iv, ct)
print(f"Got Key => {key}")

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size)

print(f"Got Flag => {pt.decode()}")