//����ģ����Խ�������
//����ģ�岻�����Զ�����ת��������ͨ��������
//C++���������ȿ�����ͨ�������������ģ����Բ������õ�ƥ�䣬���ȿ��Ǻ���ģ��
#include <iostream>
using namespace std;
#include <vector>

template <typename T>
T MyAdd(T x, T y)
{
	cout << "����ģ�庯��" << endl;
	return x + y;
}

int MyAdd(int x, char y)
{ 
	cout<<"������ͨ����"<<endl;
	return x + y;
}

void test01()
{
	int a = 10;
	int b = 20;
	char c1 = 'a';
	char d1 = 'b';
	cout << MyAdd(a, b) << endl;	//ģ��   C++���������ȿ�����ͨ�������������ģ����Բ������õ�ƥ�䣬����ú���ģ��
	cout << MyAdd(a, c1) << endl;	//��ͨ
	cout << MyAdd(c1, a) << endl;	//������ͨ��������ͨ�������Խ����Զ�����ת����������ģ������ϸ�ƥ����������
}

int main()
{
	test01();
	return 0;
}

