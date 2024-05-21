#include <stdio.h>
struct my {
    int a;
    char b;
    float c;
} x = {1,'a',1.5};

int main() 
{
    struct my y = {3,'c',3.5};
    printf("x.a=%d x.b=%c x.c=%3.1f\n", x.a, x.b, x.c);
    printf("y.a=%d y.b=%c y.c=%3.1f\n", y.a, y.b, y.c);
}
