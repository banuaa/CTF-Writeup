import hashlib, json
from pwn import *

class Encoder():

    def __init__(self, secrets_file):
        with open(secrets_file, "r") as file:
            data = json.load(file)
            self.hashed_key = data["key"]
            self.secret = data["secret"]

    def hash(self, user_input):
        salt = "RITSEC_Salt"
        return hashlib.sha256(salt.encode() + user_input.encode()).hexdigest()

if __name__ == "__main__":
    API = Encoder("supersecret.json")
    password = ""
    for i in range(54700000,99999999):
        check = API.hash("{:08d}".format(i))
        # print(i)
        if check == API.hashed_key:
            password += str(i)
            print(f"[+] Got Passcode = {i} !!")
            break

    io = remote("guessthepassword.challenges.ctf.ritsec.club", 1337, level="error")
    io.sendline(password.encode())
    print(io.recvline().decode())
    print(io.recvline().decode())
    io.close()