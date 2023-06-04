from os import urandom




# for _ in range(32):
#     for i, c in enumerate(urandom(6) * 3):
#         flag[i] = flag[i] ^ c

# print(f"{flag = }")

while True:
    flag = bytearray(b'\x05p\x07MS\xfd4eFPw\xf9}%\x05\x03\x19\xe8')
    for c in range(256):
        for _ in range(32):
            flag[0] = flag[0] ^ c
            print(chr(flag[0]))