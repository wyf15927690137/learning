#include <iostream>
#include <unistd.h>
using namespace std;

int main()
{
    while (1)
    {
        // get the processs id of son process and father process
        cout << "my pid:" << getpid() << endl;
        cout << "---------------------" << endl;
        cout << "father pid" << getppid() << endl;
        sleep(1);
    }
    return 0;
}

// check the corresponding process:

//  ps aux | grep "process id"

// nearly all the father process of command process are bash under linux
// bash create son process to complete tasks