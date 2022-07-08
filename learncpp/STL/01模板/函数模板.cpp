//函数模板可以进行重载
//函数模板不允许自动类型转化，而普通函数可以
//C++编译器优先考虑普通函数，如果函数模板可以产生更好的匹配，优先考虑函数模板
#include <iostream>
using namespace std;
#include <vector>

template <typename T>
T MyAdd(T x, T y)
{
	cout << "调用模板函数" << endl;
	return x + y;
}

int MyAdd(int x, char y)
{ 
	cout<<"调用普通函数"<<endl;
	return x + y;
}

void test01()
{
	int a = 10;
	int b = 20;
	char c1 = 'a';
	char d1 = 'b';
	cout << MyAdd(a, b) << endl;	//模板   C++编译器优先考虑普通函数。如果函数模板可以产生更好的匹配，则调用函数模板
	cout << MyAdd(a, c1) << endl;	//普通
	cout << MyAdd(c1, a) << endl;	//调用普通函数，普通函数可以进行自动类型转换，而函数模板必须严格匹配数据类型
}

int main()
{
	test01();
	return 0;
}

