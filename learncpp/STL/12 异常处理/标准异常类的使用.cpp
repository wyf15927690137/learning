//当继承标准异常类的时候，需要重载父类的what()函数和虚析构函数
#include <iostream>
using namespace std;
#include <stdexcept>
#include <cstring>
class Person
{
public:
    int mAge;

public:
    Person(int age)
    {
        if (age < 0 || age > 100)
        {
            throw out_of_range((char *)"The age should be in the range of 0-100!");
        }
        this->mAge = age;
    }
};

void test01()
{
    try
    {
        Person p1(1000);
    }
    catch (out_of_range e)
    {
        cout << e.what() << endl;
    }
}

//当继承标准异常类的时候，需要重载父类的what()函数和虚析构函数
class MyOutOfRange : public exception
{
public:
    char *pError;

public:
    MyOutOfRange(char *erro)
    {
        this->pError = new char[strlen(erro) + 1];
        strcpy(this->pError, erro);
    }

    virtual const char *what()
    {
        return pError;
    }

    virtual ~MyOutOfRange()
    {
        if (this->pError != nullptr)
            delete[] this->pError;
    }
};

void func()
{
    throw MyOutOfRange((char *)"my out of range!");
}
void test02()
{
    try
    {
        func();
    }
    catch (MyOutOfRange &e) //用引用接受创建的异常对象，只会调用构造函数而不会调用拷贝构造函数
    {
        cout << e.what() << endl;
    }
}
int main()
{
    test01();
    cout << "--------------------" << endl;
    test02();
    return 0;
}