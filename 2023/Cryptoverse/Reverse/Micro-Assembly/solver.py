flag = [
    3, # MOV  $3, -4(%BP)
    286, # MOV  $286, -8(%BP)
    66, # MOV  $66, -12(%BP)
    228, # MOV  $228, -16(%BP)
    16, # MOV  $16, -20(%BP)
    16, # MOV  $16, -24(%BP)
    154, # MOV  $154, -28(%BP)
]

# @if0:
#    DIV  -28(%BP), $2, %0
#    CMP  %12, $0
#    JNE  @false0
if (flag[6] / 2 != 0): # @false0
    # @true0:
    #    DIV  -28(%BP), $2, %0
    #    MOV  %0, -28(%BP)
    #    JMP  @exit0
    flag[6] = flag[6] / 2
else:
    pass

# @exit0:
#    MUL  -24(%BP), $3, %0
#    ADD  %0, $1, %0
#    MOV  %0, -24(%BP)
#    SHL  -20(%BP), $2, %0
#    ADD  %0, $3, %0
#    MOV  %0, -20(%BP)
flag[5] = (flag[5] * 3) + 1
flag[4] = (flag[4] << 2) + 3

# @if1:
#    DIV  -16(%BP), $3, %0
#    CMP  %12, $1
#    JNE  @false1
if (flag[3] / 3 == 1):
    # @true1:
    #    SUB  -16(%BP), $1, %0
    #    DIV  %0, $3, %0
    #    MOV  %0, -16(%BP)
    #    JMP  @exit1
    flag[3] = (flag[3] - 1) / 3
else:
    # @false1:
    #     DIV  -16(%BP), $2, %0
    #     MOV  %0, -16(%BP)
    flag[3] = flag[3] / 2

# @exit1:
#    SUB  -12(%BP), $2, %0
#    MOV  %0, -12(%BP)
flag[2] = flag[2] - 2

# @if2:
#    DIV  -8(%BP), $3, %0
#    CMP  %12, $1
#    JNE  @false2
if (flag[1] / 3 == 1):
    # @true2:
    #     SUB  -8(%BP), $1, %0
    #     DIV  %0, $3, %0
    #     MOV  %0, -8(%BP)
    #     JMP  @exit2
    flag[1] = (flag[1] - 1) / 3
else:
    # @false2:
    #     DIV  -8(%BP), $2, %0
    #     MOV  %0, -8(%BP)
    flag[1] = flag[1] / 3 # / 2 # Maybe Wrong, Change it to 3
    
# @exit2:
#    SHL  $11, -4(%BP), %0
#    ADD  %0, $11, %0
#    MOV  %0, -4(%BP)
#    LEA  -28(%BP), %0
#    MOV  %0, %13
#    JMP  @main_exit
flag[0] = (11 << flag[0]) + 11

f = "cvctf{"
for x in flag[::-1]:
    f += chr(int(x))
    print(str(int(x)) + " " + f + " ()" + chr((int(x))))

f += "}"
print(f)
