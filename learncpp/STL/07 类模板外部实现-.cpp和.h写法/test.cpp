#include "Person.hpp"
//函数模板需要进行二次编译，必须要有定义类模板的文件，先生成具体的类
//hpp，其实质就是将.cpp的实现代码混入.h头文件当中，定义与实现都包含在同一文件
int main()
{
	Person<string, int> p1("zhang", 12);
	p1.show();
	return 0;
}