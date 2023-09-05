import git
import os
from git import Repo

# File: RunGitAutoUpdate_forBlog.py
# Author: HowardXue https://howiexue.blog.csdn.net/

WORK_PATH = r'C:\Work\xxxx\\'

# Merge branch name, FROM_BRANCH -> TO_BRANCH
FROM_BRANCH = 'xxxx'
TO_BRANCH = 'xxxx'
# Repo name
REPO_NAME = "xxxx"


def autoMerge(workpath, repo_name, fromBranch, toBranch):
    if(os.path.isdir(workpath) == False):
        print("Error: Folder not exist, tool exit: " + workpath)
        exit()

    # get repo path
    repo_path = workpath + repo_name
    print('repopath:' + repo_path)
    repo = Repo(repo_path)
    print(repo)

    # check if local has dirty data
    if repo.is_dirty():
        print('{0}:  There is dirty data in your local git, please commit or clean it'.format(repo_name))
        exit()

    print('>>> start merge ' + repo_name + ' branch ' + fromBranch + ' -> ' + toBranch)
    # do branch merge
    branch_merge(repo, FROM_BRANCH, TO_BRANCH)
    print('end  merge <<< ' + repo_name + '\n')

    git = repo.git
    remoteVer = git.rev_parse("@{u}")
    print("Remote Current Rev Parse:" + remoteVer)


def branch_merge(repo, from_branch, to_branch):
    git = repo.git
    # Check out origin branch
    print('git checkout origin ' + from_branch)
    git.checkout(from_branch)
    git.pull('--progress', '--no-rebase', 'origin', from_branch)

    # switch to target branch, pull latest commit
    print('git checkout target ' + to_branch)
    git.checkout(to_branch)
    git.pull('--progress', '--no-rebase', 'origin', to_branch)

    # merge branch
    print('git merge ' + from_branch)
    git.merge(from_branch)

    # push merged branch to remote
    print('git push ' + to_branch)
    git.push('--progress', 'origin', to_branch)



def main():
    print('Auto Git Merge Tool... \n')
    autoMerge(WORK_PATH, REPO_NAME, FROM_BRANCH, TO_BRANCH)


if __name__ == '__main__':
    main()

