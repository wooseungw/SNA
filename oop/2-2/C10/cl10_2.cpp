#include <iostream>
using namespace std;
class MyClass
{
public:

	//���� ������ ������
	MyClass(int args) {
		m_Value = args;
	};
	~MyClass();

private:

};
//�ܺ� ���� �� ������ Ŭ���� �ȿ� MyClass() �����ؾ���
MyClass::MyClass()
{
}
//�ܺ� ������ �� �Ҹ���
MyClass::~MyClass()
{
}
int main() {
	return 0;
}