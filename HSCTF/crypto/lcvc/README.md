## Diketahui
Ciphertext
> "mawhxyovhiiupukqnzdekudetmjmefkqjgmqndgtnrxqxludegwovdcdmjjhw"

Alphabet yang digunakan
> "abcdefghijklmnopqrstuvwxyz"

Dan juga proses enkripsi flag, namun yang paling menarik ada disini
> ciphertext += alphabet[(alphabet.index(character)+state)%26]

## Solusi
Karena ciphertext didapatkan dengan menambahkan huruf dari alphabet dengan index dari character flag `ditambah (+)` state kemudian di modulus 26
Kita cukup melakukan reverse dengan cara mengubah `+ menjadi -` dan mendapatkan flagnya
> ciphertext += alphabet[(alphabet.index(character)-state)%26]

flag = flag{iguessthisiswhatyouwouldcallalinearcongruentialvigenerecipher}