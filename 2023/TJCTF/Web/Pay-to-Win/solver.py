from base64 import b64encode, b64decode
import hashlib
import random
import json

def hash(data):
    return hashlib.sha256(bytes(data, 'utf-8')).hexdigest()

data = {
    "username": "banua",
    "user_type": "basic"
}

b64data = b64encode(json.dumps(data).encode())

gotNumber = ""
knownHash = "a658be0e0b42c90693d824a82a7314af4f0e8ac9d462318e201a74f062b12342"
i = 300000
while i < 16777215:
    data_hash = hash(b64data.decode() + hex(i)[2:])
    print(i)
    print(data_hash)
    if data_hash == knownHash:
        gotNumber += str(i)
        print(f"[+] Got hash getrandbits = {i}")
        break
    i += 1

print("[+] Create New Hash for Premium User Type")

dataNew = {
    "username": "banua",
    "user_type": "premium"
}

b64dataNew = b64encode(json.dumps(dataNew).encode())
new_hash = hash(b64dataNew.decode() + hex(int(gotNumber))[2:])
print(f"[+] Got New Hash! {new_hash}")
print(f"[+] Got New Data JWT! {b64dataNew}")