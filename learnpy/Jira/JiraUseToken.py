
from jira import JIRA
import sys
import base64
import sys

passedString = "PASSED:12345"
jiraIssue = sys.argv[1]
jiraUsr = "svc_cicd"
jiraPwd =  "U2hhbmdAMTIz"
jiraPwd = base64.b64decode(jiraPwd)
jiraPwd = jiraPwd.decode('ascii')
jira_token = "MzE0NTk0OTQwMzcxOoA3ajlJ8aOOI1VcB8S47Dc+Gfcc"
api_token = "MzMzOTc3OTM4ODY3OhxRP/Hw4yA9bHEGjbm7xXIeuxUu"

jira = JIRA(server="https://jira.cadence.com/", token_auth=( jira_token ))
issue = jira.issue(jiraIssue)
comments = issue.fields.comment.comments
result = ""
try:
    result = comments[-1].body
except Exception as err:
    print("false")
    exit(0)
if passedString in result:
    print("true")
else:
    print("false")
