#include <stdio.h>
struct st
{
    int a;
    char b;
};
int main(){
    struct st x = {1,'c'};
    struct st *p = &x;
    printf("Print By Value: %d %c\n",x.a,x.b);
    printf("Print By Pointer: %d %c\n",p->a,p->b);
    return 0;
    for (int i =0;i<10;i++){
        for (int j =0 ; j < 10;j++){
            printf("%d %d",i,j);
        }
    }
    
}


