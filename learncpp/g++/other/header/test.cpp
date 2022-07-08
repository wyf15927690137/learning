#include <iostream>
using namespace std;
#include "Person.cpp"
//g++ -I path: specify the location of header file:
//g++ -g :adding debugging information

void test01()
{
    cout<<"hanbao"<<endl;
}


int main()
{
	Person p1("zhang", 24);
	p1.show();
	cout<<"test"<<endl;
    #ifdef HANBAO
    test01();
    #endif
	return 0;
}

