# C++编译相关：

g++ main.cpp -o filename

生成名为filename 的.out文件

g++ -c main.cpp

生成main.o的二进制文件（只编译不链接	）



四步：

预处理：展开宏文件	g++ -E test.cpp -o test.i

编译：检查代码规范	g++ -S test.i -o test.s

汇编：生成二进制文件（翻译）g++ -c test.s -o test.o

链接：生成可执行文件	g++ -c test.o -o out



其他：

-I 指定头文件位置

-g 添加调试语句，用于gdb调试

-Wall 显示所有警告信息

-D 向程序中”动态“注册一个宏