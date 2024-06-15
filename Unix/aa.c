jump1.c

void  p1(), p2();
jmp_buf env;
int main()
{
    if (setjmp(env) == 1) {
        printf("오류로 인해 복귀: main()\n");
        exit(0);
    }
    else printf("처음 통과: main()\n");
    p1();
}
void p1()
    p2();

void p2() 
{
    int error = 1;

    if (error) {
        printf("p2()에서 오류\n");
        longjmp(env, 1);
    }
}