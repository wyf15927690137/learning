#include <iostream>
using namespace std;

void test01()
{
    char *s;
    //把第一个字符‘h’的地址转换为char*类型并接受
    //字符串常量的本质是其第一个字符的地址（编译器将字符串常量视为一个地址）
    //与数组名类似，数组名也为其第一个元素的地址
    s = (char *)("hello world"); // s = "hello world";   //发生隐式类型转换，可能发出警告
    cout << s[0] << s[5] << s[6] << endl;
}

void test02()
{
    char a[5] = "hell";
    char *s1 = a;                                     // char* s可以看作是字符数组（字符串）的首地址
    cout << s1[2] << s1[3] << endl;                   // 默认s1[4]='\0'
    cout << sizeof(a) << "   " << sizeof(s1) << endl; // a为字符数组，其大小为字符串的大小，为5；s1为一个指针，大小为4个字节
}

void test03()
{
    char str1[] = "hello";       //"hello"是字符串常量，初始化在常量区，将常量区的值赋给变量str1,str1在栈中;
    char str2[] = "hello";       // str2也在栈中，其地址与str1不同
    char *str3 = "hello";        // str3指向常量区中"hello"的首地址
    char *str4 = "hello";        // str4指向常量区中"hello"的首地址
    const char str5[] = "hello"; // const使得指针无法指向新的地址
    const char str6[] = "hello";
    const char *str7 = "hello";
    const char *str8 = "hello";
    cout << (str1 == str2) << endl;
    cout << (str3 == str4) << endl;
    cout << (str5 == str6) << endl;
    cout << (str7 == str8) << endl;
}
int main()
{
    test01();
    test02();
    test03();
    return 0;
}