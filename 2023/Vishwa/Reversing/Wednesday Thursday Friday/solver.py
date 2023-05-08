from itertools import product

#s = "vishwaCTF{xxxxxxxxxxxxxxxxxxxxxxx}"
s = "vishwaCTF{N3V3r_60NN4_61V3_Y0U_Ux}"

missing_indices = [x for x in range(32, 34)]

for chars in product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789}{_', repeat=len(missing_indices)):
    s_list = list(s)
    for i, char in zip(missing_indices, chars):
        s_list[i] = char
    s = ''.join(s_list)
    # print(s)

    if (
    	# Percobaan 1
    	# ord(s[3]) + ord(s[4]) + ord(s[1]) + ord(s[7]) - ord(s[8]) * ord(s[2]) * ord(s[6]) * ord(s[5]) - ord(s[11]) - ord(s[9]) - ord(s[10]) == -52316790 and
    	# ord(s[3]) - ord(s[4]) - ord(s[6]) + ord(s[9]) + ord(s[8]) * ord(s[11]) * ord(s[10]) - ord(s[2]) + ord(s[5]) + ord(s[7]) * ord(s[12]) == 285707 and
    	# ord(s[11]) + ord(s[10]) * ord(s[4]) + ord(s[3]) - ord(s[12]) * ord(s[7]) - ord(s[13]) - ord(s[5]) * ord(s[9]) * ord(s[6]) + ord(s[8]) == -797145
    	
    	# Percobaan 2
    	# ord(s[4]) + ord(s[12]) - ord(s[7]) * ord(s[11]) - ord(s[9]) - ord(s[5]) * ord(s[6]) - ord(s[14]) - ord(s[8]) * ord(s[13]) * ord(s[10]) == -289275 and
    	# ord(s[13]) + ord(s[14]) + ord(s[7]) + ord(s[6]) - ord(s[12]) - ord(s[15]) * ord(s[11]) - ord(s[5]) + ord(s[8]) * ord(s[10]) * ord(s[9]) == 666868 and
    	# ord(s[12]) + ord(s[15]) * ord(s[16]) + ord(s[11]) + ord(s[13]) - ord(s[10]) + ord(s[6]) * ord(s[8]) - ord(s[7]) - ord(s[9]) + ord(s[14]) == 9837
    	
    	# Percobaan 3
    	# ord(s[7]) + ord(s[11]) - ord(s[8]) + ord(s[16]) * ord(s[13]) - ord(s[17]) - ord(s[14]) - ord(s[9]) + ord(s[10]) * ord(s[15]) - ord(s[12]) == 9858 and
    	# ord(s[17]) + ord(s[12]) + ord(s[9]) - ord(s[18]) - ord(s[8]) - ord(s[15]) + ord(s[16]) + ord(s[11]) * ord(s[14]) * ord(s[13]) - ord(s[10]) == 296504 and
    	# ord(s[11]) * ord(s[13]) * ord(s[18]) * ord(s[16]) - ord(s[17]) - ord(s[10]) + ord(s[9]) + ord(s[15]) * ord(s[12]) - ord(s[19]) - ord(s[14]) == 10963387
    	
    	# Percobaan 4
		# ord(s[17]) + ord(s[16]) + ord(s[20]) + ord(s[12]) - ord(s[14]) * ord(s[18]) * ord(s[15]) * ord(s[19]) - ord(s[13]) - ord(s[11]) - ord(s[10]) == -65889660 and
		# ord(s[16]) - ord(s[19]) - ord(s[15]) + ord(s[11]) * ord(s[13]) + ord(s[18]) + ord(s[21]) * ord(s[12]) + ord(s[14]) + ord(s[17]) * ord(s[20]) == 13340 and
		# ord(s[18]) * ord(s[16]) + ord(s[17]) * ord(s[15]) - ord(s[20]) - ord(s[12]) - ord(s[19]) * ord(s[14]) + ord(s[22]) + ord(s[13]) * ord(s[21]) == 4641
		
		# Percobaan 5
		# ord(s[15]) + ord(s[20]) + ord(s[18]) + ord(s[21]) + ord(s[13]) * ord(s[19]) - ord(s[22]) - ord(s[16]) - ord(s[14]) + ord(s[17]) * ord(s[23]) == 6428 and
		# ord(s[19]) * ord(s[24]) + ord(s[15]) * ord(s[20]) + ord(s[16]) * ord(s[14]) + ord(s[23]) - ord(s[18]) * ord(s[21]) - ord(s[22]) * ord(s[17]) == 7851 and
		# ord(s[19]) + ord(s[24]) + ord(s[22]) + ord(s[21]) + ord(s[25]) + ord(s[16]) + ord(s[18]) + ord(s[20]) * ord(s[23]) - ord(s[15]) + ord(s[17]) == 2997

		# Percobaan 6
    	# ord(s[17]) * ord(s[23]) + ord(s[20]) * ord(s[25]) - ord(s[16]) + ord(s[26]) * ord(s[21]) - ord(s[24]) + ord(s[22]) * ord(s[19]) * ord(s[18]) == 342425 and
    	# ord(s[20]) + ord(s[26]) + ord(s[24]) * ord(s[17]) + ord(s[27]) * ord(s[22]) * ord(s[25]) - ord(s[21]) - ord(s[19]) * ord(s[18]) + ord(s[23]) == 243251 and
    	# ord(s[24]) + ord(s[22]) + ord(s[25]) * ord(s[21]) - ord(s[28]) - ord(s[19]) - ord(s[26]) * ord(s[27]) * ord(s[20]) - ord(s[23]) + ord(s[18]) == -434772
    	
    	# Percobaan 7
    	# ord(s[28]) + ord(s[19]) + ord(s[25]) + ord(s[29]) - ord(s[24]) - ord(s[21]) - ord(s[23]) + ord(s[27]) - ord(s[22]) * ord(s[26]) + ord(s[20]) == -4957 and
    	# ord(s[21]) + ord(s[30]) + ord(s[26]) + ord(s[22]) * ord(s[23]) - ord(s[29]) + ord(s[20]) - ord(s[24]) * ord(s[25]) - ord(s[27]) - ord(s[28]) == -1625 and
    	# ord(s[22]) + ord(s[26]) + ord(s[25]) + ord(s[30]) + ord(s[23]) - ord(s[24]) - ord(s[29]) - ord(s[31]) - ord(s[21]) - ord(s[27]) - ord(s[28]) == -144
    	
    	# Percobaan 8
    	ord(s[29]) + ord(s[30]) + ord(s[31]) - ord(s[26]) - ord(s[25]) - ord(s[23]) - ord(s[28]) - ord(s[27]) - ord(s[22]) - ord(s[32]) * ord(s[24]) == -7001 and
    	ord(s[33]) + ord(s[25]) - ord(s[31]) * ord(s[23]) + ord(s[27]) - ord(s[26]) * ord(s[32]) + ord(s[30]) - ord(s[24]) * ord(s[29]) - ord(s[28]) == -18763
    	):
    	print("CORRECT")
    	print(s)
