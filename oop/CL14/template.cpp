#include<iostream>
using namespace std;

//�����Ҵ�
int b = 3;//���μ��� �����ֱ�� ����
#include<iostream>



using namespace std;



//Ŭ������ new�� ���������
//���ø��� ������� ��
//�ΰ��� ��밡��
//STL Standard Tempelate Library cppreference���� , ���迣 �ȵ�

template <class T,class T2>
class Point {
public:
	Point() :x(0), y(0) {
		cout << this << " ������ Point()" << endl;
	}
	Point(T x, T y) :x(x), y(y) {
		cout << this << " ������ Point(x,y)" << endl;
	}
	~Point()/*�Ҹ���*/ {
		cout << this << "�Ҹ��� ~Point()" << endl;
	}
	T GetX() { return x; }
	T GetY() { return y; }

private:
	//Ÿ���� �������
	//Ÿ���� �ٸ����
	T x;
	T2 y;
};
//�ΰ��� ���� �̸��� �Լ� �����ε�
/*
void printM(int a) {
	cout << a << endl;
}
void printM(char a) {
	cout << a << endl;
}
*/

template <class T>//Ʋ ,���� � ������ Ÿ���̰� ��밡��
void printM(T a) {
	cout << a << endl;
}

//�ڹ��� VectorŬ���� Vector <String> v = new Vector<String>(); ������ Ÿ���� �����ϴ� ���

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
	//���ø� Ŭ���� ���
	//Vectoró�� T�� ����ϴ� Ŭ������ ��� float�� �ȴ�.
	//Ŭ������ T�� ���� �����
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
	
	//�ΰ��� ���� �̸��� �Լ� �����ε� �����ε��� ��Ȳ�� ����.
	//
	printM(2);
	printM('a');
	*/
	/*
	* 
	Point p1 = Point();//�����Ҵ�
	Point p2 = Point(2,3);
	Point* p3 = new Point();
	Point* p4 = new Point(3, 4);

	//�����Ҵ��� ���� ������
	delete p3;//���� �ؾ� �Ҹ��ڰ� ���������� �۵���
	delete p4;
	*/
	/*
	* 
	//�����Ҵ�	
	//int a = 5;//main�� �����ֱ� ���� �Ʒ��� ����
	//int a(5);//���� ������ c++������ ���������Ҷ� ��
	//int a = int(5);//���� ���� ���� 3���� �����Ҵ�
	
	int * a = new int(5); // �����Ҵ� new ->�����ֱ⸦ ���� ��Ʈ�Ѱ��� �޸𸮿� �� 5�� �Ҵ��ϰ� �����ͷ� �޸� �ּҸ� ����Ŵ delete�� �� �������
	//new�� malloc�� �ٸ��� �����ڰ� �����
	//a = '\0';//�ּҰ� �ٲ� ��� ���� ����� �޸𸮰� �������� �ʴ´�.
	//logic
	delete a;//���ص� ���α׷��� ������ ������.
	int* arr;
	int len;
	cout << "arr�����迭 ũ�⸦ ���Ͻÿ�:";
	cin >> len;
	arr = new int[len];
	cout << "arr ����" << endl;
	for (int i = 0; i < len; i++)
		arr[i] = len - i;
	for (int i = 0; i < len; i++)
		cout << arr[i]<<" ";
	//delete arr;// �迭�� �����Ҷ� �̰ž��� �� ���� ���� ������ �迭�������� Ư¡
	delete[] arr;//�迭�� ������ �� [] ���ȣ ���ֱ�
	*/


	return 0;
}