#include <stdio.h>
#define N 4

int main()
{
    int sum = 0;
    int a[N], i;

    for(i=0; i < N; i++)
        a[i] = i*2;

    for(i=0; i < N; i++)
           sum += a[i];

    printf("배열 a[]의 합=%d\n", sum);
}
