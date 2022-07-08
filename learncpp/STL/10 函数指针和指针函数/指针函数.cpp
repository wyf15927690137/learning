#include <iostream>
using namespace std;

//指针函数：返回值为指针的函数

int *fun1(int n)
{
    static int sum = 0;
    int *p = &sum;
    int i = 0;
    while (i <= n)
    {
        sum += i;
        i++;
    }
    return p;
}

int max(int a, int b)
{
    return a > b ? a : b;
}

int callback(int a, int b, int (*p)(int, int))
{
    return p(a, b);
}

//函数指针：一个指针，指向函数的地址；
int main()
{
    int *p = fun1(5);
    cout << *p << endl;

    int (*fun)(int, int); //函数指针的初始化
    // int (*fun)(int a,int b);//另一种初始化方法
    fun = max;
    cout << fun(13, 2) << endl;
    cout << callback(12, 14, max) << endl;
    return 0;
}