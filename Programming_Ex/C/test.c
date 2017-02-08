#include <stdio.h>

int htoi(char* s)
{
	int i,n,t;

	n = 0;
	t = 0;
	for(i=0; (s[i]>='0' && s[i]<='9') || (s[i]>='A' && s[i]<='F') || (s[i]>='a' && s[i]<='f'); i++)
	{
		if(s[i]>='0' && s[i]<='9')
			t = s[i] - '0';
		if(s[i]>='A' && s[i]<='F')
			t = s[i] - 'A' + 10;
		if(s[i]>='a' && s[i]<='f')
			t = s[i] - 'a' + 10;

		n = n * 16 + (t);
	}

	return n;
}

int main(int argc, char** argv)
{
	int c;

	if(argc == 2)
	{
		c = htoi(argv[1]);
		printf("%s: %d\n",argv[1],c);
	}

	return 0;
}
