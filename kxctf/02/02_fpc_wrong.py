
MOD_NUM = 0x100000000

def isValid(x):
	return (x >= ord('a')-0 and x <= ord('z')+0) or (x >= ord('A')-0 and x <= ord('Z')+0) or (x >= ord('0')-0 and x <= ord('9')+0)

def validAns(iAns):
	iAns = iAns % 0x100000000
	return isValid(iAns & 0xFF) and isValid((iAns >> 8) & 0xFF) and isValid((iAns >> 16) & 0xff) and isValid((iAns >> 24) & 0xff)


a = -207009661
b = 866732163
c = 2404399682
d = 4015012418


for x in xrange(-100,100):
	for y in xrange(-100,100):
		na = (a + x *  MOD_NUM)
		nb = (b + y * MOD_NUM)
		ans2 = (17 * nb - 6 * na) / 11
		ans1 = (7 * ans2 - nb) / 6

		if (validAns(ans1) or validAns(ans2)):
			print "correct"
		#if not(17*(ans2-ans1)+ans2==4087957635 and 7*(ans2-ans1)+ans1==866732163):
		#	print str((17*(ans2-ans1)+ans2)%MOD_NUM)
		#	print str((7*(ans2-ans1)+ans1)%MOD_NUM)
			print hex(ans1 % MOD_NUM)
			print hex(ans2 % MOD_NUM)

print validAns(0x61169202b1)

# 17(y-x)+y=4087957635
# 7(y-x)+x= 866732163
# 5(y-x)+y=2404399682
# 13(y-x)+x=4015012418