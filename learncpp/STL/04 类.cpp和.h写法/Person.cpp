#include "Person.h"

Person::Person(string name, int age)
{
	this->mAge = age;
	this->mName = name;
}

void Person::show()
{
	cout << this->mName << "'s age is " << this->mAge << endl;
}