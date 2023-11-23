#include <iostream>
using namespace std;

int main() {
	int t_num = 0;
	char city[10] = "\0";
	int price = 0;
	cout << "티켓 몇 개를 구매할건가요? " << endl;
	cin >> t_num;
	while (t_num < 1 or t_num>2)
	{
		if (t_num > 2) {
			cout << "3장이상은 구매할 수 없습니다. 2장이하로 구매하세요." << endl;
			cin >> t_num;
		}
		if (t_num < 1) {
			cout << "1장이상은 구매 해야합니다." << endl;
			cin >> t_num;
		}
	}
	cout << "어디갈건가요? " << endl;
	
	if (!strcmp(city, "manila")) {
		price = 400;
	}
	if (!strcmp(city, "newyork")) {
		price = 700;
	}
	if (!strcmp(city, "london")) {
		price = 2000;
	}
	cout << "구매성공입니다.  가격은 " << price * t_num << "원 입니다." << endl;
}