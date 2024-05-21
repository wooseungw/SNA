#include <stdio.h>
struct student {
    char name[10];
    int age;
} man[3], *p;

int main() {
    int i;

    for (i=0; i<3; i++ ) {
        printf("이름: ");
        scanf("%s", man[i].name);
        printf("나이: ");
        scanf("%d", &man[i].age);
    }

   for (i=0; i<3; i++)
       printf("이름=%10s,  나이=%3d\n", man[i].name, man[i].age);

   p = man;
   for (i=0; i<3; i++, p++)
       printf("이름=%10s,  나이=%3d\n", (*p).name, (*p).age);

   p = man;
   for (i=0; i<3; i++, p++)
       printf("이름=%10s,  나이=%3d\n", p->name, p->age);
}
