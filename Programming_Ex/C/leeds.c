#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    if(argc < 3)
    {
        printf("Usage: ./leeds <hours> <hours> ...\n");
        return 0;
    }

    int x = strtol(argv[1],NULL,10);
    int y = strtol(argv[2],NULL,10);
    int z = strtol(argv[3],NULL,10);
    int c = 1;
    int j,k,l;

    printf("First sat: %d\nSecond sat: %d\nThird sat: %d\n",x,y,z);

    j = c%x;
    k = c%y;
    l = c%z;

    while(j!=k || k!=l || j!=l)
    {
        j = c%x;
        k = c%y;
        l = c%z;
        c++;
    }

    printf("after %d hours\n",c++);

    return 0;
}
