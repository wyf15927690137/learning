////��Ԫ���������˽�г�Ա����������ʽ��
//	//1.ȫ�ֺ�������Ԫ
//	//2.������Ԫ
//	//3.���Ա��������Ԫ
//
//��ͨ����Դ���ģ�����ͨ���е�������ģ��Ҳ���Դ���ͨ�����ģ���е���������ͨ�����ģ����Թ������ּ̳й�ϵ

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