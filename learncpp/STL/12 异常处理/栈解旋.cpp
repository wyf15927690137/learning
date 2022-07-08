#include <iostream>
using namespace std;

class Person
{
public:
    Person()
    {
        cout << "establis an object" << endl;
    }

    ~Person()
    {
        cout << "release an object" << endl;
    }
};

int divide(int a, int b)
{
    Person p1, p2;
    if (b == 0)
    {
        throw b;
    }
    return a / b;
}

void test01()
{
    try //在try语句块中，如果抛出了异常，该块的所有局部变量都会发生析构
    {
        divide(10, 0);
    }
    catch (int e)
    {
        cout << "deal with exception!" << endl;
    }
}

int main()
{
    test01();
    return 0;
}