#include <iostream>
using namespace std;
#include <string>

class Filght {
public:
    Filght(string season, int ticket_num, string location) {
        this->season = season;
        setPeak();
        this->ticket_num = ticket_num;
        this->location = location;
    }
    void setPeak() {
        if (season.find("may") != string::npos or season.find("june") != string::npos or season.find("july") != string::npos)
            isPeak = true;
    }
    void setDistance(int distance) {
        this->distance = distance;
    }
    int getPrice() {
        if (distance < 5)
            price = 100;
        if (distance > 5 and distance < 8)
            price = 150;
        if (distance > 10)
            price = 200;
        if (isPeak)
            price = price + 50;
        return price*ticket_num;
    }

private:
    string season;
    bool isPeak = false;
    string location;
    int ticket_num;
    int price;
    int distance;
};
/*
class ManilaFilght
{
public:
    
private:
    int distance = 4;
};
class NewYorkFilght
{
public:
    
private:
    int distance = 7;
};

class LondonFilght : public Filght{
public:
    LondonFilght(string season, string location, int ticket_num) :Filght(season, ticket_num,location) {

    }
    int getPrice() {

    }
private:
    int distance = 12;
};
*/
int main()
{
    string date;
    int ticket_num;
    string loc;
    
    cout << "input departure date" << endl;
    cin >> date;   
    cout << "How many tickets will you buy?" << endl;
    cin >> ticket_num;
    while (true) {
        if (ticket_num < 3)
            break;
        cout << "there are no tickets.  Please buy the tickets not more than 3 " << endl;
        cin >> ticket_num;
    }
    cout << "where will you go? " << endl;
    cin >> loc;

    Filght* filght = new Filght(date, ticket_num, loc);
    if (loc == "manila")
        filght->setDistance(12);
    if (loc == "newyork")
        filght->setDistance(7);
    if (loc == "london")
        filght->setDistance(12);
    cout << "your purchase is successful.  Price is  " << filght->getPrice() << endl;
}   
