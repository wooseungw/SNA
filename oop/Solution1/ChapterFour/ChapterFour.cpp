#include <iostream>
using namespace std;

class CTest {
    char arr[16];
};
class CTest2
{
public:
    int i = 0;
    int j = 0;
private:
    int k = 0;
};


int main()
{
    CTest2 t2;
    t2.i = 12;
    t2.j = 21;
    CTest2* pt2 = &t2;
    cout << t2.i << endl;
    cout << (*pt2).i << " " << (*pt2).j << endl; //*는 값 참조 .이 연산자 우선순위가 높으므로 ()를 쳐준다.
    //포인터는 배열의 역할
    pt2->i = 2;//이렇게 접근을 더 많이 함, 위와 동일한 역할
    cout << pt2->i << endl;

    CTest t;
    CTest* pt = &t;

    cout << pt << endl;
    pt++;
    cout << pt << endl; //16진수라 두번째 자리가 1증가하면 16byte가 증가한것 10만큼 증가한게 아님
    cout << ++pt << endl; 
    cout << ++pt << endl; 

    //char* pC = NULL;
    //int* pI = NULL;
    //double* pD = NULL;
    //cout << (void*)(pC + 1) << (void*)(pI + 1) << (void*)(pD + 1) <<endl; // double이나 int형은 8,4byte이기 때문에 +1하면 8byte와 4byte를 건너뛴다 char는 1byte라 1칸증가

    //int i = 0;
    //int a = 1;
    //cout << "adress:" << &a << ", value:" << a << endl;
    //int* ap = &a; //a에 대한 참조
    //cout << "adress:" << ap + 1 << ", value:" << *ap + 1 << endl;
    //int b = 65;
    ////char* cp = &a;//오류
    //char* cp = (char*)&b;
    //*(cp + 1) = 'B';
    //*(cp + 2) = 'C';
    //*(cp + 3) = 'D';
    //*(cp + 4) = '\0';
    //  cout <<  (char*) & b << endl;
    

    /*
    for (i =1 ; i < 10; i++) {
        for (int j = 1; j < 10; j++) {
            if (j == 3 and i == 3)
                cout << endl;
            else    
                cout << i << " * " << j << " = " << i * j << endl;
        }
        cout << endl;
    }*/
    /*for (; ; ){
        sum += i;
        cout << i << " ";
        i++;
        if (i > 10) break;     
    }
    cout << "for: " << sum << endl;
    cout << endl;
    i = 0;
    sum = 0;
    while (1) {
        sum += i;
        cout << i <<" ";
        
        i++;
        if (i > 10) break;
    }
    cout << "while: " << sum << endl;
    cout << endl;
    i = 0;
    sum = 0;
    do {
        sum += i;
        cout << i << " ";
        i++;
    } while (i < 11);*/


    
}
