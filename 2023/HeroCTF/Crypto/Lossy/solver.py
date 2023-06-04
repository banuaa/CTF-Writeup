# from cryptography.hazmat.primitives.ciphers.algorithms import AES
# from cryptography.hazmat.primitives.ciphers import Cipher, modes

# def encrypt(pt, key):
# 	aes = Cipher(AES(key), modes.ECB())
# 	enc = aes.encryptor()
# 	ct  = enc.update(pt)
# 	ct += enc.finalize()
# 	return ct

# def decrypt(ct, key):
# 	aes = Cipher(AES(key), modes.ECB())
# 	dec = aes.decryptor()
# 	pt = dec.update(ct)
# 	pt += dec.finalize()
# 	return pt

ct  = bytes.fromhex('0e17c69a812e76d90e455a346c49e22fb6487d9245b3a90af42e67c7b7c3f28230')
key = bytes.fromhex('0eb5295cd71d2f7cedb377c2ab6cb930')

# print(decrypt(ct, key))

from Crypto.Cipher import AES

aes = AES.new(key, AES.MODE_ECB)
pt = aes.decrypt(ct)
print(pt)