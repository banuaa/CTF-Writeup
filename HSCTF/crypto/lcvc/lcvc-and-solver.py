#/usr/bin/python3

state = 1
flag = "flag{mawhxyovhiiupukqnzdekudetmjmefkqjgmqndgtnrxqxludegwovdcdmjjhw}"
alphabet = "abcdefghijklmnopqrstuvwxyz"

assert(flag[0:5]+flag[-1]=="flag{}")

ciphertext = ""
for character in flag[5:-1]:
    state = (15*state+18)%29
    #Change "+" to "-"
    #ciphertext+=alphabet[(alphabet.index(character)+state)%26]
    ciphertext+=alphabet[(alphabet.index(character)-state)%26]

print("flag{%s}"  % (ciphertext) )
