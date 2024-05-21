#include <stdio.h>

int main()
{
    char *p = "UNIX";
    char m[] = "SEVER";
    p = m;
    printf("%c%c%c%c",p,*p+1,p[2],m);
    // printf("%c%c%c%s",p,*(p+1),p[2],m);
    // 출력 결과: SFSERVER
    return 0;
}