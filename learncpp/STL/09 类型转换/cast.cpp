#include <iostream>
using namespace std;

class Animal
{
};
class Cat : public Animal
{
};

class Building
{
};

// static_cast: 用于基础类型的转换
//拥有继承关系的指针或者引用的转换
void test01()
{
    int a = 104;
    char c = static_cast<char>(a);
    cout << c << endl;

    // 拥有继承关系的指针或者引用的转换
    Animal *ani = nullptr;
    Cat *cat = static_cast<Cat *>(ani);

    Cat *cat1 = nullptr;
    Animal *ani1 = static_cast<Animal *>(cat1);

    Animal ani2;
    Animal &ani3 = ani2;
    Cat &cat2 = static_cast<Cat &>(ani3);
}

// dynamic_cast: 用于具有继承关系的指针或者引用的类型转换
// 且要做类型安全检查,即只能由子类型转变为父类型
// static_cast 没有安全类型检查
void test02()
{
    Cat *cat = nullptr;
    Animal *ani = dynamic_cast<Animal *>(cat);
    Animal *ani1 = nullptr;
    // Cat *cat1 = dynamic_cast<Cat *>(ani1);
}

// const_cast: 对基础数据类型或者指针增加或者去除const属性
void test03()
{
    const int a = 5;
    int *b = const_cast<int *>(&a); //把一个const变量赋值给非const变量
    *b = 20;
    cout << a << "  " << *b << endl;

    int &c = const_cast<int &>(a);
    c = 10;
    cout << a << "  " << c << endl;

    //指针的const属性
    int *p = nullptr;
    const int *q = const_cast<const int *>(p);
    //*q = c;   //不能通过指针来修改*q的值

    const int *p1 = nullptr;
    int *q1 = const_cast<int *>(p1);
}

// reinterpet_cast
void test04()
{
    // 1.无关类型的相互转换
    Building *bul = nullptr;
    Animal *ani = reinterpret_cast<Animal *>(bul);

    // 2.函数指针的转换
}
int main()
{
    test01();
    test02();
    test03();
    return 0;
}