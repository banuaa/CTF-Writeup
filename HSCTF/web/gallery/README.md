## Diketahui
Pada source code yang diberikan, image folder berada di `./images`, route `/flag` akan memanggil flag yang ada di `/flag.txt`, dan juga route `/image` dengan parameter `/image?image=` untuk memanggil file image yang ada di folder `images`.

Karena untuk menampilkan file nya menggunakan fungsi `flask.send_file` maka terdapat vulnerability yaitu Path Traversal seperti yang ada di sumber berikut
> https://huntr.dev/bounties/7acac778-5ba4-4f02-99e2-e4e17a81e600/

Namun, untuk memanggil file, file harus berada di direktori `/image`, harus menggunakan parameter `?image`, serta file ekstension harus `.jpg`.

## Solusi
Lakukan bypass dengan cara `.jpg` harus ada dan lakukan Path Traversal pada parameter `/image?image=` tersebut
> http://web1.hsctf.com:8003/image?image=.jpg../../../../flag.txt

Flag = flag{1616109079_is_a_cool_number}