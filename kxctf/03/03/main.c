#include "base64.h"
#include "sm3.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define UPPER_BOUND_OF_3BYTES 0x01000000
#define SM3_LEN 32
#define SM3_LEN_ASCII (SM3_LEN * 2)
#define SM3_LEN_ASCII_BUFLEN (SM3_LEN_ASCII + 1)
#define BASE64X1_LEN (SM3_LEN_ASCII / 4 * 3)
#define BASE64X2_LEN (BASE64X1_LEN  / 4 * 3)
#define BUF_LEN 1024

int flag;
char sm3_hash[SM3_LEN];
char ascii_hash[SM3_LEN_ASCII_BUFLEN];
char base64_dec1[BUF_LEN];
char base64_dec2[BUF_LEN];

void get_ascii_hash(char* hash, char* ret)
{//pre: ret has size (SM3_LEN*2+1)
	for (int i = 0; i < SM3_LEN; ++i)
		sprintf(&ret[2 * i], "%02x", (unsigned __int8)hash[i]);
	ret[SM3_LEN_ASCII] = 0;
}
/*
sm3(base64dec(base64dec(input))[0..3)) == input

sm3(str[0..3)) == base64(base64(str))
base64dec(base64dec(sm3(str[0..3)))) == str
*/

int isBase64Char(char c)
{
	return ((c | 32) >= 'a' && (c | 32) <= 'z') || c == '=' || c == '+' ||
		c == '/' || (c >= '0' && c <= '9');
}

int firstThreeSame(char* a1, char* a2)
{
	return a1[0] == a2[0] && a1[1] == a2[1] && a1[2] == a2[2];
}

int isValidBase64(char* base64, int len)
{
	for (int i = 0; i < len; i++)
	{
		if (!isBase64Char(base64[i]))
		{
			return 0;
		}
	}
	return 1;
}

int main2()
{
	for (flag = 0; flag < 0x01000000; flag++)
	{
		if ((flag & 0xffff) == 0)
		{
			printf("%d\n", flag);
		}
			
		sm3((unsigned char*)&flag, 3, sm3_hash);
		get_ascii_hash(sm3_hash, ascii_hash);
		memset(base64_dec1, 0, BUF_LEN);
		base64_decode(ascii_hash, /*SM3_LEN_ASCII*/BUF_LEN, base64_dec1);
		memset(base64_dec2, 0, BUF_LEN);
		if (base64_decode(base64_dec1, /*BASE64X1_LEN*/BUF_LEN, base64_dec2))
		{
			//continue;
		}
		/*else
		{
			base64_decode(base64_dec1, BASE64X1_LEN, base64_dec2);
		}//*/
		base64_dec2[BASE64X2_LEN] = 0;
		if (firstThreeSame(base64_dec2, (char*)&flag))
		{
			printf("%s\n", ascii_hash);
			printf("%s\n", base64_dec2);
			printf("%s\n", &flag);
			//system("pause");
		}
	}
	system("pause");
	return 0;
}