#include <iostream>
using namespace std;

template <typename T>

T square(T x)
{
    return x*x;
}

int main()
{
    cout<<square(5)<<endl;
    cout<<square(5.5)<<endl;
    cout<<square<int>(87)<<endl;
    cout<<square<double>(8.4)<<endl;
    return 0;
}