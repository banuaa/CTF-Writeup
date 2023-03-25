def decrypt(ct):
    result = ""
    for i in range(len(ct)):
        result += chr(int(ct[i],16) ^ 93)

    return result


ct = ['2b','34','36','38','1e','09','1b','26','33','6d','02','68','6a','0f','6c','33','64','68','02','1b','6d','2f','02','04','6d','28','20']

print(decrypt(ct))