#include <iostream>
using namespace std;

void main() {

	//����� �Ҵ��ϴ� ������
	const int& ca = 3;
	cout << ca << endl;
	int a;
	int* b = &a;
	int** c = &b;
	**c = 3;
	cout << b << endl;
	cout << &b<<endl;
	cout << &c<<endl;
	cout << a << endl;

}