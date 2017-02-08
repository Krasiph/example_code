#include <stdio.h>

int main(int argc, char** argv)
{
	char c;
	int count = 0;
	printf("Write anything. (Ctrl+D to exit)\n");

	c = getc(stdin);
	while(c != EOF)
	{
		count++;
		c = getc(stdin);
	}

	printf("You typed %d character(s).\n",count);

	return 0;
}
