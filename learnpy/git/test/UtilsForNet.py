
from time import sleep
from Config import Config
import os
import subprocess

if os.name == 'nt':
    from lib import requests
else:
    from lib_linux import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from settingUI import SettingsUI, WarningUI

class JenkinsNetwork:
    def __init__(self):
        pass

    @staticmethod
    def testConnectivity():
        r = requests.get(Config.BridgeServerHost, verify=False)
        if r.status_code != 200:
            raise Exception("Target " + Config.BridgeServerHost + " is not reached!")

        return r.text

    @staticmethod
    def updateTools():
        print("End the current process and start to update!")
        updateTools = ["python.exe", "ClientUpdateTools/client.py"]
        subprocess.Popen(updateTools,shell=True)
        print("start.py is over")
        exit(0)

    @staticmethod
    def checkVersion(text):
        arr = text.split(":")
        if len(arr) <= 1:
            print("Version is not matched, automatically update the client tool!")
            if os.name == 'nt':
                JenkinsNetwork.updateTools()
            else:
                raise Exception("Version is not matched, please update your client tool!")
        if arr[1].strip() != Config.BridgeServerVersion:
            print("Version is not matched, automatically update the client tool!")
            if os.name == 'nt':
                JenkinsNetwork.updateTools()
            else:
                raise Exception("Version is not matched, please update your client tool!")
