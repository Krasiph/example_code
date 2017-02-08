#include <stdio.h>
#include <stdlib.h>

int on_even(int num);
int on_odd(int num);

int main(int argc, char** argv)
{
	int num = 0;
	int i = 0;
	for(i=1; i<argc; i++)
	{
		num = atoi(argv[i]);
		if(!num || num < 0 || num != atof(argv[i]))
		{
			printf("%s is not a valid number.\n",argv[i]);
		}
		else
		{
			printf("%d\n",num);
			while(num != 1)
			{
				if(num % 2 == 0)
				{
					num = on_even(num);
				}
				else
				{
					num = on_odd(num);
				}
				printf("\t%d\n",num);
			}
		}
	}
	return 0;
}

int on_even(int num)
{
	return num / 2;
}

int on_odd(int num)
{
	return num * 3 + 1;
}
