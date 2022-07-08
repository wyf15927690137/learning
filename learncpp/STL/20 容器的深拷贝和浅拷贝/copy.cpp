#include <iostream>
using namespace std;
#include <vector>
#include <string>
#include <cstring>

//拷贝构造函数的调用时机：
// 1.对象作为函数的传入参数，以值传递的方式传入函数体
// 2.对象作为函数的返回值，以值传递的方式从函数返回
// 3.用一个对象初始化另一个对象

//浅拷贝：多个对象公用同一块资源，会导致资源的重复释放
//深拷贝：每个对象拥有各自的资源，必须显式的提供拷贝构造函数和赋值运算符
class Person
{
public:
    int mAge;
    char *mName;

public:
    Person(){};
    Person(int age, char *name)
    {
        this->mAge = age;
        this->mName = new char[strlen(name) + 1];
        strcpy(this->mName, name);
        cout << "constructor!" << endl;
    }

    Person(const Person &p) //拷贝构造函数的形参不可以通过值传递，否则会无限调用拷贝构造函数，无线递归
    {
        this->mAge = p.mAge;
        this->mName = new char[strlen(p.mName) + 1];
        strcpy(this->mName, p.mName);
        cout << "copy constructor!" << endl;
    }

    Person &operator=(const Person &p) //拷贝赋值函数可以通过值传递
    {
        if (this->mName != nullptr)
        {
            delete[] this->mName;
            this->mName = nullptr;
        }
        this->mName = new char[strlen(p.mName) + 1];
        strcpy(this->mName, p.mName);
        this->mAge = p.mAge;
        cout << "operator = overriding!" << endl;
        return *this; // return *this 返回该对象
    }

    ~Person()
    {
        if (this->mName != nullptr)
        {
            delete[] this->mName;
            this->mName = nullptr;
        }

        cout << "destructor!" << endl;
    }
};

void test01()
{
    vector<Person> vPer;
    Person p1(15, "zhangsan");
    vPer.push_back(p1); // push_back的过程会进行对象的拷贝，call copy constructor
    cout << "-----------------" << endl;
    //创建p2调用拷贝构造； vPer扩容要将所有元素拷贝： 拷贝p1； 放入p2要拷贝；销毁原来的p1
    Person p2(p1);
    vPer.push_back(p2);
    cout << "-----------------" << endl;
    //创建p3调用赋值构造； vPer扩容要将所有元素拷贝： 拷贝p1,拷贝p2； 放入p3要拷贝；销毁原来的p1,p2
    Person p3;
    p3 = p2;
    vPer.push_back(p3);
    cout << "-----------------" << endl;
    //运行结束销毁所有的Person对象
    return;
}

int main()
{
    test01();
    return 0;
}