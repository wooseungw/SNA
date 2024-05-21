#include <stdio.h>  

int main()
{
  printf("[줄/(완전) 버퍼 사용]\n");
  printf("안녕하세요, "); sleep(1);
  printf("리눅스입니다!"); sleep(1);
  printf("\n"); sleep(3);	// default: line buffer

  setbuf(stdout, NULL);		// unbuffered
  printf("\n[버퍼 미사용]\n");
  printf("여러분, "); sleep(1);
  printf("반갑습니다."); sleep(1);
  printf("^^"); sleep(1);
  printf("\n");
}
