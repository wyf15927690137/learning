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

jira = JIRA(server="https://jira.cadence.com/", token_auth=( jira_token ))

try:
    comment = jira.add_comment(jiraIssue, "The changelist has been submitted!")
except Exception as err:
    print("Update jira issue comment failed!")
    exit(0)
print("Update jira issue comment successfully!")
exit(1)