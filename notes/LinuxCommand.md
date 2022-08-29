mv -v dir1 dir2 /path/to/dest/ 

cp /home/usr/dir/{file1,file2,file3,file4} /home/usr/destination/





command1 | command2

Linux所提供的管道符“|”将两个命令隔开，管道符左边命令的输出就会作为管道符右边命令的输入。

command1 ; command2

用;号隔开每个命令, 每个命令按照从左到右的顺序,顺序执行， 彼此之间不关心是否失败， 所有命令都会执行。

cat /etc/passwd | grep /bin/bash | wc -l

命令使用了两个管道，利用第一个管道将cat命令(显示passwd文件的内容)的输出送给grep命令，grep命令找出含有“/bin /bash”的所有行；第二个管道将grep的输出送给wc命令，wc命令统计出输入中的行数。这个命令的功能在于找出系统中有多少个用户使用bash

command1 &

默认情况下，进程是前台进程，这时就把Shell给占据了，我们无法进行其他操作，对于那些没有交互的进程，很多时候，我们希望将其在后台启动，可以在启动参数的时候加一个'&'实现这个目的

command1 && command2 [&& command3 ...]

命令之间使用 && 连接，实现逻辑与的功能。

只有在 && 左边的命令返回真(命令返回值 $? == 0)，&& 右边的命令才会被执行。

只要有一个命令返回假(命令返回值 $? == 1)，后面的命令就不会被执行
command1 && command2 [&& command3 ...]

命令之间使用 && 连接，实现逻辑与的功能。

只有在 && 左边的命令返回真(命令返回值 $? == 0)，&& 右边的命令才会被执行。

只要有一个命令返回假(命令返回值 $? == 1)，后面的命令就不会被执行。
command1 || command2 [|| command3 ...

命令之间使用 || 连接，实现逻辑或的功能。

只有在 || 左边的命令返回假(命令返回值 $? == 1)，|| 右边的命令才会被执行。这和 c 语言中的逻辑或语法功能相同，即实现短路逻辑或操作。

只要有一个命令返回真(命令返回值 $? == 0)，后面的命令就不会被执行。 –直到返回真的地方停止执行
————————————————



# screen:



screen -S test	//create a screen named test

screen -ls	//view all the screen

exit	//delete the current screen

ctrl+a+d	//put the current screen background

screen -r {pid}	//step into  a screen

screen -x {pid}   //step into a screen in multiplay



# 软链接和硬链接：



ll -rt *.so	-list by time

ll *.so	-list by name

edit the setenv.csh file

source setenv.csh	then the env will works

clean empty folder

```
find . -type d -empty -deletes
```

find a folder

```
find . -name "lnx86_output" | xargs rm -rf {}
```

```
grep -r "redeem reward" /home/tom/
```

