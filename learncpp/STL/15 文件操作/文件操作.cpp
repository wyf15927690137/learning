#include <iostream>
using namespace std;
#include <fstream>

void test01()
{
    string s = "H:\\ѧϰ\\����\\STL\\15 �ļ�����\\source.txt";
    // ifstream ism(filename,ios::in);//ֻ����ʽ���ļ�
    ifstream ism;
    ism.open(s, ios::in);

    // write file
    char *ta = "H:\\ѧϰ\\����\\STL\\15 �ļ�����\\target.txt";
    ofstream osm(ta, ios::out | ios::app); // append behind the file when write
    if (!ism)
    {
        cout << "failed to open file .." << endl;
        return;
    }

    char ch;
    while (ism.get(ch)) //���ļ�
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
