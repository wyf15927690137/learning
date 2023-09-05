from P4 import P4, P4Exception
from jira import JIRA
import base64

class Config:
    p4user = "cc"
    p4pwd = "QzJkZW5jZUAyMDIx"
    jusr = "svc_cicd"
    jtoken = "MzE0NTk0OTQwMzcxOoA3ajlJ8aOOI1VcB8S47Dc+Gfcc"

    def __init(self):
        pass

class P4Conn:
    def __init__(self, p4user, p4pwd, p4port):
        self.p4 = P4()
        self.p4.client = "www"
        self.p4.user = p4user
        p4pwd = base64.b64decode(p4pwd).decode('ascii')
        self.p4.password = p4pwd
        self.p4.port = p4port
    
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

    def getJiraIssue(self, changelist):
        spec = self.p4.run("describe", str(changelist))
        if not spec or len(spec) < 1:
            return None

        spec = spec[0]
        desc = spec['desc']
        if not desc:
            return None
        if ":" not in desc:
            return None
        jiraIssue = ""
        for s in desc:
            if s != ":":
                jiraIssue += s
            else:
                break
        return jiraIssue

class JiraTool:
    def __init__(self, jusr, jtoken):
        self.jusr = jusr
        self.jtoken = jtoken
        self.jira_conn = JIRA(server="https://jira.cadence.com/", token_auth=(jtoken))

    def checkJiraValidation(self, jissue):
        passedString = "PASSED:12345"
        result = ""
        try:
            issue = self.jira_conn.issue(jissue)
            comments = self.jira_conn.comments(issue)
            result = comments[-1].body
        except Exception as err:
            print("false")
            exit(1)
        if passedString in result:
            print("true")
            exit(0)
        else:
            print("false")
            exit(1)
    
    def updateJiraIssueComment(self, jissue, changelist):
        try:
            comment = self.jira_conn.add_comment(jissue, f"The changelist {changelist} has been submitted!")
        except Exception as err:
            print("Update jira issue comment failed!")
            exit(1)
        print("Update jira issue comment successfully!")
        exit(0)
