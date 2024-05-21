#include <stdio.h>

void swap(int *p);
int main(){
    int a[2] = {3,20};
    int*ap = a;
    printf("SWAP전 %d, %d\n",*ap,*(ap+1));
    swap(ap);
    printf("SWAP후 %d, %d\n",*ap,*(ap+1));
    return 0;
}

void swap(int *ap) {
   int buffer; 
   buffer = *ap; 
   *ap=*(ap+1);
   *(ap+1) = buffer;
}



