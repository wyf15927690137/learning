from jenkinsapi.jenkins import Jenkins
import json
import requests

def startNewBuild():
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        #auth = (JenkinsInstance.usernameJenkins, JenkinsInstance.passwordJenkins) no use password any more, use apiToken
        auth = ("admin", "113f4b569d2a7161eb3d9bde75111d4c02")
        # when trigger new build, parameter can be less than the build parameter, but can not be more than the build parameter.
        toJson = {'parameter':
                 [
                    #  {'name': 'id', 'value': "6270014f-6c97-4bd7-aaf7-22b28410c4cb"},
                    #  {'name': 'batchid', 'value': "edf39829-8fdd-49cb-9571-5288aadddd91"},
                     {'name': 'username', 'value': "yanfeiw"},
                     {'name': 'changelist', 'value': "389350"},
                    #  {'name': 'version', 'value': "main_in_one"},
                    #  {'name': 'projectName', 'value': "ALLPROJECT"},
                     {'name': 'platform', 'value': "linux"}
                 ]
        }
        form = {'json': json.dumps(toJson)}
        response = requests.post("http://si-rdtest1:9090/job/CheckBuild/job/PreCheck_main/build?token=8fbe0598-c71c-42f8-b396-dd48091f6fe7", data=form, auth=auth, headers=headers)
        if response.status_code == 200 or response.status_code == 201:
            print("Start new build successfully!")
        else:
            raise Exception("Failed to start new build!")


startNewBuild()