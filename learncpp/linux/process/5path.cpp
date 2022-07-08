#include <iostream>
using namespace std;
#include <stdlib.h>

int main()
{
    cout << "the env path=" << getenv("PATH") << endl;

    char *ret = "/home/megbin";
    int res = putenv(ret);
    if (res == 0)
    {
        cout << "success" << endl;
    }
    else
    {
        cout << "failed" << endl;
    }
    return 0;
}