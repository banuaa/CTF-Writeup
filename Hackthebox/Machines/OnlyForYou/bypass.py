import re

email = "tes@email.com|sleep 5"

if not re.match("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})", email):
	print("FALSE")
else:
	domain = email.split("@", 1)[1]
	print(domain)