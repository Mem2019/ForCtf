from numpy import *

key_matrix = [[0x22,0x2e,0x92,0x6e,0xc9],
			[0x56,0x57,0x9,0xff,0x7c],
			[0x5a,0xe2,0x34,0xf7,0xde],
			[0x39,0x67,0x99,0xd2,0xaf],
			[0xbe,0xd4,0x2d,0x45,0x7a]]

encode_mat = dot(key_matrix, key_matrix)

def find_flag(key):
	assert (len(key) == 25)
	flag = []
	i = 0
	while i < 25:
		solution = linalg.solve(encode_mat, key[i:i+5])
		for j in xrange(0, 5):
			flag.append(solution[j] * 0x101 * 0x101 % 0x101)
		print solution
		i += 5
	return flag

res = dot(encode_mat, [0x30, 0x31, 0x32, 0x33, 0x34])
for x in xrange(0,5):
	print hex(res[x] % 0x101)


print find_flag([ 243, 90, 187, 253, 163, 14, 64, 186, 103, 24, 49, 219, 234, 201, 149, 155, 76, 122, 21, 104, 176, 28, 56, 141, 204])