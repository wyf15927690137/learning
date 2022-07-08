#include <iostream>
#include <unistd.h>
using namespace std;

int main()
{
    int ret = fork();
    if (ret > 0)
    {
        cout << "this is father process,and ID is: " << getppid() << ",and ppid is: " << getppid() << endl;
    }
    else if (ret == 0)
    {
        sleep(1);
        cout << "this is son process,and ID is: " << getpid() << ",and ppid is: " << getppid() << endl;
    }
    for (int i = 0; i < 3; i++)
    {
        // the ppid of son process has become 1
        cout << "this is :" << i << ",and the ID is" << getpid() << " and ppid is: " << getppid() << endl;
    }
    // the father process has ended but the son process is still running.
    // the orphan process will adopted by 1 process.
    return 0;
}