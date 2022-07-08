#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

void test01()
{
    int fd = open("./test02.txt", O_RDONLY);
    printf("fd=%d\n", fd);
    close(fd);
}

void test02()
{
    //文件权限相关：linux文件的基本权限有9个，依次为user, group, others
    // r:4 w:2 x:1 对应 读，写，执行
    //更改权限： chmod 777 filename
    // when the second argument O_CREAT exists,the third argument works.
    //文件权限=mode&~umask
    int fd = open("./test03.txt", O_RDONLY | O_CREAT, 0664); // 0664 means -rw-rw-r--
    printf("fd=%d\n", fd);
    close(fd);
}

void test03()
{
    int fd = open("./test03.txt", O_RDWR);
}
int main(int argc, char *argv[])
{
    test01();
    printf("----------------\n");
    test02();
    printf("----------------\n");
    return 0;
}