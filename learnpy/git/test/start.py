#!/usr/bin/python

# import pdb
# pdb.set_trace()

import sys
import copy
import subprocess
import uuid
import os
import time

from settingUI import SettingsUI, WarningUI
from utilsForP4 import VerifySigrityChangeList, VerifyFidelityChangeList, CheckProduct, getSigrityJobType
from UtilsForNet import JenkinsNetwork
from Config import Config
from UtilsForCCRCheck import AllowSubmit, CheckCCRNote

print("Tool Version: ", Config.BridgeServerVersion)

ccrNumber = ""
JiraIssue = ""
branch = ""
vc_Changed = False

try:
    changelist = str(sys.argv[2]).strip()
    username = str(sys.argv[4]).lower().strip()
    p4port = str(sys.argv[6]).lower().strip()
except Exception as err:
    warnMsg = WarningUI(err, "Please reimport the regression tool (C:\\regressiontest\\regtest.xml) in p4 custom tools.")
    warnMsg.showMsg()
    exit(1)

jobtype = []
product = ""
batchId = str(uuid.uuid4())

# 1. test the version if OK
resp = ''
try:
    print("Test the connection to Jenkins server...")
    resp = JenkinsNetwork.testConnectivity()
except Exception as err:
    warnMsg = WarningUI("Network Error!", err)
    warnMsg.showMsg()
    exit(1)

try:
    print("Verify version with PreCheckIn server...")
    JenkinsNetwork.checkVersion(resp)
except Exception as err:
    warnMsg = WarningUI("Version error!", err)
    warnMsg.showMsg()
    exit(1)

try:
    print("Check product info...")
    product = CheckProduct(p4port)
except Exception as err:
    warnMsg = WarningUI("P4 port Error!", err)
    warnMsg.showMsg()
    exit(1)

# 2. test the changelist description
if product == Config.ProductSigrity:
    try:
        print("Verify the change list...")
        ccrNumber, branch, vc_Changed = VerifySigrityChangeList(changelist)
    except ValueError as err:
        warnMsg = WarningUI("ChangeList Error!", err)
        warnMsg.showMsg()
        exit(1)
    except Exception as errBase:
        warnMsg = WarningUI("ChangeList Error!", errBase)
        warnMsg.showMsg()
        exit(1)

    try:
        jobtype = getSigrityJobType(changelist)
    except Exception as err:
        errMSg = "Some error happened when get changelist job type!"
        warnMsg = WarningUI("ChangeList Error!", errMSg)
        warnMsg.showMsg()
        exit(1)

    print("Verify the change list for VC Project...")
    if vc_Changed:
        if username not in Config.vc_user_list:
            vc_err = "User " + username + " is not permitted to update VC Project file!" + " Please ask your manager for the permission!"
            print(vc_err)
            warnMsg = WarningUI("ChangeList Error!", vc_err)
            warnMsg.showMsg()
            exit(1)

    try:
        print("Verify if the CCR is allowed...")
        isAllowed = AllowSubmit(ccrNumber)
        if isAllowed:
            print("ccrNumber is allowed to submit!", ccrNumber)
        else:
            warnMsg = WarningUI("Your CCR is not allowed to submit! Because current system is broken only CCR in the WhiteList is allowed!")
            warnMsg.showMsg()
            exit(1)
    except Exception as err:
        warnMsg = WarningUI("CCR is not allowed to submit!", err)
        warnMsg.showMsg()
        exit(1)
    
    # test the CCR status to update note
    try:
        print("Verify if the CCR notes status...")
        passed = CheckCCRNote(ccrNumber, batchId)
        if passed:
            print("ccrNumber notes check passed for: ", ccrNumber)
        else:
            warnMsg = WarningUI("CCR notes check failed, quit!")
            warnMsg.showMsg()
            exit(1)
    except Exception as err:
        warnMsg = WarningUI("CCR notes check failed, ", err)
        warnMsg.showMsg()
        exit(1)
else:
    try:
        print("Verify the change list...")
        branch, JiraIssue = VerifyFidelityChangeList(changelist)
    except ValueError as err:
        warnMsg = WarningUI("ChangeList Error!", err)
        warnMsg.showMsg()
        exit(1)
    except Exception as errBase:
        warnMsg = WarningUI("ChangeList Error!", errBase)
        warnMsg.showMsg()
        exit(1)
    jobtype.append(Config.JobFidelity)

# 1st of tuple is setter flag, 2nd is the project name
varReleaseMainAllInOne = (False, "")
varReleaseIsrAllInOne = (False, "")

varFidelity = (False, "")
varCGC = (False, "")
varAllProject = (False,"")

varOnWindows = (False, "")
varOnLinux = (False, "")

# move ui construction from GetProjectSetting(), or when GetProjectSetting() quit,
# the ui will be self destroyed, cause such error:
# Traceback (most recent call last):
#   File "C:\regressiontest-master\bin\Python37\lib\tkinter\__init__.py", line 329, in __del__
#     if self._tk.getboolean(self._tk.call("info", "exists", self._name)):
# RuntimeError: main thread is not in main loop
ui = SettingsUI()
def GetProjectSetting():
    global branch
    branchVal = 1
    if branch == Config.BranchMain:
        branchVal = 1
    elif branch == Config.BranchIsr:
        branchVal = 2

    global jobtype
    allVal = 0
    cgcVal = 0
    fidelityVal = 0
    if Config.JobAll in jobtype:
        allVal = 1
    if Config.JobCGC in jobtype:
        cgcVal = 1
    if Config.JobFidelity in jobtype:
        fidelityVal = 1
    ui.setReleaseSwitchingDef(branchVal)
    ui.setALLSwitchingDef(allVal)
    ui.setCGCSwitchingDef(cgcVal)
    isCGC = False
    if cgcVal == 1:
       isCGC = True 
    ui.setFidelitySwitchingDef(fidelityVal)
    ui.showWindow(isCGC)
    if ui.isCancelled:
        return False

    if ui.releaseSwitch.get() != branchVal:
        warnBranchMsg = WarningUI("Branch Selection Error!", "ChangeList is not match the selected branch!")
        warnBranchMsg.showMsg()
        return False

    global varReleaseMainAllInOne, varReleaseIsrAllInOne
    varReleaseMainAllInOne = ui.releaseMainAllInOne.get(), Config.BranchMain
    varReleaseIsrAllInOne = ui.releaseIsrAllInOne.get(), Config.BranchIsr

    # for debugging
    # varReleaseMainAllInOne = 0, Config.BranchMainAllInOne
    # varReleaseIsrAllInOne = 1, Config.BranchIsrAllInOne

    global varOnWindows, varOnLinux
    global varCGC, varAllProject, varFidelity

    varCGC = ui.projectCGC.get(), "cgc"
    varFidelity = ui.projectFidelity.get(), "fidelity"
    varAllProject =ui.projectAllProject.get(),"allproject"

    varOnWindows = ui.onWindows.get(), "windows"
    varOnLinux = ui.onLinux.get(), "linux"

    # for debugging
    # varOnWindows = 1, "windows"
    # varOnLinux = 0, "linux"
    return True

def UpdateLinuxProjectSetting():
    global varOnWindows, varOnLinux
    global varCGC, varFidelity

    if varCGC[0]:
        return

    selectProject = 0
    for project in (varCGC, varFidelity):
        if project[0]:
            selectProject += 1

    singleRunProject = 0

    if singleRunProject == selectProject:
        return

def TriggerWindowsJob(product, args):
        global varCGC, varAllProject, varFidelity
        global varReleaseMainAllInOne, varReleaseIsrAllInOne
        global ccrNumber, JiraIssue

        if varOnWindows[0]:
            for release in (varReleaseMainAllInOne, varReleaseIsrAllInOne):
                if not release[0]:
                    continue

                for project in (varAllProject, varCGC, varFidelity):
                    if not project[0]:
                        continue

                    args.append(project[1])
                    if project[1] == varFidelity[1]:
                        args.append(varOnWindows[1] + "-" + varOnLinux[1])
                    else:
                        args.append(varOnWindows[1])
                    args.append(release[1])

                    if product == Config.ProductSigrity:
                        # start project
                        if os.name == 'nt':
                            # ['python.exe', 'startProjects.py', '2586516', '-c', '421661', '-u', 'yanfeiw', 'd280fbd0-c16e-4eda-9aeb-d909ec60af56', 'allproject', 'windows', 'main']
                            startProjParams = ["python.exe", "startProjects.py", ccrNumber]
                        else:
                            startProjParams = ["python3", "startProjects.py", ccrNumber]

                        if len(args) > 1:
                            startProjParams += args[1:]
                        if os.name == 'nt':
                            subprocess.Popen(startProjParams, creationflags=0x8, shell=True)
                        else:
                            os.system("/usr/bin/xterm -e '" + " ".join(startProjParams) + "' &")
                    else:
                        # start project
                        if os.name == 'nt':
                            startProjParams = ["python.exe", "startProjects.py", JiraIssue]
                        else:
                            startProjParams = ["python3", "startProjects.py", JiraIssue]

                        if len(args) > 1:
                            startProjParams += args[1:]
                        # ['python.exe', 'startProjects.py', 'SBH-136', '-c', '152172', '-u', 'nali', '0c528a41-37a6-4f65-9cf5-484ad70da3a3', 'fidelity', 'windows-linux', 'main']
                        if os.name == 'nt':
                            subprocess.Popen(startProjParams, creationflags=0x8, shell=True)
                        else:
                            os.system("/usr/bin/xterm -e '" + " ".join(startProjParams) + "' &")

def TriggerLinuxJob(product, args):
    global varCGC, varAllProject, varFidelity
    global varReleaseMainAllInOne, varReleaseIsrAllInOne
    global ccrNumber, JiraIssue

    for release in (varReleaseMainAllInOne, varReleaseIsrAllInOne):
        if not release[0]:
            continue

        for project in (varAllProject, varCGC, varFidelity):
            if not project[0]:
                continue

            args.append(project[1])
            args.append(varOnLinux[1])
            args.append(release[1])
             
            if product == Config.ProductSigrity:
                # start project
                if os.name == 'nt':
                    startProjParams = ["python.exe", "startProjects.py", ccrNumber]
                else:
                    startProjParams = ["python3", "startProjects.py", ccrNumber]

                if len(args) > 1:
                    startProjParams += args[1:]
                    # ['python.exe', 'startProjects.py', '2586516', '-c', '421661', '-u', 'yanfeiw', 'fd69a1ec-2540-4e81-99a7-c4f1b0f06cbc', 'allproject', 'linux', 'main']
                if os.name == 'nt':
                    subprocess.Popen(startProjParams, creationflags=0x8, shell=True)
                else:
                    os.system("/usr/bin/xterm -e '" + " " .join(startProjParams) + "' &")
            else:
                # start project
                if os.name == 'nt':
                    startProjParams = ["python.exe", "startProjects.py", JiraIssue]
                else:
                    startProjParams = ["python3", "startProjects.py", JiraIssue]

                if len(args) > 1:
                    startProjParams += args[1:]
                # ['python.exe', 'startProjects.py', 'SIG-315', '-c', '4104912', '-u', 'cc', 'a71d03bd-aec4-4324-af27-8650a4b2af05', 'fidelity', 'linux', 'main']
                if os.name == 'nt':
                    subprocess.Popen(startProjParams, creationflags=0x8, shell=True)
                else:
                    os.system("/usr/bin/xterm -e '" + " " .join(startProjParams) + "' &")

if __name__ == '__main__':
    if not GetProjectSetting():
        exit(1)
    args = copy.deepcopy(sys.argv)
    args.pop()
    args.pop()
    args.append(batchId)
    linuxArgs = copy.deepcopy(args)
    winArgs = copy.deepcopy(args)

    if product == Config.ProductSigrity:
        if varOnLinux[0]:
            TriggerLinuxJob(product, linuxArgs)
        if varOnWindows[0]:
            TriggerWindowsJob(product, winArgs)
    else:
        if varOnWindows[0]:
            TriggerWindowsJob(product, winArgs)
        else:
            TriggerLinuxJob(product, linuxArgs)


    # Handle original request for Windows Products
    # Handle group request for Linux Products
    # UpdateLinuxProjectSetting()