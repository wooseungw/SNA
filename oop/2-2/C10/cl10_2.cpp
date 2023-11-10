#include <iostream>
using namespace std;
class MyClass
{
public:

	//내부 생성된 생성자
	MyClass(int args) {
		m_Value = args;
	};
	~MyClass();

private:

};
//외부 정의 된 생성자 클래스 안에 MyClass() 선언해야함
MyClass::MyClass()
{
}
//외부 저으이 된 소멸자
MyClass::~MyClass()
{
}
int main() {
	return 0;
}