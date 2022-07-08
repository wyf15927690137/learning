#include <iostream>
using namespace std;
#include <string>

// string 是一个char* 型的容器
// string 类管理char* 所分配的内存，不需要考虑内存释放和越界

// string and char* transformation
void test01()
{
    string str = "abcdefg";
    const char *cstr = str.c_str();
    cout << cstr << endl;
    char *s = "fafaf";
    string ss(s);
    cout << ss << endl;
    cout << "-------------------" << endl;
}

// initaileze
void test02()
{
    string s = "dada";
    string s1("abs");
    string s2(s1);
    string s3(10, 'a');
    cout << s << endl;
    cout << s1 << endl;
    cout << s2 << endl;
    cout << s3 << endl;
}

void test03()
{
    string s;
    s.assign("abcdefg"); //赋值

    for (int i = 0; i < s.length(); i++)
    {
        cout << s[i] << " ";
    }

    cout << endl;

    for (int i = 0; i < s.size(); i++) // at 越界之后会抛出异常out_of_range，而[]不会抛出异常
    {
        cout << s.at(i) << " ";
    }
    cout << endl;
    try
    {
        cout << s.at(100) << endl;
    }
    catch (out_of_range)
    {
        cout << "exception!" << endl;
    }
    cout << "--------------------------" << endl;
}

//拼接操作
void test04()
{
    string s1 = "aaa";
    s1 += "bbbb";
    string s2 = "cccc";
    string s3 = s1 + s2;
    string s4 = s3.append("ddddd");
    string s5 = s4.append(s1);
    cout << s5 << endl;
    cout << "-------------------------" << endl;
}

// find
void test05()
{
    string s = "abcdefghijklmnop";
    int pos = s.find("ghi");
    int rpos = s.rfind("ghi"); //从右往左开始查找
    cout << "the position of \"ghi\":" << pos << endl;
    cout << "the position of \"ghi\"(from right):" << rpos << endl;
    if (s.find("dada") == s.npos) //未查找到
    {
        cout << "not found!" << endl;
    }

    cout << "-------------------" << endl;
}
int main()
{
    test01();
    test02();
    test03();
    test04();
    test05();
    return 0;
}