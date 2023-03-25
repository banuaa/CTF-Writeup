import os
import subprocess

char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&_"
for i in char:
	for j in char:
		for d in char:
			for e in char:
				password = f"p!ll@ge_{i}{j}{d}{e}_p1und3r"
				os.system(f"./decrypt flag.enc {str(password)}")

				output = subprocess.check_output("strings flag.enc.dec", shell=True)
				print(output)
				if b"\n" not in output:
					with open("got_flag.txt", "wb") as f:
						f.write(output)

					print(output)
					break