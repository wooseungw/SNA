#include <sys/types.h>
#include <sys/stat.h>
#include <sys/time.h>
#include <utime.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    struct stat buf;        /* struct to hold file stats */
    struct utimbuf time; // struct utimbuf { time_t actime; time_t modtime; };

    if (argc < 3) {
        fprintf(stderr, "사용법: %s file1 file2\n", argv[0]);
        exit(1);
    }
 
    if (stat(argv[1], &buf) < 0) {
        perror("stat()");
        exit(-1);
    }

    time.actime = buf.st_atime;
    time.modtime = buf.st_mtime;

    printf("\t수정시간: %s\n", ctime(&buf.st_mtime));

    if (utime(argv[2], &time))
        perror("utime");
    else
        exit(0);
}
