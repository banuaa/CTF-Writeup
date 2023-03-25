#!/usr/bin/python3

import r2pipe
import json

flag = ""
for i in range(590):
	r2p = r2pipe.open("./bertanya{}".format(str(i)))
	r2p.cmd("aaa")

	t = r2p.cmd("aflj")
	d = json.loads(t)
	fc_name = d[0]["name"]
	if fc_name == "entry0":
		fc_name = d[0]["name"]

	# Get operation XOR / ADD / SUB and the value
	t = r2p.cmd("pdj 10@%s" %( fc_name))
	d = json.loads(t)
	xoraddsub = d[9]["opcode"]
	print(xoraddsub)
	cal = int(xoraddsub.split(', ')[1],16)
	print(cal)

	# Get value of CMP
	t = r2p.cmd("pdj 11@%s" %( fc_name))
	d = json.loads(t)
	ins = d[10]["opcode"]
	comp = int(ins.split(', ')[1],16)
	print(comp)

	if "xor" in xoraddsub:
		flag += chr((comp ^ cal) & 0xFF)
	if "add" in xoraddsub:
		flag += chr((comp - cal) & 0xFF)
	if "sub" in xoraddsub:
		flag += chr((comp + cal) & 0xFF)
print(flag)
