4、初始化git信息(在右键Git Bash输入以下命令)

(1) git config --global user.name 'itcats_cn'
(2) git config --global user.email 'itcats_cn@itcats.cn'
(3) ssh-keygen -t rsa -C 'itcats_cn@itcats.cn'   (plus:直接按Enter即可,密码可输入可不输入)
————————————————
版权声明：本文为CSDN博主「itcats_cn」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/itcats_cn/article/details/100936303



Git 操作：

进入路径---git init------ls -a(看到	.git)



暂存区：

git add filename

git add .(所有修改添加到暂存)





提交到仓库

git commit (提交所有暂存区文件)

git commit -m "提交内容说明“

ssh -T -p 443 git@ssh.github.com

git status 查看文件状态	



git diff 查看本地文件和暂存区文件的更新

git log 提交到远程仓库的历史记录

git reset <commit ID>

git reset --hard HEAD^ 回退到上个版本







git remote add origin git@github.com:wyf15927690137/cloud

git push -u origin master 

git clone https://github.com/wyf15927690137/test3   :克隆远程库test3到本地当前路径下



切换远程库：

git remote rm origin
git remote add origin git@[github](https://so.csdn.net/so/search?q=github&spm=1001.2101.3001.7020).com:wyf15927690137/cloud1



# git init之后的流程：

git clone  https://github.com/wyf15927690137/test3

做出修改

git add -A

git commit -m "wyf"

git push origin master





分支：

git branch -v

git branch branch01

git checkout branch01

git branch -D branch01

git checkout master

git merge branch01

```
submit a merge request:
git branch branchname
git checkout branchname
git add / commit -m/ push
create merge request in gitlab
```



git更新单个文件：

git fetch 

git checkout origin/master filename

my_list = [(1, 2), (3, 1), (4, 0), (11, 4)]
my_list.sort(key=lambda x: x[1])
print(my_list)

```
git config --global http.sslverify "false"
```

get latest code and overwrite local

```
git fetch --all
git reset --hard origin/master
git pull
```

git withdraw commited file (not pushed):

```
git reset --soft HEAD^
```
