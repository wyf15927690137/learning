import os

if os.name == 'nt':
    from lib import P4
    from lib.P4 import P4, P4Exception
else:
    from lib_linux import P4
    from lib_linux.P4 import P4, P4Exception

import re
from Config import Config

import base64
import socket

class P4Conn:
    def __init__(self, p4usr, p4usrpwd, p4port):
        self.p4 = P4()
        self.p4.client = "www"
        self.p4.user = p4usr
        ccPwd = base64.b64decode(p4usrpwd)
        ccPwd = ccPwd.decode('ascii')
        self.p4.password = ccPwd
        self.p4.port = p4port
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))

        my_ip = s.getsockname()[0]
        #my_ip = socket.gethostbyname("sjf-cpgmsa19")

        print("Ip for my machine is:", my_ip)
     
        if not my_ip.startswith("10.13") and p4port == Config.SigritySHP4:
            print("SanJose")
            self.p4.port = Config.SigrityUSP4
        s.close()

    def con(self):
        try:
            self.p4.connect()
            self.p4.exception_level = 1
            self.p4.run_login()
        except P4Exception:
            for e in self.p4.errors:
                print(e)
        finally:
            pass

    def disCon(self):
        self.p4.disconnect()

    def getCcmNumber(self, changelist):
        spec = self.p4.run("describe", str(changelist))
        if not spec or len(spec) < 1:
            return None

        spec = spec[0]
        desc = spec['desc']
        if not desc:
            return None
        numbers = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*?\d*(?:[eE][-+]?\d+)?", desc)
        ccr = None
        for num in numbers:
            if len(num) >= 7:
                for index, char in enumerate(num):
                    if char == '0':
                        continue
                    else:
                        ccr = num[index:]
                        if len(ccr) == 7:
                            break

                if ccr:
                    break

        print("CCMPR number is: " + str(ccr))
        return ccr

    def getJiraIssue(self, changelist):
        spec = self.p4.run("describe", str(changelist))
        if not spec or len(spec) < 1:
            return None

        spec = spec[0]
        desc = spec['desc']
        if not desc:
            return None
        jiraIssue = ""
        if ":" not in desc:
            return jiraIssue
        for s in desc:
            if s != ":":
                jiraIssue += s
            else:
                break

        print("Jira Issue is: " + str(jiraIssue))
        return jiraIssue

    def checkCcmShelveContent(self, changelist):
        # get Pending
        spec = self.p4.run("describe", "-s", str(changelist))
        if not spec or len(spec) < 1:
            return False, False

        if not 'depotFile' in spec[0].keys():
            return False, False

        descPending = spec[0]['depotFile']
        if not len(descPending):
            return False, False
        # get shelved files
        spec = self.p4.run("describe", "-sS", str(changelist))
        if not spec or len(spec) < 1:
            return False, False

        if not 'depotFile' in spec[0].keys():
            return False, False
        descShelve = spec[0]['depotFile']
        if not len(descShelve):
            return False, False

        result = (sorted(descShelve) == sorted(descPending))
        print("Shelve Equal to Pending: " + str(result))

        isVCProjUpdated = False
        for file in descShelve:
            if str(file).endswith('.vcxproj'):
                isVCProjUpdated = True
                break

        return result, isVCProjUpdated

    def checkChangeVCPro(self, changelist):
        # get shelved files
        spec = self.p4.run("describe", "-sS", str(changelist))
        if not spec or len(spec) < 1:
            return False

        if not 'depotFile' in spec[0].keys():
            return False
        descShelve = spec[0]['depotFile']
        if not len(descShelve):
            return False

        isVCProjUpdated = False
        for file in descShelve:
            if str(file).endswith('.vcxproj'):
                isVCProjUpdated = True
                break
        return  isVCProjUpdated

    # check the change list if correctly shelved
    def checkChangeShelve(self, changelist):
        # get Pending
        spec = self.p4.run("describe", "-s", str(changelist))
        if not spec or len(spec) < 1:
            return False

        if not 'depotFile' in spec[0].keys():
            return False

        descPending = spec[0]['depotFile']
        if not len(descPending):
            return False
        # get shelved files
        spec = self.p4.run("describe", "-sS", str(changelist))
        if not spec or len(spec) < 1:
            return False

        if not 'depotFile' in spec[0].keys():
            return False
        descShelve = spec[0]['depotFile']
        if not len(descShelve):
            return False

        result = (sorted(descShelve) == sorted(descPending))
        print("Shelve Equal to Pending: " + str(result))
        return result

    def checkSigrityBranch(self, changelist):
        # get shelved files
        spec = self.p4.run("describe", "-sS", str(changelist))
        if not spec or len(spec) < 1:
            return None

        if not 'depotFile' in spec[0].keys():
            return None
        descShelve = spec[0]['depotFile']
        if not len(descShelve):
            return None

        branch = ""
        for s in descShelve:
            if Config.TagMainSigrity[0] in s and Config.TagMainSigrity[1] not in branch:
                branch += Config.TagMainSigrity[1]
            if Config.TagIsrSigrity[0] in s and Config.TagIsrSigrity[1] not in branch:
                branch += Config.TagIsrSigrity[1]
        return branch


    def checkFidelityBranch(self, changelist):
        # get shelved files
        spec = self.p4.run("describe", "-sS", str(changelist))
        if not spec or len(spec) < 1:
            return None

        if not 'depotFile' in spec[0].keys():
            return None
        descShelve = spec[0]['depotFile']
        if not len(descShelve):
            return None

        branch = ""
        for s in descShelve:
            if Config.TagMainFidelity[0] in s and Config.TagMainFidelity[1] not in branch:
                branch += Config.TagMainFidelity[1]
            if Config.TagIsrFidelity[0] in s and Config.TagIsrFidelity[1] not in branch:
                branch += Config.TagIsrFidelity[1]
        return branch

    def getSigrityJobType(self, changelist):
        spec = self.p4.run("describe", "-sS", str(changelist))
        depotFile = spec[0]['depotFile']
        jobtype = []
        for s in depotFile:
            judgeCGC_main = ( Config.TagMainSigrity[0] + "Projects/CADKernel/" in s) or (Config.TagMainSigrity[0] + "Programs/Library/CADKernel/" in s) or \
                  (Config.TagMainSigrity[0] + "Share/INTSCT/" in s) or (Config.TagMainSigrity[0] + "Share/cgk/" in s)
            judgeCGC_ISR = (Config.TagIsrSigrity[0] + "Projects/CADKernel/" in s) or (Config.TagIsrSigrity[0] + "Programs/Library/CADKernel/" in s) or \
                  (Config.TagIsrSigrity[0] + "Share/INTSCT/" in s) or (Config.TagIsrSigrity[0] + "Share/cgk/" in s)
            if judgeCGC_main and Config.JobCGC not in jobtype:
                jobtype.append(Config.JobCGC)
            if judgeCGC_ISR and Config.JobCGC not in jobtype:
                jobtype.append(Config.JobCGC)                
            if (not judgeCGC_main) and (not judgeCGC_ISR):
                jobtype.append(Config.JobAll)
        return jobtype

def CheckProduct(p4port):
    product = ""
    if p4port == Config.SigritySHP4 or p4port == Config.SigrityUSP4:
        product = Config.ProductSigrity
    elif p4port == Config.FidelityP4:
        product = Config.ProductFidelity
    else:
        raise ValueError("Cant't recognize your p4 port.")
    return product

def VerifyFidelityChangeList(changelist):
    con = P4Conn(Config.FidelityP4Usr, Config.FidelityP4UsrPwd, Config.FidelityP4)
    con.con()
    shelve = con.checkChangeShelve(changelist)
    branch = con.checkFidelityBranch(changelist)
    jiraIssue = con.getJiraIssue(changelist)

    con.disCon()

    if not shelve:
        raise ValueError("Empty ChangeList or Shelved content is not same with pending content.")

    if not branch:
        raise ValueError("Can't deduce the branch info.")
    
    if jiraIssue == "":
        raise ValueError("Can't get the JiraIssue,changelist description must be:\n  JiraIssue:YourCustomDescription")

    if Config.TagIsrFidelity[1] in branch and Config.TagMainFidelity[1] in branch:
        raise ValueError("You can't shelve two branches files at the same time!")

    return str(branch), str(jiraIssue)

def VerifySigrityChangeList(changelist):
    con = P4Conn(Config.SigrityP4Usr, Config.SigrityP4UsrPwd, Config.SigritySHP4)
    con.con()
    # shelve, vc_changed = con.checkCcmShelveContent(changelist)
    shelve = con.checkChangeShelve(changelist)
    branch = con.checkSigrityBranch(changelist)
    ccr = con.getCcmNumber(changelist)
    vc_changed = con.checkChangeVCPro(changelist)

    con.disCon()

    if not shelve:
        raise ValueError("Empty ChangeList or Shelved content is not same with pending content.")

    if not branch:
        raise ValueError("Can't deduce the branch info.")

    if not ccr:
        raise ValueError("No valid CCMPR number set in the changlist description.")

    if Config.TagIsrSigrity[1] in branch and Config.TagMainSigrity[1] in branch:
        raise ValueError("You can't shelve main branch and isr branch files at the same time!")

    return str(ccr), str(branch), vc_changed

def getSigrityJobType(changelist):
    con = P4Conn(Config.SigrityP4Usr, Config.SigrityP4UsrPwd, Config.SigritySHP4)
    con.con()
    jobtype = con.getSigrityJobType(changelist)
    con.disCon()

    return jobtype

if __name__ == "__main__":
    con = P4Conn(Config.SigrityP4Usr, Config.SigrityP4UsrPwd, Config.SigritySHP4)
    con.con()
    con.checkCcmShelveContent("143275")
    con.checkSigrityBranch("143275")
    con.checkSigrityBranch("154051")
    con.getCcmNumber("143195")
    con.disCon()
