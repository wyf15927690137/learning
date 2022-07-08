#include <iostream>
using namespace std;
#include <cstring>
void func1()
{
    throw 1;
}

void func2()
{
    throw(char *) "exception";
}

class MyException
{
public:
    char *error;

public:
    MyException(char *str)
    {
        this->error = new char[strlen(str) + 1];
        strcpy(this->error, str);
    }

    MyException(const MyException &ex)
    {
        this->error = new char[strlen(ex.error) + 1];
        strcpy(this->error, ex.error);
    }

    MyException &operator=(const MyException &ex)
    {
        if (this->error != nullptr)
        {
            delete[] this->error;
            this->error = nullptr;
        }
        this->error = new char[strlen(ex.error) + 1];
        strcpy(this->error, ex.error);
        return *this;
    }

    void what()
    {
        cout << this->error << endl;
    }

    ~MyException()
    {
        if (this->error != nullptr)
            delete[] error;
    }
};

void func3()
{
    throw MyException((char *)"a new exception"); //调用构造函数生成匿名对象，抛出
}

void test01()
{
    try
    {
        func1();
    }
    catch (int e)
    {
        cout << "catch int exception:" << e << endl;
    }

    try
    {
        func2();
    }
    catch (char *x)
    {
        cout << "catch char* exception:" << *x << "  " << x << endl;
    }

    try
    {
        func3();
    }
    catch (MyException ex)
    {
        cout << "catch class exception:";
        ex.what();
    }
}

void test02()
{
    char *s1 = (char *)"string";
    cout << s1 << endl; // char*s 中输出s
}
int main()
{
    test01();
    test02();
    return 0;
}
