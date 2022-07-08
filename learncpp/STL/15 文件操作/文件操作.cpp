#include <iostream>
using namespace std;
#include <fstream>

void test01()
{
    string s = "H:\\学习\\代码\\STL\\15 文件操作\\source.txt";
    // ifstream ism(filename,ios::in);//只读方式打开文件
    ifstream ism;
    ism.open(s, ios::in);

    // write file
    char *ta = "H:\\学习\\代码\\STL\\15 文件操作\\target.txt";
    ofstream osm(ta, ios::out | ios::app); // append behind the file when write
    if (!ism)
    {
        cout << "failed to open file .." << endl;
        return;
    }

    char ch;
    while (ism.get(ch)) //读文件
    {
        cout << ch;
        osm.put(ch);
    }

    ism.close();
    osm.close();
}

int main()
{
    test01();
    return 0;
}
