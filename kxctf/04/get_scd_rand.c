#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	if (argc != 2)
		return -1;
	int seed;
	seed = atoi(argv[1]);
	srand(seed);
	rand();
	printf("%d\n", rand());
	return 0;
}