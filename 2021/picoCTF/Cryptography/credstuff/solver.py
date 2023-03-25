import codecs

username = open("usernames.txt", "r").readlines()
password = open("passwords.txt", "r").readlines()

for i,j in zip(username,password):
	if "cultiris" in i:
		print(i,j)
		print(codecs.decode(j, "rot_13"))