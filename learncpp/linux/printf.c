#include <stdio.h>

int main(int argc, char *argv[])
{
    //  \n: begin a new line
    printf("abc\n");
    //  \r: back to the beginning pf this line
    printf("abcxyzfgh\r");
    printf("de\n");
    printf("de\n");
    int x = 10;
    printf("print a int type:x=%d\n", x);
    return 0;
}
