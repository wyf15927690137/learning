#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <cstring>

//�������캯���ĵ���ʱ����
// 1.������Ϊ�����Ĵ����������ֵ���ݵķ�ʽ���뺯����
// 2.������Ϊ�����ķ���ֵ����ֵ���ݵķ�ʽ�Ӻ�������
// 3.��һ�������ʼ����һ������
class Person
{
public:
    int mAge;
    char* mName;

public:
    Person() {};
    Person(int age, char* name)
    {
        this->mName = new char[strlen(name) + 1];
        strcpy(this->mName, name);
        this->mAge = age;
        cout << "constructor!" << endl;
    }

    Person(const Person& p) //�������캯�����ββ�����ͨ��ֵ���ݣ���������޵��ÿ������캯�������ߵݹ�
    {
        this->mAge = p.mAge;
        this->mName = new char[strlen(p.mName) + 1];
        strcpy(this->mName, p.mName);
        cout << "copy constructor!" << endl;
    }
    // operator = overloading
    Person& operator=(const Person& p) //������ֵ��������ͨ��ֵ����
    {
        if (this->mName != nullptr)
        {
            delete[] this->mName;
            this->mName = nullptr;
        }

        this->mName = new char[strlen(p.mName) + 1];
        strcpy(this->mName, p.mName);
        cout << "operator = overloading" << endl;
        return *this;
    }

    ~Person()
    {
        if (this->mName != nullptr)
            delete[] this->mName;
        this->mName = nullptr;
        cout << "destructor!" << endl;
    }
};

void test01()
{
    vector<Person> vPer;
    Person p1(12, (char*)"zhangsan");
    Person p2 = p1;     //���ÿ������캯��
    vPer.push_back(p1); // STL��������Ԫ�ص�ʱ�򶼻�ʵʩ�����������������ÿ������캯��

    Person p3;
    p3 = p2; //�������ص�=
}

int main()
{
    test01();
    return 0;
}