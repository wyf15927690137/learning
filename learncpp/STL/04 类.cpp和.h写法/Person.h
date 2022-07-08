#pragma once
#include <iostream>
#include <string>
using namespace std;

class Person
{
public:
	Person(string name, int age);
	void show();
public:
	string mName;
	int mAge;
};