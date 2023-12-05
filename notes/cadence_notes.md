use product through VNC

```shell
setenv CDS_LIC_FILE 5280@sjflex4
```

config rbt post

```
rbt status --p4-port ssl:p4shanghai:2644 --p4-client PC-DT-YANFEIW --username yanfeiw --password
```

# Windows Installer:

## some path:

```sh
# newest image
\\shwinshare\wint$\cdrom\23.10RTM\Cd-202305180418\Cd-202305180418
# installer packages and documents
\\shwinshare\winshare\CICD\Tools\Installer
```

yanfei jira token

```
MzMzOTc3OTM4ODY3OhxRP/Hw4yA9bHEGjbm7xXIeuxUu
```

fidelity jira token

```
# user is svc_cicd (nali)
MzE0NTk0OTQwMzcxOoA3ajlJ8aOOI1VcB8S47Dc+Gfcc
```



Run clarity3dlayout:

```
Test env: set CLARITY_C2_BACKUP=1
C:\Users\yanfeiw>set CDS_LIC_FILE=5280@sjflex1
set QTDIR=D:\CMBuild\23.10.0917.454196\Internal\tools\Qt\v5\64bit
set QTPREFIX=cds
set QTROOT=D:\CMBuild\23.10.0917.454196\Internal\tools\Qt\v5\64bit
C:\Users\yanfeiw>J:\23.10main\23.10.0917.454196\tools\bin\Clarity3DLayout.exe

select clariy 3d cloud - > close
simulation -> set up computer resources

Properties->Debugging->
CDS_LIC_FILE=5280@sjflex1
CLARITY_C2_BACKUP=1
```
