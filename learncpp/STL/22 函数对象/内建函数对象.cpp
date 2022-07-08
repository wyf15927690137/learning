#include <iostream>
using namespace std;
#include <functional>

//谓词：返回值为bool类型的函数或者仿函数
//谓词有一个传入参数，一元谓词；两个传入参数，二元谓词

// STL有内建函数对象
void test01()
{
    plus<int> pl;
    cout << pl(19, 21) << endl;
}

int main()
{
    test01();
    return 0;
}