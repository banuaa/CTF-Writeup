from Crypto.Util.number import *

def sub_77A(a1, a2):
	return (a1 << a2) | (a1 >> (-a2 & 7))

v8 = [_ for _ in range(3)]
v8[0] = 0x26666FE8EA686A28
v8[1] = 0xAEE8EBE666666666
v8[2] = 0xEBA5EB4E666E6E66

print(long_to_bytes(v8[0])[1] << 3)