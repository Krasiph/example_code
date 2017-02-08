#include <stdio.h>
#include <stdlib.h>

void output(size_t j)
{
    printf("i = %u\n",j);
}

int main(int argc, char** argv)
{
    int i = -1;
    output(i);

    return 0;
}
