
  #            40 RETURN_VALUE
  # 6     >>   38 LOAD_FAST                2 (temp)

  #            36 JUMP_ABSOLUTE           12
  #            34 STORE_FAST               2 (temp)
  #            32 INPLACE_ADD
  #            30 CALL_FUNCTION            1
  #            28 BINARY_XOR
  #            26 LOAD_CONST               1 (65)
  #            24 CALL_FUNCTION            1
  #            22 LOAD_FAST                3 (x)
  #            20 LOAD_GLOBAL              1 (ord)
  #            18 LOAD_GLOBAL              0 (chr)
  # 5          16 LOAD_FAST                2 (temp)

  #            14 STORE_FAST               3 (x)
  #       >>   12 FOR_ITER                24 (to 38)
  #            10 GET_ITER
  # 4           8 LOAD_FAST                0 (v)

  #             6 STORE_FAST               2 (temp)
  # 3           4 LOAD_CONST               2 ('')

  #             2 STORE_FAST               1 (a)
  # 2           0 LOAD_CONST               1 (65)

encFlag = open("hidden.txt", "rb").read()

a = 65
temp = []

for v in range(38):
  temp += [chr(x ^ 65) for x in encFlag]
print("".join(temp))