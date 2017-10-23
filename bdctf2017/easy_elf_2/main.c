#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

signed long check(unsigned int ans, unsigned int k, int i);


int main(int argc, char const *argv[])
{
	int result; // eax@7
	char v4[18]; // [sp+0h] [bp-20h]@1
	int v5; // [sp+14h] [bp-Ch]@2
	int v6; // [sp+18h] [bp-8h]@1
	int i; // [sp+1Ch] [bp-4h]@1

	puts("welcome");
	strcpy(v4, "adminadmin1231233");
	v6 = 0;
	for ( i = 0; i <= 16; ++i )
	{
		for (unsigned char v5 = 0; v5 <= 255; ++v5)
		{//zhi jie bao po le, lan de xie le...
			if ( (unsigned int)check(v5, v4[i], i) )
			{
				putchar(v5);
				break;
			}
		}
	}
	printf("\n");
	/*
	if ( v6 == 17 )
		result = puts("good job,now you know what is flag!");
	else
		result = puts("wrong\ntry again!!!");//*/
	return result;
}

signed long check(unsigned int ans, unsigned int k, int i)
{
	signed long result; // rax@2
	unsigned int v4[17]; // [sp+10h] [bp-50h]@1

	v4[0] = 7;
	v4[1] = 8;
	v4[2] = 12;
	v4[3] = 14;
	v4[4] = 21;
	v4[5] = 13;
	v4[6] = 13;
	v4[7] = 3;
	v4[8] = 28;
	v4[9] = 22;
	v4[10] = 110;
	v4[11] = 93;
	v4[12] = 64;
	v4[13] = 110;
	v4[14] = 93;
	v4[15] = 88;
	v4[16] = 78;
	if ( (k ^ ans) == v4[i] )
	{
		//printf("%d,%d,%d\n", ans, k, v4[i]);
		//putchar(k ^ ans);
		result = 1LL;
	}
	else
	{
		result = 0LL;
	}
	return result;
}