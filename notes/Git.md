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





branch：

local branch:

```sh
git branch branch01
git checkout branch01
git checkout -b branch01
git branch -d branch01
```

remote branch

```sh
git checkout -b local_branch
git ad .
git cm -m "init remote_branch"
git push origin remote_branch
git push origin --delete remote_branch

# view the connection betweent local and remote branch
git branch -vv
git branch --set-upstream-to=origin/remote_branch  local_branch
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
git reset --hard origin/master
git pull
```

git withdraw commited file (not pushed):

```
git reset --soft HEAD^
```

git overwrite local changes

```
git fetch --all
git reset --hard origin/master
```

git delete local ad and commit

```
git reset HEAD^
```

bash file returns unexpected token `$'do\r''

```
git config --global core.autocrlf false
dos2Unix ExtendTimeOut.sh
```



create a remote repo

```
git init
git remote add testgit git@github.com:wyf15927690137/testgit.git
git push --set-upstream testgit master
```

```
git reset --hard commit_id 
```

git merge:

```sh
# merge YanfeiTest branch into master branch
git checkout master
# start merge local
git merge origin/YanfeiTest
# push to remote
git push
# clone specify the target location
git clone git@github.com:wyf15927690137/testgit.git /data/user/yanfei

# diff two branch
git diff mainYanfeiTest..master


# create a branch from a previous commit on an existing branch
git branch <branch_name> <commit_id>
# create <branch2> from <branch1>
git checkout -b <branch2> <branch1>

# diff two file of two different commit
git diff <revision_1>:<file_1> <revision_2>:<file_2>
```

git clean

```
git clean -d -f 
```

git stash

```
git st
git stash
git pull
git stash show
git stash apply (resolve conflicts)
```

git clean

```
# see which files will be deleted
git clean -n

# remove files and directory
git clean -df
```

diff two commit

```
git diff commit1 commit2			
```

```
git remote remove origin
git remote add origin http://sigrity-lab.cadence.com/fidelity/containerbuilder.git
git pull
git remote -v
```

git set multi remote

```
git remote -vv

# create a git repo at github.cadence.com
git remote add cadence git@github.cadence.com:yanfeiw/Precheckin.git
git remote -v
git push -u cadence master
```

git deal with large file

```
git lfs install
git lfs track "*.psd"
git add .gitattributes


git add file.psd
git commit -m "Add design file"
git push origin main
```

git http resource set no password auth:

```
git config --global credential.helper store
git pull (with username and passwd for the first time)
```

```
https://www.aleksandrhovhannisyan.com/blog/crlf-vs-lf-normalizing-line-endings-in-git/

 

Setting	        		Repo (check-in)			Working Tree (checkout)
core.autocrlf=true			LF						CRLF
core.autocrlf=input			LF						original (usually LF, or CRLF if you're viewing a file you created on Windows)
```

