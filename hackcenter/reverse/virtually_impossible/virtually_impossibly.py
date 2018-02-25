def dword_to_pynum(num):
	if (num & 0x80000000) == 0:
		return num
	else:
		return (~(0xffffffff)) | num

def push_dwords(asm, pc):
	ret = "push "
	i = pc
	while asm[i] != 0:
		ret += hex(dword_to_pynum(asm[i]))
		ret += " "
		i += 1
	return ret, i+1

def push_dword(asm, pc):
	ret = "push " + hex(dword_to_pynum(asm[pc]))
	return ret, pc+1

def push_top_elem(asm, pc):
	return "push top", pc

def add_op(asm, pc):
	return "add", pc
def mul_op(asm, pc):
	return "mul", pc
def and_op(asm, pc):
	return "and", pc
def xor_op(asm, pc):
	return "xor", pc
def mod_op(asm, pc):
	return "mod", pc

def copy_stack(asm, pc):
	return "pop n, copy stack", pc
def reverse_stack(asm, pc):
	return "pop n, reverse stack", pc

def jmp_op(asm, pc):
	off = dword_to_pynum(asm[pc])
	return "jmp " + hex(off + pc + 1), pc + 1

def condjmp_op(asm, pc):
	off = dword_to_pynum(asm[pc])
	return "cond jmp " + hex(off + pc + 1), pc + 1

def getc_op(asm, pc):
	return "getc",pc
def putc_op(asm, pc):
	return "putc",pc
def printint_op(asm, pc):
	return "print int",pc

def switch_stack(asm, pc):
	return "switch stack",pc

def exit_op(asm, pc):
	return "exit",pc

def pop_reg1(asm, pc):
	return "pop reg1",pc
def pop_reg2(asm, pc):
	return "pop reg2",pc
def push_reg1(asm, pc):
	return "push reg1",pc
def push_reg2(asm, pc):
	return "push reg2",pc

def call_op(asm, pc):
	return "call " + hex(asm[pc]), pc+1
def ret_op(asm, pc):
	return "ret",pc

def nop(asm, pc):
	return "nop",pc

def disass(asm):
	ret = ""
	opcode = {
				0 : push_dwords, 
				1 : push_dword, 
				2 : push_top_elem, 
				3 : add_op,
				4 : mul_op,
				5 : and_op,
				6 : xor_op,
				7 : jmp_op, 
				8 : condjmp_op,
				9 : getc_op,
				10 : putc_op,
				11 : switch_stack,
				12 : exit_op,
				13 : mod_op,
				22 : copy_stack,
				50 : pop_reg1,
				51 : push_reg1,
				52 : pop_reg2,
				53 : push_reg2,
				99 : reverse_stack,
				100 : printint_op,
				120 : call_op,
				121 : ret_op,
				144 : nop
			}
	pc = 0
	length = len(asm)
	while pc < length:
		if asm[pc] in opcode:
			asmstr, newpc = opcode[asm[pc]](asm, pc+1)
		else:
			asmstr, newpc = "undefined" + hex(asm[pc]), pc+1
		ret += asmstr
		ret += "\n"
		print hex(pc) + ": " + asmstr
		pc = newpc
	return ret

print disass([1, 0, 0, 10, 58, 100, 114, 111, 119, 115, 115, 97, 112, 32, 101, 104, 116, 32, 114, 101, 116, 110, 101, 32, 101, 115, 97, 101, 108, 80, 0, 10, 2, 8, 4294967292, 11, 1, 4294967295, 11, 9, 11, 1, 1, 3, 11, 2, 1, 1, 3, 8, 4294967284, 1, 1, 3, 11, 50, 11, 52, 51, 99, 51, 1, 4294967271, 3, 8, 2, 7, 1, 255, 144, 144, 7, 131, 4, 1, 257, 13, 51, 3, 1, 257, 13, 50, 121, 1, 0, 50, 1, 34, 120, 73, 1, 46, 120, 73, 1, 146, 120, 73, 1, 110, 120, 73, 1, 201, 120, 73, 121, 1, 0, 50, 1, 86, 120, 73, 1, 87, 120, 73, 1, 9, 120, 73, 1, 255, 120, 73, 1, 124, 120, 73, 121, 1, 0, 50, 1, 90, 120, 73, 1, 226, 120, 73, 1, 52, 120, 73, 1, 247, 120, 73, 1, 222, 120, 73, 121, 1, 0, 50, 1, 57, 120, 73, 1, 103, 120, 73, 1, 153, 120, 73, 1, 210, 120, 73, 1, 175, 120, 73, 121, 1, 0, 50, 1, 190, 120, 73, 1, 212, 120, 73, 1, 45, 120, 73, 1, 69, 120, 73, 1, 122, 120, 73, 121, 1, 5, 52, 1, 5, 22, 1, 5, 22, 1, 10, 22, 120, 84, 11, 51, 11, 120, 108, 11, 51, 11, 120, 132, 11, 51, 11, 120, 156, 11, 51, 11, 120, 180, 11, 51, 11, 53, 1, 4294967295, 3, 2, 52, 8, 4294967254, 11, 1, 25, 99, 1, 5, 52, 1, 5, 22, 1, 5, 22, 1, 10, 22, 120, 84, 11, 51, 11, 120, 108, 11, 51, 11, 120, 132, 11, 51, 11, 120, 156, 11, 51, 11, 120, 180, 11, 51, 11, 53, 1, 4294967295, 3, 2, 52, 8, 4294967254, 11, 1, 25, 99, 11, 0, 204, 141, 56, 28, 176, 104, 21, 122, 76, 155, 149, 201, 234, 219, 49, 24, 103, 186, 64, 14, 163, 253, 187, 90, 243, 0, 1, 25, 52, 50, 11, 51, 6, 8, 35, 11, 53, 1, 4294967295, 3, 2, 52, 8, 4294967281, 1, 0, 0, 10, 33, 103, 97, 108, 102, 32, 101, 104, 116, 32, 115, 39, 116, 97, 104, 84, 0, 10, 2, 8, 4294967292, 12, 1, 0, 0, 10, 33, 103, 110, 111, 114, 87, 0, 10, 2, 8, 4294967292, 255])
