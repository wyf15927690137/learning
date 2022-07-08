#include <iostream>
using namespace std;
#include <cstring>
#include <iomanip>

void test01()
{
    cout << "hello world!" << endl;
    cout.flush();                                          //手动刷新缓冲区
    cout.put('w').put('y').put('f') << endl;               //向缓冲区写字符
    cout.write("hello wyf", strlen("hello wyf!")) << endl; //二进制流的输出
}

//标准化输出    ios::dec(10进制)
void test02()
{
    int number = 15;
    cout << number << endl;
    cout.unsetf(ios ::dec); //卸载掉默认的10进制输出方式
    cout.setf(ios ::oct);   //设置为8进制输出
    cout << number << endl;
    cout.setf(ios::showbase); //显示8进制(0)和16进制(0X)的前缀
    cout << number << endl;
    cout.unsetf(ios::oct);
    cout.setf(ios::hex);
    cout.setf(ios::showbase); //显示8进制(0)和16进制(0X)的前缀
    cout << number << endl;
    cout << "---------------" << endl;
}

void test03()
{
    int num = 23;
    cout << num << endl;
    cout.unsetf(ios::dec);
    cout.setf(ios::hex);
    cout.setf(ios::showbase);
    cout << num << endl;
    cout.width(10); // 10个字符对齐，向左填充
    cout.fill('*');
    cout << num << endl;
    cout.width(10);       // 10个字符对齐，向左填充
    cout.setf(ios::left); //设置向右填充
    cout.fill('*');
    cout << num << endl;
    cout.setf(ios::left); //设置向右填充
    cout << "---------------" << endl;
}

void test04()
{
    int number = 57;
    cout << hex
         << setiosflags(ios::showbase)
         << setw(10)
         << setfill('~')
         << setiosflags(ios::left)
         << number
         << endl;
}
int main()
{
    test01();
    test02();
    test03();
    test04();
    return 0;
}