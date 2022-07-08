#pragma once
#include <iostream>
using namespace std;

template<class T1, class T2> class Person
{
public:
	Person<T1, T2>(T1 name, T2 age);
	void show();
public:
	T1 mName;
	T2 mAge;
};
