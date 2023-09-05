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

code my ~/.cshrc

```csh
setenv CDS_LIC_FILE "5280@shcaps1"
setenv CMROOT "/cds/22.10/main/latest"
setenv PATH   "/data/users/yanfei/Files/tools/git-2.24.1:/data/users/yanfei/Files/RegressionBridgeServer/mongodb_rhel70_bin/bin:/data/users/yanfei/Files/Python3/Python-3.7.9:/data/users/yanfei/Files/nodejs/node-v17.2.0-linux-x64/bin:/data/users/yanfei/Files/go/go-admin:/usr/local/go/bin:/home/yanfeiw/.vscode-server/bin/97dec172d3256f8ca4bfb2143f3f76b503ca0534/bin/remote-cli/code:/data/users/yanfei/Files/LearnDocker/noVNC/utils:/grid/common/pkgs/perforce/v2020.1/bin:/grid/common/pkgs/gcc/v9.3.0p4/bin:/grid/common/pkgs/make/v4.2/bin:/grid/common/pkgs/gdb/v8.1/bin:${CMROOT}/tools/bin:/usr/local/bin:/usr/sbin/:/home/yanfeiw/.local/bin:$PATH"
setenv QTDIR  "${CMROOT}/Internal/tools.lnx86/Qt/v5/64bit"

setenv LD_LIBRARY_PATH "/grid/common/pkgs/gcc/v9.3.0p4/lib64:/lib64:${CMROOT}/tools/bin:${CMROOT}/tools/lib/64bit:${CMROOT}/tools/Qt/v5/64bit/lib:${CMROOT}/share/oa/lib/linux_rhel60_64/opt"
setenv SPB "${CMROOT}/Internal"
setenv WORKSPACE "/data/users/yanfei/yanfeiw_shsirdlnx2"
setenv P4PORT ssl:p4shanghai:2644
setenv P4CLIENT yanfeiw_shsirdlnx2

```

source ~/.cshrc