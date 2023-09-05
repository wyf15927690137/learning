import git
import os
import shutil
  
# Clone a remote repository
repo_url = "http://yanfeiw:7snuDTTcFWxnRBXrpzDA@sigrity-lab.cadence.com/ztz0223/regressiontest.git"
local_path = os.getcwd() + "/.git"
root = os.getcwd()
# the os.path.exists(path) method that returns True if the path is a file, directory, or a symlink to a file.
if os.path.exists(local_path):
    print("git folder")
    repo = git.Repo(root)
    print(repo)
else:
    print("no git log")
    # if os.path.exists(root):
    #     shutil.rmtree(root)
    # print(root)
    # os.mkdir(root)
    repo = git.Repo.init(root)
    repo = git.Repo.clone_from(repo_url, root)
    print(f'Repository Cloned at location: {root}')


# check if local has dirty data
if repo.is_dirty():
    print("dirty")
else:
    print("not dirty")
repo.git.pull()
repo.git.clean("-dxf")
repo.git.reset('--hard')