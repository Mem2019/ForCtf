#include <stdlib.h>
#include <stdio.h>
#define SEED_OFF 0x202148
void proc_srand(unsigned int i)
{
	srand((unsigned int)(i + SEED_OFF));
	printf("\"%d\":%u,", rand(), (unsigned int)(i + SEED_OFF));
}

int main()
{
	//system("/bin/sh");
	printf("{");
	unsigned int i;
	for (i = 0x00000000; i < 0xffffe000; i += 0x1000)
	{
		proc_srand(i);
		/*if (i + SEED_OFF == 0x75b4148)
			getchar();*/
	}
	proc_srand(i);
	i += 0x1000;
	srand((unsigned int)(i + SEED_OFF));
	printf("\"%d\":%u}", rand(), (unsigned int)(i + SEED_OFF));
}

/*
0x000055dd139ce000
0x000055ce8c5e3000
0x000055aaadb17000
0x00005610214b0000
0x0000558f744b5000
0x000056038011e000
0x0000564d46904000
0x0000556e073b2000
*/