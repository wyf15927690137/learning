//#include<iostream>
//#include<stdexcept>
//#include<Windows.h>
//using namespace std;
//int main()
//{
//	int a, b;
//error1:try {
//	cin >> a >> b;
//	if (b == 0)
//		throw runtime_error("b can't be 0.\n");
//}
//catch (...) {
//	cout << "Do you want to input again ?\n Enter y or n." << endl;
//	char c;
//	cin >> c;
//	if (c == 'y')
//		goto error1;
//}
//cout << a / b;
//system("pause");
//return 0;
//}

#include <iostream>
using namespace std;

void func1()
{
    int a, b;
    cin >> a >> b;
    if (b == 0)
    {
        throw string("除0错误");
    }
    else
    {
        cout << a / b << endl;
    }
}


int main()
{
    try
    {
        func1();
    }
    catch (const char* errmsg)  //不可以捕获string的异常
    {
        cout << errmsg << endl;
    }
    catch (...)  //可以捕获string的异常
    {
        cout << "string 异常"  << endl;
    }
    return 0;
}