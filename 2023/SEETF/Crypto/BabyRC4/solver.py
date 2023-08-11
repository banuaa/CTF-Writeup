from pwn import xor

c0 = bytes.fromhex('b99665ef4329b168cc1d672dd51081b719e640286e1b0fb124403cb59ddb3cc74bda4fd85dfc')
c1 = bytes.fromhex('a5c237b6102db668ce467579c702d5af4bec7e7d4c0831e3707438a6a3c818d019d555fc')

pl = "a"*36
C = [a ^ j for a,j in zip(c0, c1)]
M = [ord(i) for i in pl]

flag = ''.join([chr(i ^ j) for i,j in zip(M, C)])
print('SE'+flag[::-1])