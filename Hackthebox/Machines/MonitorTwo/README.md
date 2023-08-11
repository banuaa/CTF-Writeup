## Solver
```
- Foothold:
Check website found Cacti version 1.2.22
Check CVE for Cacti 1.2.22 its vulnerable to Unauthenticated RCE
Using exploit from Exploit DB
Modify X-Forwarder-For value to 127.0.0.1
Run the exploit and gaining Shell

Its docker inside
upgrade shell with script
script -qc /bin/bash /dev/null

found cacti.sql inside /var/www/html
marcus   | $2y$10$vcrYth5YcCLlZaPDj6PwqOYTw68W1.3WeKlBn70JonsdW/MhFYK4C |     0 | Marcus Brune   | marcus@monitorstwo.htb

crack the hash with john
~/src/john/run/john hash.txt --wordlist=/home/banua/Desktop/Tools/rockyou.txt

Found password funkymonkey
SSH marcus with funkymonkey as passwd

We known before foothold inside docker and have overlay
Check docker version Docker version 20.10.5+dfsg1, build 55c4c88
Its vulnerable to CVE-2021-41091
Run and Got root

```