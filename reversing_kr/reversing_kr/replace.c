//input + 2 + 0x601605c7 + 2 == 0x00401071
#include "headers.h"

unsigned int getinput()
{
	return 0x00401071 - 4 - 0x601605c7;
}

int main()
{
	char tang[100];

	printf("%u\n", getinput());
	printf("%s\n", tang);
	system("pause");
}//*/