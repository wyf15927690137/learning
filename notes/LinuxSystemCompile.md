环境变量：

系统级：/etc/bashrc 

用户级：~./ bashrc	~./ bash_profile

env 查看所有环境变量

echo $PATH 查看path



临时修改环境变量：

export PATH=$PATH:/home/poke/	添加poke目录下的可执行文件到临时的环境变量 (在当前终端有效)

##### 针对当前用户永久修改环境变量：

vim ./.bash_profile

source ~/.bash_profile



加载顺序：

先系统级：etc/bashrc

再用户级中~/.bashrc 然后是 ~/.bash_profile