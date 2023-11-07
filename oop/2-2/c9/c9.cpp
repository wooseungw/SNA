//함수 중복정의
#include <iostream>
using namespace std;

//void Func(int arg)
//{
//	cout << "Value" << endl;
//}
//
//void Func(int& arg)
//{
//	cout << "Reference" << endl;
//}
/*
void Func(short arg)
{
	cout << "short: " << arg << endl;
}

void Func(int arg)
{
	cout << "int: " << arg << endl;
}

void Func(__int64 arg)
{
	cout << "__int64: " << arg << endl;
}
*/
//클래스도 헤더 가능
struct STest
{
	const char* n_Name;
public:
	int public_int;
private:
	int pri_int;
};


class COne
{
protected:
	int a;
private:
public:
	void Seta(int arg) {
		a = arg;
	}

	void Showa() {
		cout << "a is " << a << endl;
	}
};
class CFamily {
protected:
	char* n_Familyname;
public:
	void SetFamilyName(char* arg) {
		n_Familyname = arg;
	}
	void ShowFamilyName() {
		cout << n_Familyname << endl;
	}

};
class CName : public CFamily
{
public:
	void SetName(char* arg) {
		n_Name = arg;
	}
	void ShowName() {
		cout << n_Familyname << " " << n_Name << endl;
	}

private:
	char* n_Name;
};
//void CName::SetName(char* arg){
//	n_Name = arg;
//}

class CTest {
public:
	const int i;//const쓰는 변수가 있으면 무조건 할당해야함
	CTest() :i(1) {
		//이렇게 하면 i에 값이 선언이 되는것
	}
};

void main()
{
	CTest ct;
	cout << ct.i << endl;

	struct STest s1;
	s1.n_Name = "sdas";
	s1.public_int = 1;
	
	cout << s1.n_Name << endl;
	CName n;
	char fm[] = "Happy";
	n.SetFamilyName(fm);
	//n.SetName("Chris"); Char * arg = "Chris"와 같은 선언 const로 바꾸는건 비효율적이다.
	char name[] = "Crisis"; //배열이 best
	n.SetName(name);
	n.ShowName();

	COne c;
	c.Seta(2);
	c.Showa();
	/*
	//Func(1);		// OK
	Func((short)1);
	Func(2);
	Func((__int64)3);	// 3LL __int64 8bit int
	int a = 1;

	int& ar = a; int ar2 = a;
	
	Func(a);		// Error a=1이다.int arg = a;와 int &arg = a;모두 에러가 나지 않음 따라서 두개는 같은 함수가 됨 보통 레퍼런스꼴은 안쓴다.
	*/
}
