#include <iostream>
using namespace std;



/*
class CTest {
public:
	int m_value;
	void Show() {
		cout << this << endl;
		cout << m_value << endl;
		cout << this->m_value << endl;
		
	}
};*/
//class CTest
//{
//public:
//	//int m_Value;//����
//	static int m_Value;
//
//	void Func()
//	{
//		cout << m_Value << endl;	// OK
//	}
//
//	static void SFunc()
//	{
//		cout << m_Value << endl;	// Error
//	}
//};
//CTest::m_Value = 2;//�̰͵� ���� 
//static�� �Լ��� ������ �ٷ� ȣ���� ������
// ���� �ȿ� �մ°͵� �ٷ� ȣ�� �����ؾ���
class CParent {
public:
	int m_Value;

	void Show() {
		cout << m_Value << endl;
	}
};
//ũ��� �ڱ�Ŭ���� ũ��+�θ�Ŭ���� 2�� ��ӹ��� ���� ��������
//static������ ���� �����Ǳ� ������ ũ�⿡ ���Ե�������
class CTest : public CParent {
public:
	int m_Value;

};
int main1() {
	CTest t;
	t.CTest::m_Value =  12;
	t.CParent::m_Value = 2;
	cout << t.m_Value << endl;
	cout << t.CParent::m_Value<< endl;
	t.CParent::Show();
	//CTest::SFunc();
	/*
	CTest t3;
	CTest* pT = &t3;
	pT->Show();
	pT = NULL;
	//pT->Show();//00000000 ��µǰ� ����

	CTest t1;
	t1.m_value = 3;
	t1.Show();
	
	CTest t2;
	t2.m_value = 12;
	t2.Show();
	*/
	//��� ������ �ʱ�ȭ
	//�ν��Ͻ��� �Լ�ȣ���� ���� �������� static�� ���� �ִ�ġ�� ������ �� ���� 
	//Static�� �ܺο��� �����ؾ���
	//const�� ���ο��� ����
	//const static�� 
	//����� �ȹް� �����ϸ� (Ŭ���� ���� ���ϴ� Ŭ���� ȣ��)
	return 0;
}