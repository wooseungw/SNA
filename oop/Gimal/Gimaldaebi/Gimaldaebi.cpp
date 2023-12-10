// Gimaldaebi.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

using namespace std;
#include <iostream>
class Point {
private:
    int x;
    int y;
public:
    Point();
    Point(int x, int y){
        this->x = x;
        this->y = y;
        cout << x << ", " << y << endl;
    }//생성자
    ~Point() {
        cout << "소멸자\n";
    }
    int GetX() const {
        return x;
    }
    int GetY()const {
        return y;
    }
    
    Point operator+(Point a);
    Point operator*(float b) {
        return Point(x * b, y * b);
    }
    
};


class MakeSqaure : Point{
private:
    int width;
    int height;
public:
    MakeSqaure(int x,int y):Point(x,y), width(x+10),height(y+10){
        cout << x << ", " << y << ", " << width << ", " << height<<endl;
    }
    void PrintSqaurefix(int width, int height);
    void PrintSquare() {
        cout << '_' * width << endl;
        for (int i =0 ;i<height ; i++)
            cout << '|' << ' ' * width << '|'<< endl;
        cout << '_' * width << endl;
    }
};
Point::Point(): x(0),y(0) {
    cout << x << ", " << y << endl;
}
Point Point::operator+(Point a) {
    return Point(a.GetX() + x, a.GetY() + y);
}

void MakeSqaure:: PrintSqaurefix(int width, int height) {
    for (int i = 0; i < width; i++)
        cout << "-";
    cout << endl;
    for (int i = 0; i < height; i++){
        cout << '|';
        for (int j = 0; j < width-2; j++)
            cout << " ";
        cout << '|'<<endl;
    }
    for (int i = 0; i < width; i++)
        cout << "-";
    cout << endl;
    
}


int main()
{
    Point* p = new Point(12, 54);
    Point p0(1, 2);
    Point c(0, 0);
    c = p->operator+(p0);
    cout << "C의 X:" << c.GetX() << "C의 Y:" << c.GetY() << endl;
    MakeSqaure ms = MakeSqaure(10,10);
    ms.PrintSqaurefix(10,10);
    c = p ->operator*(2);
    //cout << "C의 X:" << c.GetX() << "C의 Y:" << c.GetY() << endl;
    std::cout << "Hello World!\n";

    delete p;
    
}
