// several status of a process:
//  r: running status
//  s: sleeping,can be interrupted
//  T: pause status
//  X:dead
//  Z:zombie
#include <iostream>
using namespace std;
#include <unistd.h>
#include <errno.h>

int main()
{
    int ret = fork();

    if (ret == 0) // here,son process will execute
    {
        cout << "this is son process,and ID is: " << getpid() << ",and ppid is: " << getppid() << endl;
    }
    else if (ret < 0)
    {
        return 0;
    }
    else
    {
        // when son process returned, father process won't terminate and reclaim the resources of son process, a zombie process emerged.
        while (1) // father process will execute
        {
            // ps aux | grep megbin : view and target the zombie process.
            cout << "this is father process,and ID is: " << getppid() << ",and ppid is: " << getppid() << endl;
            sleep(1);
        }
    }
    return 0;
}