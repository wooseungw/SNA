#include <iostream>
#include "multiply.h"

using namespace std;
//시험범위는 배열까지 연습문제 위주
int mul(int a1,int a2);
void func2(char* arg) {
	cout << "char *" << arg << endl;
}
void func2(const char* arg) {
	cout << "const char *"<<arg << endl;
}
void func1(int* arg) {
	cout << "int *" << endl;
}
void func1(const int* arg) {
	cout << "const int *" << endl;
}

int main() {
	const char* p = "A";
	char p1[2] = "B";
	char b = 'B';
	func2(p);
	func2("A");
	func2(p1);
	func2(b);

	int result = mul(2, 3);
	
	cout << result << endl;
	result = 1;
	func1(&result);//
	const int *b = &result;
	func1(b);



	result = multiply(2, 3);//헤더-리소스-메인
	cout << result << endl;


	int i = 21;
	const int& da = 3; 
	char c = 65;
	int arr[5] = { 1,2,3,4,5 };
	cout << da << endl;
	cout << i << " " << &i << endl;
	cout << c << " " << &c << endl;
	cout << arr << " " << &arr << endl;
	cout<< endl;
	int* ipt = &i;
	char* cpt = &c;
	cout << ipt << " " << &ipt << " " << *ipt << endl;
	cout << cpt << " " << &cpt << " " << *cpt << endl;
	return 0;
}

int mul(int a1, int a2) {
	return a1 * a2;
}