#include "Person.hpp"
//����ģ����Ҫ���ж��α��룬����Ҫ�ж�����ģ����ļ��������ɾ������
//hpp����ʵ�ʾ��ǽ�.cpp��ʵ�ִ������.hͷ�ļ����У�������ʵ�ֶ�������ͬһ�ļ�
int main()
{
	Person<string, int> p1("zhang", 12);
	p1.show();
	return 0;
}