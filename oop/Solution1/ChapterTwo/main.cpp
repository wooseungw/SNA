#include <iostream>
using namespace std;

int main() {
	
	char c1 = 'A';
	char c2 = 65;
	char c3 = c1 + 1;
	cout << c1 << endl;
	cout << c2 << endl;
	cout << c3 << endl;
	char c4 = c3 / 2;

	cout << c4 << endl;
	/*
	cout << fixed;
	cout.precision(0);
	float f = 67108864 + 4;
	__int64 i = 67108864 + 4;
	cout << f << endl;
	cout<< i<<endl;
	*/

	/*
	// �ε��Ҽ��� ����
	cout << fixed;
	cout.precision(4);
	for (int i = 0; i < 10; i++) {
		double f = 67108864 + i;
		cout << f << endl;
	}

	cout << "-------------" << endl;
	for (int i = 0; i < 10; i++) {
		float f = 67108864 + i; //26bit���� Ŀ����
		cout << f << endl;
	}
	
	float f1 = 8388608.0;//float���� �ִ� ǥ�� bit�� �� 23bit ǥ���Ҽ��ִ� bit�� ��� �Ἥ �Ҽ����� ǥ���� �ȵ�
	float f2 = 8388608.5;

	cout << "f1: " << f1 << endl;
	cout << "f2: " << f2 << endl;;
	*/
	//cout << "intũ��: " << sizeof(int) << endl;
	//cout << "short: " << sizeof(short) << endl;
	//cout << "long: " << sizeof(long) << endl;
	return 0;
 }