CC      = gcc
CFLAGS  = -Wall -Werror -std=c99

.PHONY: all clean exploit

.SUFFIXES: .c .o

all: get_scd_rand rand_to_seed.json

exploit: all
	python ./exp.py

get_scd_rand: get_scd_rand.c 
	$(CC) $(CFLAGS) get_scd_rand.c -o get_scd_rand

rand_to_seed.json: rand_to_seed
	./rand_to_seed > rand_to_seed.json

rand_to_seed: rand_to_seed.c
	$(CC) $(CFLAGS) rand_to_seed.c -o rand_to_seed

clean:
	rm -f rand_to_seed rand_to_seed.json get_scd_rand
