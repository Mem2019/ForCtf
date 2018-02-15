#+  -  +  -  +  -  +  -  +
#01 01 11 11 01 01 10 00 01
#01 11 01 00 11 10 10 11 00 0

# 0 1 3 2 0 3 2 1 2
#100123322013022122

evens = ["much ", "many ", "very ", "so "]
odds = ["microsoft ", "windows ", "system ", "amaze "]


def arr_to_args(sequece):
	args = []
	for i in xrange(0,len(sequece)):
		if i % 2 == 0:
			args.append(evens[sequece[i]])
		else:
			args.append(odds[sequece[i]])
	return "".join(args)

print arr_to_args([1,0,0,1,2,3,3,2,2,0,1,3,0,2,2,1,2,2])

#