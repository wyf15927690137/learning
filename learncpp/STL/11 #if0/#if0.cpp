#include <iostream>
using namespace std;

#if 0 //#if 0执行第二段代码，#if 1执行第一段代码
int main()
{
    cout<<"a"<<endl;
}
#else
int main()
{
    cout << "b" << endl;
}
#endif
