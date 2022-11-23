for i in range(83):
	file = open(f'{i:02d}.txt').read().split()
	print(''.join(file), end='')
print()
