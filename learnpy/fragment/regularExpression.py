import re

# desc = "#12758 FIXED STL export 89083132 423422"
desc = "#12758: FIXED STL export "
jiraIssue = re.findall("(?:(?:[A-Z]+-\d+)|(?:NOP))", desc)[0]
print(jiraIssue)
