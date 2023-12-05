import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--jira', nargs='+', type=str, help='jira')

args = parser.parse_args()
jira_list = args.jira

if not jira_list:
    print("The jira list is empty")
else:
    print(f"jira: {jira_list}")