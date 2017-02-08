#include <stdio.h>
#include <stdlib.h>

struct person{
    char name[20];
    double weight;
    int age;
};

union word{
    short i;
    char c[2];
};

void print_person(struct person *p);

int main(int argc, char** argv)
{
    struct person p1;
    p1.name[0] = 'B';
    p1.name[1] = 'i';
    p1.name[2] = 'l';
    p1.name[3] = 'l';
    p1.name[4] = '\00';
    p1.weight = 183.1;
    p1.age = 22;

    print_person(&p1);

    union word w;
    w.i = 1024;
    FILE* f = fopen("test","w");
    if(f)
    {
        putc(w.c[0],f);
        putc(w.c[1],f);
        fclose(f);
    }

    return 0;
}

void print_person(struct person *p)
{
    printf("%s is %d year(s) old and weighs %f lbs.\n",p->name,p->age,p->weight);
}
