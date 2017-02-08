#include <stdio.h>
#include "grandfather.h"
//#include "father.h"

int main(int argc, char** argv)
{
	struct foo a_struct;
	a_struct.member = 7;

	printf("The member is %d\n", a_struct.member);

	return 0;
}
