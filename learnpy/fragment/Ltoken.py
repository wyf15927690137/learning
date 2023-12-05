# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.
from __future__ import annotations

import re

from jira.client import JIRA

# By default, the client will connect to a Jira instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
api_token = "MzE0NTk0OTQwMzcxOoA3ajlJ8aOOI1VcB8S47Dc+Gfcc"
# jira = JIRA(server="https://jira.cadence.com/", basic_auth=('svc_cicd','Shang@123'))
jira = JIRA(server="https://jira.cadence.com/", basic_auth=('svc_cicd',api_token))

# Get all projects viewable by anonymous users.
projects = jira.projects()

# Sort available project keys, then return the second, third, and fourth keys.
keys = sorted(project.key for project in projects)[2:5]
# https://jira.cadence.com/projects/SBH/issues/SBH-45?filter=allopenissues
# Get an issue.
issue = jira.issue("SBH-136")
# Find all comments made by Atlassians on this issue.
atl_comments = [
    comment
    for comment in issue.fields.comment.comments
    if re.search(r"@atlassian.com$", comment.author.key)
]

# Add a comment to the issue.
jira.add_comment(issue, "Fidelity regression passed!")

# # Change the issue's summary and description.
# issue.update(
#     summary="Use python Api!", description="Use python jira Api."
# )

# # # Change the issue without sending updates
# # issue.update(notify=False, description="Quiet summary update.")

# # You can update the entire labels field like this
# issue.update(fields={"labels": ["AAA", "BBB"]})

# # Or modify the List of existing labels. The new label is unicode with no
# # spaces
# issue.fields.labels.append("new_text")
# issue.update(fields={"labels": issue.fields.labels})

# Send the issue away for good.
# issue.delete()

# # Linking a remote jira issue (needs applinks to be configured to work)
# issue = jira.issue("JRA-1330")
# issue2 = jira.issue("XX-23")  # could also be another instance
# jira.add_remote_link(issue.id, issue2)