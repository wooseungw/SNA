#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#define MAXLINE 100

/* 파이프를 통해 자식에서 부모로 데이터를 보내는 프로그램 */
int main()
{
    int n, length, fd[2], pid;
    char cbuffer[MAXLINE], pbuffer[MAXLINE];

    pipe(fd);			// 파이프 생성

    if ((pid = fork()) == 0) {	// 자식 프로세스 (부모 프로세스와 파이프 공유)
        close(fd[0]);		// 읽기용(0) fd 닫음
        sprintf(cbuffer, "<-- Hello from PID %d\n", getpid());
        length = strlen(cbuffer)+1;
        write(fd[1], cbuffer, length);		// 파이프 쓰기
    } else {			// 부모 프로세스 (자식 프로세스와 파이프 공유)
        close(fd[1]);		// 쓰기용(1) fd 닫음
        n = read(fd[0], pbuffer, MAXLINE);	// 파이프 읽기
	printf("[%d] %s", getpid(), pbuffer);
    }
    exit(0);
}
