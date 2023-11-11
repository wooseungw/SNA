#include <iostream>
using namespace std;

int main()
{
	int ticket_num = 0;
	bool ticket_check = true;
	char city[10] = "\0";
	int price = 0;

	cout << "티켓 몇 개를 구매할건가요?";
	cin >> ticket_num;

	if (ticket_num == 1 || ticket_num == 2)
		ticket_check = false;
	while(ticket_check){
		cout << ticket_num <<"장이상은 구매할 수 없습니다. 2장이하로 구매하세요 ";
		cin >> ticket_num;
		if (ticket_num == 1 || ticket_num == 2) {
			ticket_check = false;
		}
	}
	cout << "어디 갈건가요?";
	cin >> city;
	
	while (true) {
		if (!strcmp(city, "NewYork")) {
			price = 700;
			break;
		}
		if (!strcmp(city, "manila")) {
			price = 400;
			break;
		}
		if (!strcmp(city, "London")) {
			price = 2000;
			break;
		}
		cout << "목적지가 없습니다. 어디 갈건가요?";
		cin >> city;
	}
	cout << "구매 성공입니다. 가격은" << ticket_num * price << "원 입니다." << endl;
}
