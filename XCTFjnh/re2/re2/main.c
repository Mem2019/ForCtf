#include <stdio.h>
#define PSW_LEN_DWORD 10
#define PSW_LEN (PSW_LEN_DWORD*sizeof(int))
#include <stdlib.h>
#include <memory.h>


int arr[PSW_LEN_DWORD] = { 1441465642 ,251096121 ,-870437532 ,-944322827 ,
647240698 , 638382323, 282381039 ,-966334428 ,-58112612, 605226810};
 
int main()
{
	int seed = (0x7473796c + 0x6f65635f + 0x61746163);
	srand(seed);
	char psw[PSW_LEN + 1];
	memset(psw, 0, PSW_LEN + 1);
	int* p_dwPsw = (int*)psw;
	for (int i = 0; i < PSW_LEN_DWORD; i++)
	{
		p_dwPsw[i] = arr[i] + rand();
	}
	printf("%s", psw);
	getchar();
}