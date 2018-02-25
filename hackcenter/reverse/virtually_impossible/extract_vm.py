def extract_vm(start_addr, end_addr):
	ret = []
	p = start_addr
	while p < end_addr:
		ret.append(Dword(p))
		p += 4
	return ret