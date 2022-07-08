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
    // char *path = "H:\\ѧϰ\\����\\STL\\15 �ļ�����\\test1.txt";
    string path = "H:\\ѧϰ\\����\\STL\\15 �ļ�����\\test1.txt"; // use the same encoding as the file,GBK
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
    // char *path = "H:\\ѧϰ\\����\\STL\\15 �ļ�����\\test1.txt";
    string path = "../test.txt";
    // app: ���ļ�֮�󸽼�����+
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
    // char *path = "H:\\ѧϰ\\����\\STL\\15 �ļ�����\\test1.txt";
    string path = "../test.txt";
    // trunc:�����ļ�
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