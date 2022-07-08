#include <iostream>
using namespace std;

// 该函数只能抛出int,char,float这三类异常，抛出其他异常就会出错
void func() throw(int, char, float)
{
    throw -1;
}

// 该函数不能抛出任何异常
void func1() throw()
{
    throw -1; //这里会发生警告
}

//该函数可以抛出所有类型的异常
void func3()
{
}

void test01()
{
    try
    {
        func();
        func1();
        func3();
    }
    catch (int)
    {
        cout << "int exception" << endl;
    }
    catch (char)
    {
        cout << "char exception" << endl;
    }
    catch (...) //捕获所有异常
    {
        cout << "all exception" << endl;
    }
}

int main()
{
    test01();
    return 0;
}