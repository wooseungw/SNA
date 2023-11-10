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
//	//int m_Value;//에러
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
//CTest::m_Value = 2;//이것도 오류 
//static이 함수에 붙으면 바로 호출이 가능함
// 따라서 안에 잇는것도 바로 호출 가능해야함
class CParent {
public:
	int m_Value;

	void Show() {
		cout << m_Value << endl;
	}
};
//크기는 자기클래스 크기+부모클래스 2개 상속받을 때도 마찬가지
//static변수는 따로 보관되기 때문에 크기에 포함되지않음
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
	//pT->Show();//00000000 출력되고 오류

	CTest t1;
	t1.m_value = 3;
	t1.Show();
	
	CTest t2;
	t2.m_value = 12;
	t2.Show();
	*/
	//멤버 데이터 초기화
	//인스턴스를 함수호출을 통해 생성가능 static를 통해 최대치를 정해줄 수 있음 
	//Static은 외부에서 정의해야함
	//const는 내부에서 정의
	//const static은 
	//상속을 안받고 위임하면 (클래스 내에 원하는 클래스 호출)
	return 0;
}