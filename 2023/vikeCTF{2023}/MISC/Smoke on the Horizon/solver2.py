import subprocess
from string import *

char = "lLoOtT1234567890!"

for a in printable:
	for b in printable:
		for c in printable:
			for d in printable:
				password = f"p!ll@ge_{a}{b}{c}{d}_p1und3r"

				decrypt = subprocess.Popen(f"./decrypt flag.enc {password}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				readFlag = subprocess.Popen(f"cat flag.enc.dec", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				out,err = readFlag.communicate()
				print(out)
				# try:
				# 	if b"" in out:
				# 		pass
				# 	else:
				# 		print(out.decode("utf-8"))
				# except:
				# 	pass