import os

for i in range(53):
	os.system(f"fcrackzip -D -p /usr/share/wordlists/rockyou.txt -u flag{i:02d}.zip >> password.txt")

file = open("password.txt", "r").read().replace("PASSWORD FOUND!!!!: pw == ", "").split()

for i in range(len(file)):
	os.system(f"unzip -j -P {file[i]} flag{i:02d}.zip")

for i in range(53):
	file = open(f"flag{i:02d}").read()
	print(file, end='')

#itf{g0t_b4mb00zl3d_4g41n_lmao_c0ngr4ts_y0u_w0n_4g41n}