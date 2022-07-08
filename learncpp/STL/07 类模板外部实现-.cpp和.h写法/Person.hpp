#include <iostream>
using namespace std;
#include "Person.h"

template <class T1,class T2>
Person<T1, T2>::Person(T1 name, T2 age)
{
	this->mAge = age;
	this->mName = name;
}
template<class T1,class T2>
void Person<T1, T2>::show()
{
	cout << this->mName << "'s age is " << this->mAge << endl;
}