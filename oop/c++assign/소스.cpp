#include <iostream>
using namespace std;

int main() {
	int t_num = 0;
	char city[10] = "\0";
	int price = 0;
	cout << "Ƽ�� �� ���� �����Ұǰ���? " << endl;
	cin >> t_num;
	while (t_num < 1 or t_num>2)
	{
		if (t_num > 2) {
			cout << "3���̻��� ������ �� �����ϴ�. 2�����Ϸ� �����ϼ���." << endl;
			cin >> t_num;
		}
		if (t_num < 1) {
			cout << "1���̻��� ���� �ؾ��մϴ�." << endl;
			cin >> t_num;
		}
	}
	cout << "��𰥰ǰ���? " << endl;
	
	if (!strcmp(city, "manila")) {
		price = 400;
	}
	if (!strcmp(city, "newyork")) {
		price = 700;
	}
	if (!strcmp(city, "london")) {
		price = 2000;
	}
	cout << "���ż����Դϴ�.  ������ " << price * t_num << "�� �Դϴ�." << endl;
}