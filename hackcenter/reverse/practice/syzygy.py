def get_flag(addr_start, addr_end):
	flag = []
	addr = addr_start
	while addr < addr_end:
		if (Byte(addr) == 0x3c):
			flag.append(chr(Byte(addr + 1)))
			print "".join(flag)
		addr += 1