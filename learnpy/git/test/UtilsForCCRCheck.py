import time
import os

from Config import Config
if os.name == 'nt':
    from lib import requests
else:
    from lib_linux import requests

import json
import urllib3
from threading import Timer
from utils import printAndFlush

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def AllowSubmit(ccrNumber):
    response = requests.get(Config.BridgeServerCheckAllowSubmit, params={'ccrNumber':ccrNumber}, verify=False)
    if response.status_code != 200:
        raise Exception("Target " + Config.BridgeServerCheckAllowSubmit + " is not reached!")
        return False
    else:
        if response.text == 'true': # check the result
            # retrieve the data
            printAndFlush('CCR ' + str(ccrNumber) + ' is allowed to submit!')
            return True
        else:
            raise Exception('CCR ' + str(ccrNumber) + ' is blocked out cause current system is broken only CCR in WhiteList is allowed to submit!')
            return False

def TryUpdateCCRNote(ccrNumber, batchId):
    response = requests.post(Config.BridgeServerCheckCCRNote, params={'ccrNumber':ccrNumber, 'batchId': batchId}, verify=False)
    if response.status_code != 200:
        raise Exception("Target " + Config.BridgeServerCheckCCRNote + " is not reached!")
    else:
        return True

def QueryUpdateCCRNoteStatus(ccrNumber, batchId):
    response = requests.get(Config.BridgeServerCheckCCRNote, params={'ccrNumber': ccrNumber, 'batchId': batchId},
                            verify=False)
    if response.status_code != 200:
        raise Exception("Target " + Config.BridgeServerCheckCCRNote + " is not reached!")
    else:
        content = json.loads(response.text)
        if content['status'] == 'passed':
            return True
        elif content['status'] == 'None' or content['status'] == 'failed':
            raise Exception('CCR ' + str(ccrNumber) + ' notes update failed!')
        elif content['status'] == 'started':
            return False

def CheckCCRNote(ccrNumber, batchId):
    TryUpdateCCRNote(ccrNumber, batchId)

    printAndFlush("Query the CCR notes updating result")
    res = QueryUpdateCCRNoteStatus(ccrNumber, batchId)
    if res:
        return True

    #start a timer to retry
    for i in range(0, 100) :
        time.sleep(1)
        printAndFlush("Query the CCR notes updating status, retry " + str(i + 1))
        res = QueryUpdateCCRNoteStatus(ccrNumber, batchId)
        if res:
            return True

    return False
