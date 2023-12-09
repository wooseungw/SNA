// 시험은 실습으로
// 11/22,11/30,12/7의 코드로 문제를 냄
// clas Weapon등을 몇가지 빼서 줌 정답과 동일한 출력을 내는게 목표 7문제 코드를 붙혀넣고 결과화면 캡쳐후 제출
// ex) 오퍼레이터
//Virtual을 쓰면 자식클래스의 함수가 실행됨
#include<iostream>
using namespace std;


class Image {

public:

	operator string() {

		return "사진";

	}

};

class Message {

private:

	int sendTime;

	string sendName;

public:

	Message(int sendTime, string sendName) {

		this->sendTime = sendTime;

		this->sendName = sendName;

	}

	int GetsendTime() const { return sendTime; }

	string GetSendName() const { return sendName; }
	//부모 클래스에서 vitual을 하고 자식클래스가 호출되는경우 자식클래스의 함수를 가져온다.
	//없으면 무조건 부모클래스의 함수가 실행됨
	virtual string GetContent() const { return ""; }

};

class TextMessage :public Message {

public:

	TextMessage(int sendTime, string sendName, string text) :Message(sendTime, sendName) {
		this->text = text;
	}
	string GetText() const { return text; }

	string GetContent() const {	return text; }
private:
	string text;
};

class ImageMessage :public Message {

private:


	Image* image;

public:

	ImageMessage(int sendTime, string sendName, Image* image) :
		Message(sendTime, sendName), image(image) {

	}

	Image* GetImage() const { return image; }


	//
	string GetContent() const {	return *this->GetImage(); }

};

void printMessage(TextMessage* m) {

	cout << "보낸사람" << m->GetSendName();

	cout << "보낸시간" << m->GetsendTime();

	cout << "보낸내용" << m->GetContent() << endl;

}

//동적바인딩으로 어쩔땐 텍스트 어쩔땐 이미지를 보내도록 바꾸기
void printTextMessage(TextMessage* m) {

cout << "보낸사람: " << m->GetSendName();

cout << " 보낸시간: " << m->GetsendTime();

cout << " 보낸내용: " << m->GetContent() << endl;//getText -> getcontent로 바꿈

}

void printImageMessage(ImageMessage* m) {

	cout << ",보낸사람: " << m->GetSendName();

	cout << ",보낸시간: " << m->GetsendTime();

	cout << ",보낸내용: " << m->GetContent() << endl;



}
//getText와 getImage를 getContents로 통합
void printMessage(Message* m) {
	cout << "보낸사람: " << m->GetSendName();
	cout << ", 보낸시간: " << m->GetsendTime();
	cout << ", 보낸내용: " << m->GetContent() << endl;;
}

// 상황에 따라 여러 클래스를 하나의 클래스처럼 쓸 수 있다.
// 상속이 겹쳐지고 클래스의 계통도가 어지러울때 문서를보자.(클래스 다이어그램) 모아놓은게 UML 
// 비주얼슽
int main2() {
	
	// TextMessage* m를 Message *m으로
	Message* m = new TextMessage(10, "병하", "안녕");
	

	Image* i = new Image();
	Message* im = new ImageMessage(11, "병하2", i);
	
	cout << endl;
	//printTextMessage(m);
	//printImageMessage(im);
	cout << endl;
	printMessage(m);
	printMessage(im);
	delete m,i, im;
	/*
	Message* t = new TextMessage(10, "병하", "안녕");

	printMessage(t);

	Image* i = new Image();

	Message* im = new ImageMessage(11, "병하2", i);

	im->GetContent();

	printMessage(im);
	*/
	delete im, i, m;
	return 0;
}

