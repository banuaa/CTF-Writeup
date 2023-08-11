from Crypto.Util.number import *
import os,random,struct
import sys

def parse_header(x):
	assert x[1:4] == b'PNG'
	signature = x[:16]
	w = struct.unpack(">I",x[16:20])[0]
	h = struct.unpack(">I",x[20:24])[0]
	crc = struct.unpack(">I", x[29:33])[0]
	new_crc = w * h * crc
	obj = random.SystemRandom()
	initial_seed = os.urandom(4)
	random.seed(obj.randrange(bytes_to_long(initial_seed)))
	new_w,new_h,new_crc = os.urandom(4),os.urandom(4),(new_crc * w * h * random.getrandbits(32))&0xffffffff
	return signature, new_w, new_h,new_crc

def traverse(x):
	count=0
	while b'IDAT' not in x[count+33:count+37]:
		count+=1
	random_data = os.urandom(count)
	return random_data,count

def transform(x):
	buf = open(x,"rb").read()
	sig, w, h, crc = parse_header(buf)
	assert len(w) == 4
	assert len(h) == 4
	assert len(struct.pack(">I",crc)) == 4
	xormask, count = traverse(buf)
	newbuf = ""
	for i in range(count):
		newbuf += chr((buf[33+i] ^ xormask[i])&0xff)
	rest = buf[count:-1]
	newbuffer = sig + w + h + struct.pack('>I',crc)+newbuf.encode()+rest
	with open(x+".enc","wb") as ff:
		ff.write(newbuffer)
		ff.close()
	print("[+] DONE!")
	os.remove(x)


print("Picturial Art v13.37\n================\n\nYour Fancy Image Beautifier")
img = input("Please input your image name (in the current directory) and we'll beautify it for you! :")
print("Thankyou we'll process your image!")
transform(img)
print("Done! But you got fooled. You lost your precious image ^-^")