#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <stdlib.h>

#define MAXLEN 100
#define MAXARG 7

int main() {
    char buf[MAXLEN];
    char *args[MAXARG];
    char *s, *save;
    int argn, i;
    static const char delim[] = " \t\n"; // 공백, 탭, 개행 구분자 선언
    int pid, status;

    while (1) {                           // 무한 반복
        printf("[shell] ");               // 프롬프트 출력
        if (fgets(buf, sizeof(buf), stdin) == NULL || buf[0] == '\0') continue;

        // 명령어 순차적 실행 처리
        char *command = strtok(buf, ";");
        while (command != NULL) {
            argn = 0;
            int background = 0;
            int redirect_out = 0, redirect_in = 0;
            char *outfile = NULL, *infile = NULL;

            // 명령어 파싱
            s = strtok_r(command, delim, &save);
            while (s) {
                if (strcmp(s, "&") == 0) {
                    background = 1;
                } else if (strcmp(s, ">") == 0) {
                    redirect_out = 1;
                    s = strtok_r(NULL, delim, &save);
                    outfile = s;
                } else if (strcmp(s, "<") == 0) {
                    redirect_in = 1;
                    s = strtok_r(NULL, delim, &save);
                    infile = s;
                } else {
                    args[argn++] = s;
                }
                s = strtok_r(NULL, delim, &save);
            }
            args[argn] = NULL;

            if (argn == 0) {
                command = strtok(NULL, ";");
                continue;
            }

            if (!strcmp(args[0], "quit"))  // 입력 단어가 quit이면 while문 종료
                exit(0);

            if ((pid = fork()) == -1) {    // fork 호출에 실패하면
                perror("fork failed");
            } else if (pid != 0) {         // 부모: 자식 프로세스 종료 기다림
                if (!background) {
                    pid = waitpid(pid, &status, 0);
                }
            } else {                       // 자식: execvp를 이용하여 arg[0] 실행
                if (redirect_out) {
                    int fd = open(outfile, O_WRONLY | O_CREAT | O_TRUNC, 0644);
                    if (fd < 0) {
                        perror("open");
                        exit(1);
                    }
                    dup2(fd, STDOUT_FILENO);
                    close(fd);
                }

                if (redirect_in) {
                    int fd = open(infile, O_RDONLY);
                    if (fd < 0) {
                        perror("open");
                        exit(1);
                    }
                    dup2(fd, STDIN_FILENO);
                    close(fd);
                }

                if (execvp(args[0], args) == -1) {
                    printf("잘못된 명령입니다.\n");
                    exit(1);
                }
            }
            command = strtok(NULL, ";");
        }
    }
    return 0;
}
