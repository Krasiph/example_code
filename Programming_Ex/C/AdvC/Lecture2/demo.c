#include <stdio.h>
#include <stdlib.h>

/*
This program must be compiled using the -std=c99 flag of GCC because of its use of restrict.

The way around this is to use __restrict__.
*/

//#define restrict __restrict__

int count();

int main(int argc, char** argv)
{
    const int never_change = 0;
    register int i = 0;
    char word[] = {'t','h','i','n','g','\00'};
    char* restrict w = (char*)malloc(6*sizeof(char));
    w[0]='t', w[1]='h', w[2]='i', w[3]='n', w[4]='g', w[5]=0;

    printf("%d: %s\n",count(),word);
    for(i=0; i<1000000000; i++);
    printf("%d: %s\n",count(),w);

    /*
    printf("%d: never_change's value is %d\n",count(),never_change);
    never_change++;
    printf("%d: never_change's value is %d\n",count(),never_change);
    //*/

    free(w);
}

int count()
{
    static int c = 0;
    return c++;
}
