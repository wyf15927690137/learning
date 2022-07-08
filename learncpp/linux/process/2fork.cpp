#include <iostream>
using namespace std;
#include <unistd.h>

int main()
{
    cout << "before fork" << endl;
    // fork return the process id of son process to father process , and return 0 to son process. fork will return nagetive number when creating son process failed.
    // son process and father process shared the same code snippets
    // son process and father process shared the same code, but they have different data.
    int ret = fork();
    sleep(1);
    cout << "my ret is:" << ret << endl;
    cout << "my pid is:" << getpid() << "  my father pid is:" << getppid() << endl;
    sleep(1);
    return 0;
}