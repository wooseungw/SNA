#include <iostream>
using namespace std;
#include <string>
//오버라이딩
class Base {
public:
	int a = 10;
	void print() {
		cout << "BASE" << endl;
	}
};
class Child :public Base{
public:
	int a = 20;
	void print() {
		cout << "CHILD" << endl;
	}
};
//상속
class Message {
public:
	Message(int sendTime, string sendName) {
		this->sendTime = sendTime;
		this->sendName = sendName;
	}
	int getSendTime()const { return this->sendTime; }
	string getSendName()const { return this->sendName; }
private:
	int sendTime;
	string sendName;
};
class TextMessage : public Message {
public:
	TextMessage(int sendTime, string sendName,string text) :Message(sendTime,sendName){
		this->text = text;
	}
	string getText()const { return this->text; }
private:
	string text;
};
class image {
public:
	//형변환시 사용됨 (sting)image; 하면 "이미지"가 출력됨
	operator string() { return "이미지"; }
	};
class ImageMessage : public Message {
public:
	ImageMessage(int sendTime, string sendName, image* image) :Message(sendTime, sendName) {
		this->image = image; 
	}
	image *getImage()const { return this->image; }//포인터도 this그냥 쓰기
private:
	image* image;//image 클래스 만들기	
	};


//class TextMessage {
//public:
//	TextMessage(int sendTime, string sendName, string text) {
//		this->sendTime = sendTime;
//		this->sendName = sendName;
//		this->text = text; // (*this) text = text와 같음
//
//	}
//	int getSendTime()const {return this->sendTime;}
//	string getSendName()const { return this->sendName; }
//	string getText()const { return this->text; }
//private:
//	int sendTime;
//	string sendName;
//	string text;
//};
//
////다형성
//class image {
//public:
//	//형변환시 사용됨 (sting)image; 하면 "이미지"가 출력됨
//	operator string() { return "이미지"; }
//};
//
//class ImageMessage {
//public:
//	ImageMessage(int sendTime, string sendName, image* image) {
//		this->sendTime = sendTime;
//		this->sendName = sendName;
//		this->image = image; 
//	}
//	int getSendTime()const { return this->sendTime; }
//	string getSendName()const { return this->sendName; }
//	image *getImage()const { return this->image; }//포인터도 this그냥 쓰기
//private:
//	int sendTime;
//	string sendName;
//	image* image;//image 클래스 만들기
//
//};

//동적 바인딩
class Weapon {
private:
	int power;
public:
	Weapon(int power) {
		this->power = power;
	}
	//virtual을 쓰면 동적바인딩이 되어 자식클래스의 함수를 호출한다.
	virtual void Use() {
		cout << "무기 사용" << endl;
	}
};
class Sword: public Weapon {
public:
	Sword(int power) : Weapon(power) {}
	void Use() {
		cout << "칼 사용" << endl;
		Swing();
	}
private:
	void Swing() {
		cout << "휘두름" << endl;
	}
};
class Gun : public Weapon {
public:
	Gun (int power): Weapon(power){}
	void Use() {
		cout << "총 쏨" << endl;
		shoot();
	}
private:
	void shoot() {
		cout << "슛" << endl;
	}
};

int main() {
	Weapon *myWeapon = new Weapon(10);
	Sword mySword(15);
	Gun myGun(20);
	myWeapon = &mySword;
	//자식클래스께 안나오고 자신의 use가 출력됨
	myWeapon->Use();
	myWeapon = &myGun;
	myWeapon->Use();

	cout << "_______________________________" << endl;
	Base b;
	cout << b.a << endl;
	Child c;
	cout << c.a << endl;
	//부모클래스값을 출력하고싶으면 부모클래스명:: -> 정적바인딩
	cout << c.Base::a << endl;
	cout << c.Child::a << endl;
	b.print();
	c.print();
	c.Base::print();
	
	b = (Base)c;

	cout << b.a << endl;

	Child e;
	//정적바인딩, C++에서만 씀 무조건 base값이 출력됨
	Base* d = &e;
	cout << d->a << endl;

	//동적바인딩
	cout << "_______________________________" << endl;
	TextMessage *tm = new TextMessage(9,"친구1","hi.");//new는 반드시 포인터변수
	image * i = new image();//new는 메모리 할당 많은수의 클래스가 생성되었을 때 new로 선언하지 않으면 컴파일러가 지울 수 있음 동적할당
	ImageMessage* im = new ImageMessage(12, "친구2", i);
	//malloc과 차이점: malloc은 생성자를 호출안해줌
	cout << tm->getSendTime()<<" " << tm->getSendName()<<":" << tm->getText() << endl;
	cout << im->getSendTime() << " " << im->getSendName() << ":" << (string)*im->getImage() << endl;//포인터 형변환


	delete tm,i,im;//new로 할당된건 delete로 지운다 안하면 정적할당 const와 똑같음 
	return 0;
}