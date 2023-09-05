#!/usr/bin/python
import sys
import json
import uuid
import time
from datetime import datetime
import os

if os.name == 'nt':
    from lib import requests
    from lib.colorama import init, Fore, Style
else:
    from lib_linux import requests
    from lib_linux.colorama import init, Fore, Style

from utils import printAndFlush, BuildBuildParameters
from Config import Config

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


import socket
socket.setdefaulttimeout(30)

init()


class JobBuildProcessor(object):
    def __init__(self):
        self.delay = 25  # waiting for delay second
        self.step = 0

        self.ccrNumber = None
        self.jiraIssue = None
        self.changelist = None
        self.username = None
        self.projectName = None
        self.platform = None
        self.release = None
        self.shareLib = None

        # this batch id is for tracing the result of a batch of build,
        # for example: trigger the psi pdc opi at the same time
        self.id = None  # build id
        self.batchId = None  # batch id

        self.inBuilding = False
        self.buildId = None
        self.retry = 0

        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'User-Agent:Mozilla/5.0'
        }

    def initInputArgv(self):
        self.step = self.step + 1
        printAndFlush("\nStep " + str(self.step) + ": Parse parameters")

        # import  pdb
        # pdb.set_trace()
        if len(sys.argv) < 10:
            printAndFlush("parameters wrong, stop the job!")
            printAndFlush("\n")
            return False
        self.projectName = str(sys.argv[7]).strip()
        if self.projectName == Config.ProductFidelity:
            self.jiraIssue = str(sys.argv[1]).strip()
            self.ccrNumber = ""
        else:
            self.ccrNumber = str(sys.argv[1]).strip()
            self.jiraIssue = ""

        self.changelist = str(sys.argv[3]).strip()
        self.username = str(sys.argv[5]).strip()
        self.batchId = str(sys.argv[6]).strip()
        self.platform = str(sys.argv[8]).strip()
        self.release = str(sys.argv[9]).strip()

        if self.projectName == Config.ProductFidelity:
            if not self.jiraIssue or not self.changelist or not self.username or not self.projectName \
                    or not self.batchId or not self.platform:
                printAndFlush("jira issue, changelist, username, batch id, platform or projectName empty, stop the job!")
                return False
            if self.ccrNumber != "":
                printAndFlush("fidelity product don't need ccr number, stop the job!")
                return False
            printAndFlush("JiraIssue is: " + self.jiraIssue)
            printAndFlush("ChangeList id is: " + self.changelist)
            printAndFlush("UserName is: " + self.username)
            printAndFlush("Project is: " + self.projectName)
            printAndFlush("Release is: " + self.release)
            return True

        else:
            if not self.changelist or not self.username or not self.projectName \
                    or not self.batchId or not self.platform or not self.ccrNumber:
                printAndFlush("changelist, username, batch id, ccr id, platform or projectName empty, stop the job!")
                return False
            if self.jiraIssue != "":
                printAndFlush("sigrity product don't need jira issue, stop the job!")
                return False

            printAndFlush("CCR id is: " + self.ccrNumber)
            printAndFlush("ChangeList id is: " + self.changelist)
            printAndFlush("UserName is: " + self.username)
            printAndFlush("Project is: " + self.projectName)
            printAndFlush("Release is: " + self.release)
            return True

    def StartNewBuild(self):
        """
        Server trigger a parameterized Jenkins build, and return the build trigger parameters
        Will use the (batch id + build id) to query the status of build
        """

        ### only for debugging
        #raise Exception("Failed to start new build!")

        self.id = str(uuid.uuid4())
        toJson = BuildBuildParameters(self.id, self.username, self.changelist, self.projectName,
                                        self.batchId, self.ccrNumber, self.release, self.jiraIssue)
        # {'parameter': [{'name': 'id', 'value': '1433cc4b-a73e-470b-b985-1b4690143544'},
        #                {'name': 'batchid', 'value': 'f1e3274e-c604-4e7b-8184-ba7a14942755'},
        #                {'name': 'ccr', 'value': ''}, {'name': 'username', 'value': 'cc'},
        #                {'name': 'changelist', 'value': '4104912'}, {'name': 'version', 'value': 'main'},
        #                {'name': 'project', 'value': 'fidelity'}, {'name': 'jira', 'value': 'SIG-315'}]}
        form = {'json': json.dumps(toJson)}
        url = Config.getBridgeServerProjectUrl(self.platform)

        response = requests.post(url, data=json.dumps(toJson), headers=self.headers, verify=False)
        if response.status_code == 200 or response.status_code == 201:
            printAndFlush("Start new build successfully!")
        else:
            raise Exception("Failed to start new build!")

        printAndFlush("Build with internal Id: " + str(self.id))
        return self.id, self.batchId

    def QueryBuildStatus(self):
        url = Config.getBridgeServerProjectUrl(self.platform)
        buildid = self.buildId if self.buildId else ''
        payload = {'id': self.id, 'batchid': self.batchId, 'project': self.projectName, 'buildid': buildid,
                   'version': self.release}

        now = datetime.now()  # current date and time
        date_time = now.strftime("%H:%M:%S") + ": "
        # print("date and time:", date_time)

        response = ''
        try:
            response = requests.get(url, params=payload, verify=False)
        except requests.RequestException as err:
            printAndFlush(date_time + 'Err in requests.get: ' + str(err))
            return False

        if response.status_code != 200:
            if self.retry > 3:
                raise Exception("Build missing!")
            else:
                self.retry += 1
                retryWithColor = Fore.YELLOW + date_time + "Retrying..."
                printAndFlush(retryWithColor)
                print(Style.RESET_ALL)
                return False

        # text including:
        # -status (queuing/building/finished)
        # -jenkins url
        # -test result
        # -passed
        #
        content = json.loads(response.text)
        if not content['status']:
            raise Exception("Server response error!")

        urlWithColor = ""
        if content['status'] == 'queuing':
            if os.name == 'nt':
                urlWithColor = Fore.WHITE + date_time + "Queuing"
            else:
                urlWithColor = Fore.BLACK + date_time + "Queuing"
            printAndFlush(urlWithColor)
            print(Style.RESET_ALL)
            response.close()
            return False

        elif content['status'] == 'building':
            if os.name == 'nt':
                urlWithColor = Fore.WHITE + date_time + "Building ..."
            else:
                urlWithColor = Fore.BLACK + date_time + "Building ..."
            printAndFlush(urlWithColor)
            if not self.inBuilding:
                self.inBuilding = True
                if content['url']:
                    if os.name == 'nt':
                        urlWithColor = Fore.WHITE + date_time + "Build url: " + content['url']
                    else:
                        urlWithColor = Fore.BLACK + date_time + "Build url: " + content['url']
                    printAndFlush(urlWithColor)
            if not self.buildId:
                if content['buildid']:
                    self.buildId = content['buildid']
            print(Style.RESET_ALL)
            response.close()
            return False

        elif content['status'] == 'finished':
            isPassed = content['passed'] if content['passed'] else 'Unknown'
            urlWithColor = date_time + "Build " + isPassed + "!"
            if isPassed == 'passed':
                urlWithColor = Fore.GREEN + urlWithColor
            elif isPassed == 'failed' or isPassed == 'aborted':
                urlWithColor = Fore.RED + urlWithColor

            printAndFlush(urlWithColor)
            if content['result']:
                if os.name == 'nt':
                    urlWithColor = Fore.WHITE + content['result']
                else:
                    urlWithColor = Fore.BLACK + content['result']
                printAndFlush(urlWithColor)

            if content['url']:
                if os.name == 'nt':
                    urlEndWithColor = Fore.CYAN + date_time + "Build url: " + content['url']
                else:
                    urlEndWithColor = Fore.BLACK + date_time + "Build url: " + content['url']
                printAndFlush(urlEndWithColor)

            print(Style.RESET_ALL)
            response.close()
            return True

    def Process(self):
        # import pdb
        # pdb.set_trace()

        if not self.initInputArgv():
            printAndFlush("Parameter error!")
            input("Press any key to Quit! ")
            exit(1)

        self.step = self.step + 1
        printAndFlush("\nStep " + str(self.step) + ": Trigger new build")

        try:
            self.StartNewBuild()
        except Exception as err:
            printAndFlush(err)
            input("Press any key to Quit! ")
            exit(1)

        try:
            while not self.QueryBuildStatus():
                time.sleep(self.delay)
                continue
        except Exception as err:
            printAndFlush(err)

        printAndFlush("\n")
        input("Press any key to Quit! ")


handler = JobBuildProcessor()
handler.Process()
