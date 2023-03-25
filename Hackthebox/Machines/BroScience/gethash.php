<?php

$db_salt = "NaCl";
$handle = print_r(fopen("/home/banua/Desktop/Tools/rockyou.txt", "r"));
echo $handle;


// if ($handle) {
//     while (($line = fgets($handle)) !== false) {
//         // process the line read.

//         echo md5($db_salt . $line);
//         echo "\n";
//         if (strpos("bd3dad50e2d578ecba87d5fa15ca5f85", md5($db_salt . $line)) !== false){
//         	echo "True\n";
//         	break;
//         } else {
//         	echo "False\n";
//         }
//     }

//     fclose($handle);
// }

?>