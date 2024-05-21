#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    FILE *fp;
 
    if (argc < 2) { perror("argc"); exit(1); }

    if (!strcmp(argv[1], "stdin")) {
	fp = stdin;
        printf("한 글자 입력: ");
        if (getc(fp) == EOF) perror("getc");
    }
    else if (!strcmp(argv[1], "stdout"))
        fp = stdout;
    else if (!strcmp(argv[1], "stderr"))
	fp = stderr;
    else if ((fp = fopen(argv[1], "r")) == NULL) {
        perror("fopen");
        exit(1);
    }
    else if (getc(fp) == EOF) perror("getc");

    printf("스트림 = %s, ", argv[1]);
    if (fp->_flag & _IONBF)
        printf("버퍼 미사용\n");
    else if (fp->_flag & _IOLBF)
	printf("줄 버퍼 사용\n");
    else
        printf("완전 버퍼 사용\n");

    exit(0);
}
