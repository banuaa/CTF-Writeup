# umassdining2 [481 pts]

**Category:** we
**Solves:** 23

## Description
>The much awaited sql to the UMass Dining experience. We\re back and better than ever, join our super fan contest for a chance to be crowned "The UMassDining Enjoyer"\r\n\r\n[umassdining2.zip](https://umass-ctf-challenges.s3.amazonaws.com/web/umassdining2.zip)\r\n\r\nAuthor:  Ayman#5138

**Hint**
* -

## Solution
```
Review Source Code:
index.js: File upload dengan endpoint /submit, terdapat validasi ext .png, path-dir dengan md5 hash dari username, serta pemanggilan fungsi getSub() dari admin.js
admin.js: Bot akan melakukan pengecekan http://127.0.0.1:${process.env.SERVER_PORT}/admin_dashboard?user=${user}&upload=${upload}
header.html: Terdapat CSP default-src: 'self'
Flag: Di page /dashboard_admin

Solusi:
Javascript File Upload untuk bypass CSP, File upload berisi document.location untuk steal cookie
Bikin 2 User Untuk:
User pertama digunakan sebagai file upload dengan username normal, untuk mendapatkan hash md5 sebagai path dir file yang di upload.
User kedua digunakan untuk trigger XSS dengan username berisi <script src='/uploads/{user_hash}/file-upload.js'></script>
```

### Flag

