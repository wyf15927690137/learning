////友元（访问类的私有成员）的三种形式：
//	//1.全局函数做友元
//	//2.类做友元
//	//3.类成员函数做友元
//
//普通类可以从类模板和普通类中导出，类模板也可以从普通类和类模板中导出，即普通类和类模板可以构成四种继承关系

#include <iostream>
using namespace std;

template<class T1, class T2> class Person;
template<class T1,class T2> void print(Person<T1,T2>& p);

template<class T1, class T2>
class Person
{
	friend void print<T1,T2>(Person<T1,T2>& p);
public:
	T1 mName;
	T2 mAge;
	Person(T1 name, T2 age)
	{
		this->mAge = age;
		this->mName = name;
	}
};

template<class T1,class T2>
void print(Person<T1, T2>& p)
{
	cout << p.mName << "'s age is " << p.mAge << endl;
}

int main()
{
	Person<string, int> p1("zhang", 14);
	print(p1);
	return 0;
}