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

//�̳���ģ��ʱ����ָ�������T���ͣ�����������޷������ڴ�
class subPerson : Person<int>{};
void test01()
{
	//����ģ����ʹ�õ�ʱ������Զ������Ƶ�
	//��ģ�������ʾָ������
	Person<int> p1(10,19);
	p1.show();
}

int main()
{
	test01();
	return 0;
}