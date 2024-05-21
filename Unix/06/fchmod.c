#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>

/* 파일 사용권한을 변경한다. */
main(int argc, char *argv[])
{
    long strtol( );
    int newmode;

    if (argc < 3) {
        fprintf(stderr, "사용법: %s file mode\n", argv[0]);
        exit(1);
    }

    newmode = (int) strtol(argv[2],(char **) NULL, 8); // 문자열 → 8진수 정수
    if (chmod(argv[1], newmode) == -1) {
        perror(argv[1]);
        exit(1);
    }
    exit(0);
}
