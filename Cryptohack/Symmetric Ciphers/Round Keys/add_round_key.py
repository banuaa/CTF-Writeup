state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    state = [x for a in s for x in a]
    round_key = [y for b in k for y in b]
    #XOR
    return ''.join(chr(x ^ y) for x,y in zip(state,round_key))


print(add_round_key(state, round_key))

