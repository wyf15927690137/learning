//标准输入：从键盘输入到程序 input
//标准输出: 从程序输出数据到显示器 output
//标准输入+标准输出=标准IO

//文件的输入和输出叫做文件IO
#include <iostream>
using namespace std;

//键盘输入到输入缓冲区，程序从输入缓冲区读取数据
//程序将数据输出到输出缓冲区，输出缓冲区显示到显示器
void test01()
{
    cout; //全局流对象，和显示器关联
    cin;
    // cerr没有缓冲区，clog有缓冲区
    cerr; //标准错误
    clog; //标准日志
}

//标准输入流
void test02()
{
    char ch;
    while ((ch = cin.get()) != EOF) // EOF: end of file
    {
        cout << ch << endl;
    }
}

void test03()
{
    while (cin.get() != EOF)
    {
        char ch;
        cin.get(ch); //读取一个字符到ch,会把字符取走
        cout << ch << endl;

        char ch1[256] = {0};
        cin.get(ch1, 256);
        cout << ch1 << endl; //读取一个字符串到ch1
    }
}

void test04()
{
    char ch2[256] = {0};
    cin.getline(ch2, 256); //读取一整行,不读换行符
    cout << ch2 << endl;
}

void test05()
{
    char ch;
    cin.get(ch);
    cout << ch << endl;
    cin.ignore(); //忽略一个字符,从缓冲区取走字符了
    cin.get(ch);
    cout << ch << endl;
    cin.ignore(3); //忽略3个字符
    cin.get(ch);
    cout << ch << endl;
    cin.ignore(100, '\n'); //清掉'\n'之前的100个字符
    cin.get(ch);
    cout << ch << endl;
}

void test06()
{
    cout << "please input a number or a string :" << endl;
    char ch;
    ch = cin.peek(); //预览缓冲区的第一个字符，不会取走数据
    if (ch >= '0' && ch <= '9')
    {
        int num;
        cin >> num;
        cout << "the input is a number: " << num << endl;
    }
    else
    {
        char buf[256] = {0};
        cin >> buf;
        cout << "the input is a string: " << buf << endl;
    }
}

void test07()
{
    char ch;
    ch = cin.get();
    if (ch >= '0' && ch <= '9')
    {
        cin.putback(ch); //将一个字符放回缓冲区
        int num;
        cin >> num;
        cout << "the input is a number: " << num << endl;
    }
    else
    {
        cin.putback(ch);
        string s;
        cin >> s;
        cout << "the input is a string: " << s << endl;
    }
}
int main()
{
    // test02();
    // test03();
    // test04();
    // test05();
    // test06();
    test07();
    return 0;
}
