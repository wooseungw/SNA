#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

#define MAX_ARGS 32

int main() {
    char input[1024];
    char *tokens[MAX_ARGS];
    char *saveptr;
    int token_count;
    int background = 0;

    while (1) {
        printf("[shell] ");
        fgets(input, sizeof(input), stdin);

        // 명령어 파싱
        token_count = 0;
        tokens[token_count] = strtok_r(input, " \t\n", &saveptr);
        while (tokens[token_count] != NULL) {
            token_count++;
            tokens[token_count] = strtok_r(NULL, " \t\n", &saveptr);
        }
        if (token_count == 0) continue;

        // 백그라운드 실행 여부 확인
        if (strcmp(tokens[token_count - 1], "&") == 0) {
            background = 1;
            tokens[token_count - 1] = NULL;
        } else {
            background = 0;
        }

        // 파이프 사용 여부 확인
        int pipe_index = -1;
        int i = 0;
        while (i < token_count) {
            if (strcmp(tokens[i], "|") == 0) {
                pipe_index = i;
                break;
            }
            i++;
        }

        if (pipe_index >= 0) {
            // 파이프 사용
            tokens[pipe_index] = NULL; // 파이프 앞부분 명령어 끝을 나타내는 NULL로 치환

            int fd[2];
            pipe(fd);

            pid_t pid1 = fork();
            if (pid1 < 0) {
                perror("fork");
                exit(EXIT_FAILURE);
            } else if (pid1 == 0) {
                close(fd[0]); // 자식 프로세스에서는 파이프의 읽기 디스크립터를 사용하지 않음
                dup2(fd[1], STDOUT_FILENO); // 파이프의 쓰기 디스크립터를 표준 출력에 복제
                close(fd[1]);
                execvp(tokens[0], tokens); // 파이프 앞부분 명령어 실행
                perror("execvp");
                exit(EXIT_FAILURE);
            }

            char **tokens2 = &tokens[pipe_index + 1]; // 파이프 뒷부분 명령어를 가리키는 임시 포인터 변수

            pid_t pid2 = fork();
            if (pid2 < 0) {
                perror("fork");
                exit(EXIT_FAILURE);
            } else if (pid2 == 0) {
                close(fd[1]); // 자식 프로세스에서는 파이프의 쓰기 디스크립터를 사용하지 않음
                dup2(fd[0], STDIN_FILENO); // 파이프의 읽기 디스크립터를 표준 입력에 복제
                close(fd[0]);
                execvp(tokens2[0], tokens2); // 파이프 뒷부분 명령어 실행
                perror("execvp");
                exit(EXIT_FAILURE);
            }

            // 부모 프로세스는 파이프를 사용하지 않으므로 파이프 디스크립터를 닫음
            close(fd[0]);
            close(fd[1]);

            // 백그라운드 실행인 경우 자식 프로세스의 종료를 기다리지 않음
            if (!background) {
                waitpid(pid1, NULL, 0);
                waitpid(pid2, NULL, 0);
            }
        } else {
            // 파이프를 사용하지 않는 경우
            pid_t pid = fork();
            if (pid < 0) {
                perror("fork");
                exit(EXIT_FAILURE);
            } else if (pid == 0) {
                // 자식 프로세스에서는 execvp로 명령어 실행
                execvp(tokens[0], tokens);
                perror("execvp");
                exit(EXIT_FAILURE);
            } else {
                // 부모 프로세스는 자식 프로세스가 종료될 때까지 기다림
                if (!background) {
                    waitpid(pid, NULL, 0);
                }
            }
        }
    }

    return 0;
}


