#include <stdio.h>

void getFlag(unsigned char* flag)
{
	/*
[0] ^ '4' == 120
[1] == '1'
[2] ^ '2' == 124
[3] ^ 0x88 == -35
[4] == 'X'
[5] == 0
	*/
	flag[0] = 120 ^ '4';
	flag[1] = '1';
	flag[2] = 124 ^ '2';
	flag[3] = (unsigned char)(-35) ^ 0x88;
	flag[4] = 'X';
	flag[5] = 0;
}

int main(int argc, char const *argv[])
{
	char flag[8];
	getFlag((unsigned char*)flag);
	printf("%s\n", flag);
	return 0;
}