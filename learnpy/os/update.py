import os
import shutil

def cloneCodeToTemp(gitExe, gitRepo, temp):
    try:
        os.system(f"{gitExe} clone -b Client_fidelity {gitRepo} {temp}")
    except Exception:
        print("Clone source code failed!")

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.
    
    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def moveSourceCode(temp,dest):
    files = os.listdir(temp)
    try:
        for file in files:
            temp_path = os.path.join(temp, file)
            dest_path = os.path.join(dest, file)
            if os.path.isdir(dest_path):
                shutil.rmtree(dest_path, onerror=onerror)
            elif os.path.isfile(dest_path):
                os.remove(dest_path)
            shutil.move(temp_path, dest_path)
        os.rmdir(temp) 
    except Exception:
        print("Error happened when move source code!")

dest = os.getcwd()
temp = os.path.join(dest, "temp")
gitExe = os.path.join(dest, "PortableGit", "bin", "git.exe")
gitRepo = "http://sigrity-lab.cadence.com/ztz0223/regressiontest.git"

cloneCodeToTemp(gitExe, gitRepo, temp)
moveSourceCode(temp, dest)
print("Update complete! Please restart your regression test.")
input("press Enter to continue ...")
