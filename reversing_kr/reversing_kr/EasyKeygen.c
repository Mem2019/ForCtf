#include <stdio.h>

char keys[3] = { 16,32,48 };
char serial[] = "\x5B\x13\x49\x77\x13\x5E\x7D\x13";
void easy_ken_gen(char* flag)
{
	int i;
	int i_3 = 0;
	for (i = 0; i < sizeof(serial) - 1; ++i)
	{
		if (i_3 >= 3)
			i_3 = 0;
		flag[i] = (serial[i] ^ keys[i_3]);
		i_3++;
	}
	flag[i] = 0;
}
/*
int main()
{
	char flag[100];
	easy_ken_gen(flag);
	printf("%s\n", flag);
	system("pause");
}//*/
