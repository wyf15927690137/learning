#include <iostream>
using namespace std;

//指针常量，*p为常量，指向的值不可以改变
void test01()
{
    int a = 5;
    int b = 7;
    const int *p;
    p = &a;
    p = &b;
    //*p = a;   *p是常量，不可以更改；而p是变量
    cout << *p << endl;
}

//常量指针，指向的地址不可以改变
void test02()
{
    int a = 5;
    int *const p = &a; //必须初始化，p是常量，指向的地址不可以改变
    // p = &b;
    *p = 9;
    cout << a << endl;
}
int main()
{
    test01();
    test02();
    return 0;
}