#include <iostream>
using namespace std;

void main() {

	int a[5];
	//����� �����ؾ� arr�� �Ҵ簡��
	const int N = 3;
	int b[N] = { 1,2,3 };//���⼭ b�� b�� �ּ�
	//int c[3] = b;
	//�迭 ����
	int c[3] = {};
	c[0] = b[0];
	c[1] = b[1];//...�� �����ؾ���
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
	//���� ������ ����
	int(*pp)[3] = &b;
	cout << pp[0] << " " << pp[1];
	cout << endl;
	//\0���� �ʱ�ȭ �ؾ���
	char str1[] = { 'C','C','+','\t','\0'};
	char str2[] = "CC+\t\0";
	char str3[] = { "CC+\t\0" };

	//char* s2 = "C++\0"; ������ ��
	const char* s2 = "C++\0";//������ �ȳ� �ӽ������Ϳ� ���� ������ �ȳ��°�
	cout << str1 << str2 <<str3<<endl;

	int arr[2] = { 1,2 };
	int* pa = arr;
	cout << pa[0]<<" "<<pa[1]<<endl;//�����͸� �迭ó�� �Ἥ value�� ������ �� ����

	int arr2[2][3] = { { 11, 12, 13 }, { 21, 22, 23 } };
	//int** ppa = (int**)arr2;//arr2�� ��ü�� �ּ� 2������ 2���� �����Ͷ�� �����ϱ�
	int(*ppa)[3] = arr2;//2���� ������ ������ �̷������� ���� �Ѵ�.	
	cout << ppa[1][2] << endl;

	int* arrM[2] = { arr2[0],arr2[1] };
	int** pp2 = arrM;
	cout << pp2[1][1]<< endl;
	//�迭�� �Լ��� ���ڷ� �־ call by pointer�� �������� �����
}