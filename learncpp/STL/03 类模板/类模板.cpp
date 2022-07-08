#include <iostream>
using namespace std;

template <class T>

class Person
{
public:
	Person(T id, T age)
	{
		this->mID = id;
		this->mAge = age;
	}

	void show()
	{
		cout << "ID: " << mID << "  " << "Age:  " << mAge << endl;
	}
public:
	T mID;
	T mAge;
};

//继承类模板时必须指明父类的T类型，否则编译器无法分配内存
class subPerson : Person<int>{};
void test01()
{
	//函数模板在使用的时候可以自动类型推导
	//类模板必须显示指定类型
	Person<int> p1(10,19);
	p1.show();
}

int main()
{
	test01();
	return 0;
}