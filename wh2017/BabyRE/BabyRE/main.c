#include <stdio.h>
#include <windows.h>

#define ASM_SIZE 182
int decodeAsm()
{
	char buffer[ASM_SIZE];
	FILE* f; 
	int error = fopen_s(&f,"1.elf", "rb+");
	error = fseek(f, 0xb00, SEEK_SET);
	error = fread_s(buffer, ASM_SIZE, 1, ASM_SIZE, f);
	error = ferror(f);
	error = feof(f);
	error = GetLastError();

	for (int i = 0; i < ASM_SIZE; i++)
	{ 
		buffer[i] ^= 0x0c;
	}
	fseek(f, 0xb00, SEEK_SET);
	fwrite(buffer, 1, ASM_SIZE, f);
	fclose(f);
	return 0;
}
 int formFlag()
{
	char v2[14]; // [sp+8h] [bp-20h]@1
	int i; // [sp+24h] [bp-4h]@1

	v2[0] = 102;
	v2[1] = 109;
	v2[2] = 99;
	v2[3] = 100;
	v2[4] = 127;
	v2[5] = 107;
	v2[6] = 55;
	v2[7] = 100;
	v2[8] = 59;
	v2[9] = 86;
	v2[10] = 96;
	v2[11] = 59;
	v2[12] = 110;
	v2[13] = 112;
	for (i = 0; i <= 13; ++i)
		v2[i] ^= i;
	printf("%s", v2);
	return 0;
}
int main()
{
	formFlag();
	getchar();
}