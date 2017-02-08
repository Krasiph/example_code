#include <stdio.h>

int main(int argc, char** argv)
{
	if(argc == 3)
	{
		int w = strtol(argv[1],NULL,10);
		int h = strtol(argv[2],NULL,10);
		float area = ((float)w*h)/2;
		printf("A traingle of width %d and height %d is %f sqaure units in area\n",w,h,area);
	}
	else
	{
		printf("Please enter a width and a height\n");
	}
	return 0;
}
