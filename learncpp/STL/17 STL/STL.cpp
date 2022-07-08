// STL: container algorithm iterator
#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
class Person
{
public:
    int mAge;
    string mName;

public:
    Person(int age, string name) : mAge(age), mName(name){};
};

void show(Person p)
{
    cout << p.mAge << "    " << p.mName << endl;
}

void test01()
{
    vector<Person> p;
    p.push_back(Person(34, "fafa"));
    p.push_back(Person(13, "jafa"));
    p.push_back(Person(35, "pafa"));
    p.push_back(Person(21, "tafa"));
    for_each(p.begin(), p.end(), show); // for_each call the callback function

    cout << "---------------------------" << endl;
    vector<Person>::iterator it = p.begin();
    for (it; it != p.end(); it++)
    {
        show(*it);
    }
}

int main()
{
    test01();
    return 0;
}