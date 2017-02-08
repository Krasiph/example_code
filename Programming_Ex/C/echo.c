#include <stdio.h>

int main(int argc, char** argv)
{
	char c;
	printf("Write anything. (Ctrl+D to exit)\n");

	c = getc(stdin);
	while(c != EOF)
	{
		putc(c,stdout);
		c = getc(stdin);
	}

	return 0;
}
