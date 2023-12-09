#include<iostream>
using namespace std;

//동적할당
int b = 3;//프로세스 생명주기와 동일
#include<iostream>



using namespace std;



//클래스의 new를 사용했을때
//탬플릿을 사용했을 때
//두개도 사용가능
//STL Standard Tempelate Library cppreference참조 , 시험엔 안들어감

template <class T,class T2>
class Point {
public:
	Point() :x(0), y(0) {
		cout << this << " 생성자 Point()" << endl;
	}
	Point(T x, T y) :x(x), y(y) {
		cout << this << " 생성자 Point(x,y)" << endl;
	}
	~Point()/*소멸자*/ {
		cout << this << "소멸자 ~Point()" << endl;
	}
	T GetX() { return x; }
	T GetY() { return y; }

private:
	//타입이 같은경우
	//타입이 다른경우
	T x;
	T2 y;
};
//두개의 같은 이름의 함수 오버로딩
/*
void printM(int a) {
	cout << a << endl;
}
void printM(char a) {
	cout << a << endl;
}
*/

template <class T>//틀 ,대명사 어떤 데이터 타입이건 사용가능
void printM(T a) {
	cout << a << endl;
}

//자바의 Vector클래스 Vector <String> v = new Vector<String>(); 변수의 타입을 지정하는 방식

template<class T>
void myswap(T &a, T& b) {
	T temp;	
	temp = a;
	a = b;
	b = temp;
}
/*
void myswap(int& a, int& b) {
	int temp;
	temp = a;
	a = b;
	b = temp;
}
void myswap(char& a, char& b) {
	char temp;
	temp = a;
	a = b;
	b = temp;
}*/

int main() {
	//템플릿 클래스 사용
	//Vector처럼 T를 사용하는 클래스가 모두 float가 된다.
	//클래스는 T가 뭔지 써야함
	Point <float>a(1.3, 3.2);
	cout << a.GetX() << " " << a.GetY() << endl;
	Point <int> b(3, 2); 
	cout << b.GetX() << " " << b.GetY() << endl;

	/*
	int a = 3, b = 10;
	myswap(a, b);
	cout << a << " " << b << endl;
	char c = 'c', d = 'd';
	myswap(c, d);
	cout << c << " " << d << endl;
	
	//두개의 같은 이름의 함수 오버로딩 오버로딩할 상황은 많다.
	//
	printM(2);
	printM('a');
	*/
	/*
	* 
	Point p1 = Point();//정적할당
	Point p2 = Point(2,3);
	Point* p3 = new Point();
	Point* p4 = new Point(3, 4);

	//동적할당이 먼저 삭제됨
	delete p3;//따로 해야 소멸자가 정상적으로 작동함
	delete p4;
	*/
	/*
	* 
	//동적할당	
	//int a = 5;//main과 생명주기 동일 아래와 동일
	//int a(5);//복사 생성자 c++유형의 변수선언할때 씀
	//int a = int(5);//위와 동일 위의 3개는 정적할당
	
	int * a = new int(5); // 동적할당 new ->생명주기를 내가 컨트롤가능 메모리에 값 5를 할당하고 포인터로 메모리 주소를 가리킴 delete를 꼭 해줘야함
	//new는 malloc과 다르게 생성자가 실행됨
	//a = '\0';//주소가 바뀐 경우 먼저 선언된 메모리가 삭제되지 않는다.
	//logic
	delete a;//안해도 프로그램이 끝나면 끝난다.
	int* arr;
	int len;
	cout << "arr동적배열 크기를 정하시오:";
	cin >> len;
	arr = new int[len];
	cout << "arr 생성" << endl;
	for (int i = 0; i < len; i++)
		arr[i] = len - i;
	for (int i = 0; i < len; i++)
		cout << arr[i]<<" ";
	//delete arr;// 배열을 삭제할때 이거쓰면 맨 앞의 값만 삭제됨 배열포인터의 특징
	delete[] arr;//배열을 삭제할 때 [] 대괄호 써주기
	*/


	return 0;
}