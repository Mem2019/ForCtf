# (input0-input1)*3+input0-input2 == 0xc0a3c68
# (input0-input1)*3+input0+input2 == 0xe8f508c8
# ((input0-input1)*4)+input0+input2 == 0xeaf917e2


MOD_NUM = 0x100000000

def isValid(x):
	return (x >= ord('a')-0 and x <= ord('z')+0) or (x >= ord('A')-0 and x <= ord('Z')+0) or (x >= ord('0')-0 and x <= ord('9')+0)

def validAns(iAns):
	iAns = iAns % 0x100000000
	return isValid(iAns & 0xFF) and isValid((iAns >> 8) & 0xFF) and isValid((iAns >> 16) & 0xff) and isValid((iAns >> 24) & 0xff)

def printAsHex(iInt):
	str = []
	str.append(chr(iInt & 0xff))
	str.append(chr((iInt >> 8) & 0xff))
	str.append(chr((iInt >> 16) & 0xff))
	str.append(chr((iInt >> 24) & 0xff))
	print "".join(str)


x1	=	1953723722
x2	=	1919903280
x3	=	1853187632


printAsHex(x1)
printAsHex(x2)
printAsHex(x3)