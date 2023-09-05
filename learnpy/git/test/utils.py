import sys


def printAndFlush(str_in):
    try:
        if not str_in:
            return
        print(str_in)
        sys.stdout.flush()
    except IOError:
        pass


def BuildBuildParameters(id, username, changelist, projectName, batchId, ccrNumber, release, jiraIssue):
    param = {'parameter':
        [
            {'name': 'id', 'value': id},
            {'name': 'batchid', 'value': batchId},
            {'name': 'ccr', 'value': ccrNumber},
            {'name': 'username', 'value': username},
            {'name': 'changelist', 'value': changelist},
            {'name': 'version', 'value': release},
            {'name': 'project', 'value': projectName},
            {'name': 'jira', 'value': jiraIssue}
        ]
    }

    return param


if __name__ == '__main__':
    BuildBuildParameters('id', 'a', 'b', 'powerSI', 'batch-id', '123', '2018', "NoShareLib")
