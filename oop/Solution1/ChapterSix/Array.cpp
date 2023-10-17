#include <iostream>
using namespace std;

void main() {

	int a[5];
	//상수로 선언해야 arr에 할당가능
	const int N = 3;
	int b[N] = { 1,2,3 };//여기서 b는 b의 주소
	//int c[3] = b;
	//배열 복사
	int c[3] = {};
	c[0] = b[0];
	c[1] = b[1];//...로 선언해야함
	for (int i = 0; i < N; i++) {
		c[i] = b[i];
	}
	for (int i=0;i<N;i++)
		cout << c[i] <<" ";
	cout << endl;
	
	int d[3] = {};
	memmove(d, b, N);
	for (int i = 0; i < N; i++)
		cout << d[i] << " ";
	cout << endl; 
	
	int* p = b;
	cout << *p << *(p+1)<< *(p+2) << endl;
	b[0] = 4;
	b[1] = 5;
	b[2] = 6;
	cout << *p << *(p + 1) << *(p + 2) << endl;
	//이중 포인터 선언
	int(*pp)[3] = &b;
	cout << pp[0] << " " << pp[1];
	cout << endl;
	//\0으로 초기화 해야함
	char str1[] = { 'C','C','+','\t','\0'};
	char str2[] = "CC+\t\0";
	char str3[] = { "CC+\t\0" };

	//char* s2 = "C++\0"; 오류가 남
	const char* s2 = "C++\0";//오류가 안남 임시포인터에 들어가서 오류가 안나는거
	cout << str1 << str2 <<str3<<endl;

	int arr[2] = { 1,2 };
	int* pa = arr;
	cout << pa[0]<<" "<<pa[1]<<endl;//포인터를 배열처럼 써서 value를 가져올 수 있음

	int arr2[2][3] = { { 11, 12, 13 }, { 21, 22, 23 } };
	//int** ppa = (int**)arr2;//arr2는 전체의 주소 2차원은 2개의 포인터라고 생각하기
	int(*ppa)[3] = arr2;//2차원 포인터 선언은 이런식으로 많이 한다.	
	cout << ppa[1][2] << endl;

	int* arrM[2] = { arr2[0],arr2[1] };
	int** pp2 = arrM;
	cout << pp2[1][1]<< endl;
	//배열은 함수의 인자로 넣어도 call by pointer라 원본값이 변경됨
}