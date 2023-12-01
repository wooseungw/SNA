#include <iostream>
using namespace std;
#include <string>
//�������̵�
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
//���
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
	//����ȯ�� ���� (sting)image; �ϸ� "�̹���"�� ��µ�
	operator string() { return "�̹���"; }
	};
class ImageMessage : public Message {
public:
	ImageMessage(int sendTime, string sendName, image* image) :Message(sendTime, sendName) {
		this->image = image; 
	}
	image *getImage()const { return this->image; }//�����͵� this�׳� ����
private:
	image* image;//image Ŭ���� �����	
	};


//class TextMessage {
//public:
//	TextMessage(int sendTime, string sendName, string text) {
//		this->sendTime = sendTime;
//		this->sendName = sendName;
//		this->text = text; // (*this) text = text�� ����
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
////������
//class image {
//public:
//	//����ȯ�� ���� (sting)image; �ϸ� "�̹���"�� ��µ�
//	operator string() { return "�̹���"; }
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
//	image *getImage()const { return this->image; }//�����͵� this�׳� ����
//private:
//	int sendTime;
//	string sendName;
//	image* image;//image Ŭ���� �����
//
//};

//���� ���ε�
class Weapon {
private:
	int power;
public:
	Weapon(int power) {
		this->power = power;
	}
	//virtual�� ���� �������ε��� �Ǿ� �ڽ�Ŭ������ �Լ��� ȣ���Ѵ�.
	virtual void Use() {
		cout << "���� ���" << endl;
	}
};
class Sword: public Weapon {
public:
	Sword(int power) : Weapon(power) {}
	void Use() {
		cout << "Į ���" << endl;
		Swing();
	}
private:
	void Swing() {
		cout << "�ֵθ�" << endl;
	}
};
class Gun : public Weapon {
public:
	Gun (int power): Weapon(power){}
	void Use() {
		cout << "�� ��" << endl;
		shoot();
	}
private:
	void shoot() {
		cout << "��" << endl;
	}
};

int main() {
	Weapon *myWeapon = new Weapon(10);
	Sword mySword(15);
	Gun myGun(20);
	myWeapon = &mySword;
	//�ڽ�Ŭ������ �ȳ����� �ڽ��� use�� ��µ�
	myWeapon->Use();
	myWeapon = &myGun;
	myWeapon->Use();

	cout << "_______________________________" << endl;
	Base b;
	cout << b.a << endl;
	Child c;
	cout << c.a << endl;
	//�θ�Ŭ�������� ����ϰ������ �θ�Ŭ������:: -> �������ε�
	cout << c.Base::a << endl;
	cout << c.Child::a << endl;
	b.print();
	c.print();
	c.Base::print();
	
	b = (Base)c;

	cout << b.a << endl;

	Child e;
	//�������ε�, C++������ �� ������ base���� ��µ�
	Base* d = &e;
	cout << d->a << endl;

	//�������ε�
	cout << "_______________________________" << endl;
	TextMessage *tm = new TextMessage(9,"ģ��1","hi.");//new�� �ݵ�� �����ͺ���
	image * i = new image();//new�� �޸� �Ҵ� �������� Ŭ������ �����Ǿ��� �� new�� �������� ������ �����Ϸ��� ���� �� ���� �����Ҵ�
	ImageMessage* im = new ImageMessage(12, "ģ��2", i);
	//malloc�� ������: malloc�� �����ڸ� ȣ�������
	cout << tm->getSendTime()<<" " << tm->getSendName()<<":" << tm->getText() << endl;
	cout << im->getSendTime() << " " << im->getSendName() << ":" << (string)*im->getImage() << endl;//������ ����ȯ


	delete tm,i,im;//new�� �Ҵ�Ȱ� delete�� ����� ���ϸ� �����Ҵ� const�� �Ȱ��� 
	return 0;
}