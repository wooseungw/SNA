#include <iostream>
using namespace std;
//먼저 선언 안하면 호출 에러
void a();
void b();
void c();

void a() {
    b();
}

void b() {
    c();
}

void c() {
    a();
}

class Point {
private:
    float x;
    float y;
public:
    //getter
    //
    float getX() const/*를 붙혀주면 이 함수에서 값이 변하는걸 막아준다. 왠만하면 getter엔 const를 쓴다.*/ {
        return x;
    }
    //const를 따로 선언한 경우에도 사용가능
    float getY() const;
    //setter
    void setX(float x) {
        x = x;//알아서 다르게 해준다.
    }
    void setY(float y) {
        this->y = y;//this로 지칭하는것도 가능
    }
    //생성자
    //입력을 따로 안받음
    Point();
    /*
    Point(): x(0),y(0) 이런 선언은 x의 복사 생성자를 사용함 콜론이 필수적 {
        //x = 0;
        //y = 0;
    }
    */
    //입력을 두개받을수 있는 생성자
    Point(float x, float y) :x(x), y(y) {

    }
    //sum을 클래스 안에 넣을 때
    static Point sum(Point a, Point b);
    Point operator+(Point a);
    Point operator*(float a, Point b) {

        return Point(b.GetX() * a, b.GetY() * a);

    }
    

};
//클래스 분리
//'클래스명::함수명'으로 어떤 클래스의 함수인지 지칭가능 
float Point::getY() const {
    return y;
}
Point Point ::sum(Point a, Point b) {
    return Point(a.getX() + b.getX(), a.getY() + b.getY());
}
//operator는 예약어
Point Point::operator+(Point a) {
    return Point(a.getX() + x, a.getY() + y);
}


//클래스 생성자 분리 입력을 따로 안받는것과 같은 선언
//헤더파일로 만들어서 include를 해서 씀
Point::Point() : x(0), y(0) {

}

int main()
{
    //기본 생성자 호출
    Point a(1,1);
    cout << a.getX() << ", " << a.getY() << endl;
    //만든 생성자로 호출
    Point b(2,3);
    cout << b.getX() << ", " << b.getY() << endl;
    /*
    //클래스 밖에 sum이 구현된 경우
    Point c = sum(a, b);
    cout << c.getX() << ", " << c.getY() << endl;
    */
    //클래스 안에 sum이 구현된 경우 
    Point c = a.sum(a, b);
    cout << c.getX() << ", " << c.getY() << endl;
    //a or b를 선언해야하는데 아예 안쓰고싶으면 선언부 sum에 static추가 구현부sum에는 추가X

    c = a.operator+(b);//연산자 오버로딩으로 operator를 재정의 한 것
    cout << c.getX() << ", " << c.getY() << endl;
    
    c = 3 * a;
}


