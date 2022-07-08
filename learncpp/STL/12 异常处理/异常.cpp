#include <iostream>
using namespace std;

int divide(int a, int b)
{
    if (b == 0)
        throw b;
    return a / b;
}

int call(int a, int b)
{
    return divide(a, b);
}

void test01()
{
    try
    {
        (divide(10, 0));
    }
    catch (int e)
    {
        cout << "exception:" << e << endl;
    }
    // 多层函数调用时，底层的异常会向上层返回，如果异常抛到顶层，还没有处理，这个时候程序会挂掉 terminate()
    // 异常必须被处理，异常是跨函数的
    try
    {
        call(20, 0);
    }
    catch (int e)
    {
        cout << "exception:" << e << endl;
    }
}

int main()
{
    test01();
    return 0;
}