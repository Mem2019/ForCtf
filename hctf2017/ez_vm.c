#include <stdio.h>
#include <stdlib.h>

#define INPUT_LEN 0x20
int stack[256];
char key[32];
int paddings[1024];
int sp = 0;
void push(int n)
{
	stack[sp] = n;
	sp++;
}
int main(int argc, char const *argv[])
{
	char szInput[INPUT_LEN];
	int r0 = 0;
	int r4 = 0;
	for (int i = 0; i < INPUT_LEN; ++i)
	{
		r0+=0x33;
		r0%=0x20;
		push(szInput[r0]);
	}
	int* curStack;
	int r10;
	r0 = 0;
	curStack = stack + sp;
	r10 = (int)(char)(*(curStack - 32));
	r0 = 5;


	return 0;
}