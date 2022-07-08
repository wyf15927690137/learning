#include <iostream>
using namespace std;
#include <algorithm>
#include <vector>

//仿函数是一个类，而不是一个函数
//结构体的成员默认是public，而类默认是private;继承方式结构体也为public,类为private;
struct MyPrint
{
    int num = 0;
    // overloading operator()
    void operator()(int val)
    {
        num++;
        cout << val << endl;
    }
};

void test01()
{
    MyPrint print1;
    print1(14); // object print1 call operator ()
    print1(15);
    cout << print1.num << endl;

    cout << "----------------" << endl;
    MyPrint print2;
    vector<int> vec;
    vec.push_back(15);
    vec.push_back(16);
    vec.push_back(13);
    vec.push_back(14);
    MyPrint prin = for_each(vec.begin(), vec.end(), print2); //返回值类型和print2(回调函数)的类型相同
    cout << print2.num << endl;                              // for_each传入的回调函数不是引用，要做拷贝，因此print2对象不会返回正确的调用次数
    cout << prin.num << endl;
}

int main()
{
    test01();
    return 0;
}