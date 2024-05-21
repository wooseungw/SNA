#include <utime.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    if (argc < 2) {
        fprintf(stderr, "사용법: %s file1\n", argv[0]);
        exit(-1);
    }
 
    utime(argv[1], NULL);	// 현재시간으로 설정
}
