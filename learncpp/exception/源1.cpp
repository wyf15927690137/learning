#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <cstring>

//拷贝构造函数的调用时机：
// 1.对象作为函数的传入参数，以值传递的方式传入函数体
// 2.对象作为函数的返回值，以值传递的方式从函数返回
// 3.用一个对象初始化另一个对象
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

    Person(const Person& p) //拷贝构造函数的形参不可以通过值传递，否则会无限调用拷贝构造函数，无线递归
    {
        this->mAge = p.mAge;
        this->mName = new char[strlen(p.mName) + 1];
        strcpy(this->mName, p.mName);
        cout << "copy constructor!" << endl;
    }
    // operator = overloading
    Person& operator=(const Person& p) //拷贝赋值函数可以通过值传递
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
    Person p2 = p1;     //调用拷贝构造函数
    vPer.push_back(p1); // STL容器插入元素的时候都会实施拷贝动作，这里会调用拷贝构造函数

    Person p3;
    p3 = p2; //调用重载的=
}

int main()
{
    test01();
    return 0;
}