#include <iostream>
using namespace std;

class MyException
{
public:
    MyException()
    {
        cout << "constructor!" << endl;
    }

    MyException(const MyException &ex)
    {
        cout << "copy constructor!" << endl;
    }

    ~MyException()
    {
        cout << "destructor!" << endl;
    }
};

void func()
{
    throw MyException(); //调用构造函数
}
void test01()
{
    try
    {
        func();
    }
    //普通元素，异常对象，catch 处理完之后就析构

    catch (MyException ex) //调用拷贝构造函数
    {
        cout << "catch exception!" << endl;
    }

    cout << "--------------------" << endl;
    try
    {
        func();
    }

    //而对于catch的引用，不用调用拷贝构造函数，异常对象处理完之后就析构
    catch (MyException &ex) //不调用拷贝构造函数
    {
        cout << "catch exception!" << endl;
    }
}

int main()
{
    test01();
    return 0;
}