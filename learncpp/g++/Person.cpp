#include <iostream>
using namespace std;

class Person{
public:
Person(string name, int age)
{
	this->mAge = age;
	this->mName = name;
}

void show()
{
	cout << this->mName << "'s age is " << this->mAge << endl;
}
public:
int mAge;
string mName;
};
