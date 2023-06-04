char = "MOabcdefghijklmnopqrstuvwxyz}{0123456789"
ct = "mo%&'()*+,-./0123456789:;<=>}{[\\]^_ !\"#$"

getChar = dict(zip(char, ct))
flag = ""

#8.',27h,'8*{;8m33[o[3[3[%")#*\}
encFlag = "8.'8*{;8m33[o[3[3[%\")#*\\}"

for c in encFlag:
	for k, v in getChar.items():
		if c == v:
			print(k, end="")