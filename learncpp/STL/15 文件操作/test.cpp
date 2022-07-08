#include <iostream>
using namespace std;
#include <fstream>

void test01()
{
    ofstream osm;
    string path = "./test.txt"; // both relative path and absolute path are ok
    osm.open(path, ios::out | ios::app);
    if (!osm)
    {
        cout << "failed!" << endl;
    }
    char ch = '2';
    osm.put(ch);
    osm.close();
}

void test02()
{
    ofstream osm;
    // char *path = "H:\\学习\\代码\\STL\\15 文件操作\\test1.txt";
    string path = "H:\\学习\\代码\\STL\\15 文件操作\\test1.txt"; // use the same encoding as the file,GBK
    osm.open(path, ios::out | ios::app);
    if (!osm)
    {
        cout << "failed!" << endl;
    }
    char ch = '2';
    osm.put(ch);
    osm.close();
}

void test03()
{
    ofstream osm;
    // char *path = "H:\\学习\\代码\\STL\\15 文件操作\\test1.txt";
    string path = "../test.txt";
    // app: 在文件之后附加内容+
    osm.open(path, ios::out | ios::app);
    if (!osm)
    {
        cout << "failed!" << endl;
    }
    char ch = '2';
    osm.put(ch);
    int n = 10;
    while (n--)
    {
        osm.put('3');
    }

    osm.close();
}

void test04()
{
    ofstream osm;
    // char *path = "H:\\学习\\代码\\STL\\15 文件操作\\test1.txt";
    string path = "../test.txt";
    // trunc:清零文件
    osm.open(path, ios::out | ios::trunc);
    if (!osm)
    {
        cout << "failed!" << endl;
    }
    char ch = '5';
    osm.put(ch);
    int n = 10;
    while (n--)
    {
        osm.put('6');
    }

    osm.close();
}
int main()
{
    test01();
    test02();
    test03();
    test04();
    return 0;
}