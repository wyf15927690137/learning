#include <iostream>
using namespace std;
#include <string>

template <class T, class M>
class Person
{
public:
    Person(T name, M age)
    {
        this->mName = name;
        this->mAge = age;
    }
    void show()
    {
        cout << this->mName << "'s age is " << this->mAge << endl;
    }
public:
    T mName;
    M mAge;
};

void test01()
{
    Person<string, int> p1("zhang", 34);
    Person<char, string> p2('p', "fifty");
    p1.show();
    p2.show();
}
int main()
{
    test01();
    return 0;
}