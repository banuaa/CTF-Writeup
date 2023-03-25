from pwn import *

DEBUG = True

binary = "gdbme"
e = ELF(binary)
p = None

gdbscripts = """
break *main+99 
run 
jump *main+104"""

p = process(binary)
gdb.attach(p.pid, gdbscripts)