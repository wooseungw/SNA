#include <stdio.h>
void swap(int *p1, int *p2);
int main() {
   int a=10, b=20;
   printf("SWAP전: a=%d(주소: %lu), b=%d(주소: %lu)\n", a, &a, b, &b);
   swap(&a, &b);
   printf("SWAP후: a=%d(주소: %lu), b=%d(주소: %lu)\n", a, &a, b, &b);
}

void swap(int *pa, int *pb) {
   int t;
   t=*pa; *pa=*pb; *pb=t;
}
