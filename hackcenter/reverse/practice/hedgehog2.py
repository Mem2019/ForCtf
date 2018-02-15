def decode(start, dst_sign, xor_key):
	eax = start
	while Dword(eax) != dst_sign:
		PatchWord(eax, Word(eax) ^ xor_key)
		eax += 1

def is_decode_asm(addr):
	if (Byte(addr) == 0x81 and \
		Byte(addr + 1) == 0x38 and \
		Byte(addr + 6) == 0x74 and \
		Byte(addr + 7) == 0x0c and \
		Byte(addr + 8) == 0x66 and \
		Byte(addr + 9) == 0x81 and \
		Byte(addr + 10) == 0x30 and \
		Byte(addr + 13) == 0x40 and \
		Byte(addr + 14) == 0xEB and \
		Byte(addr + 15) == 0xF0):
		return ((addr + 20),Dword(addr + 2),Word(addr + 11))
	else:
		return None

def decode_auto(addr_start, addr_end = 0x8049281):
	addr = addr_start
	while addr < addr_end:
		ret = is_decode_asm(addr)
		if (ret):
			print "decode asm found in " + hex(addr)
			start, dst_sign, xor_key = ret
			decode(start, dst_sign, xor_key)
			addr = start
		else:
			addr += 1

def is_ebp_plus_8(addr):
	if (Byte(addr) == 0x8b and \
		Byte(addr + 1) == 0x45 and \
		Byte(addr + 2) == 0x08):
		i = addr + 3
		while True:
			if Byte(i) == 0x3c:
				return chr(Byte(i + 1))
			i += 1
	else:
		return None


def show_flag(addr_start, addr_end):
	flag = []
	addr = addr_start
	while addr < addr_end:
		ret = is_ebp_plus_8(addr)
		if (ret):
			flag.append(ret)
			print "".join(flag)
		addr += 1