#include <iostream>
using namespace std;
#include <fstream>

class Person
{
private:
    int mAge;
    int mId;

public:
    Person(){};
    Person(int age, int id) : mAge(age), mId(id){};
    void show()
    {
        cout << this->mAge << "   " << this->mId << endl;
    }
};
void test01()
{
    Person p1(35, 31313);
    Person p2(17, 2314977);

    string path = "H:\\学习\\代码\\STL\\16 二进制文件的读写\\file.txt";
    ofstream osm(path, ios::out | ios::binary); // write a file with binary type

    osm.write((char *)&p1, sizeof(Person));
    osm.write((char *)&p2, sizeof(Person));
    osm.close();

    ifstream ism(path, ios::in | ios::binary);
    Person p3, p4;
    ism.read((char *)&p3, sizeof(Person));
    ism.read((char *)&p4, sizeof(Person));
    p3.show();
    p4.show();

    ism.close();
}

int main()
{
    test01();
    return 0;
}