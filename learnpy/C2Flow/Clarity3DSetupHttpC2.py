import json
import os
import requests
import datetime
import boto3
import hashlib

from Clarity3DSetupUtils import LicenseHolder, ClarityUserLoginUtils, ClarityWebLibUtils, ClarityDataUtil
import base64
class C2AwsCBDInfo:
    region = ""
    url = ""
    portal_url = ""
    inited = False

class C2AwsS3Storage:
    access_key = ""
    secret_key = ""
    session_token = ""
    # prefix
    storage_folder = ""
    # bucket
    storage_bucket = ""
    expiration = ""
    isValid = False


class C2AwsUserAuthInfo:
        is_admin = False
        auth_token = ""
        auth_token_expiry_timestamp = ""

class C2AwsSessionInfo:
        cbid = ""
        cb_url = ""
        auth_token = ""
        auth_token_expiry_timestamp = ""
        heartBeatIntervalInMinutes = 0
        heartBeatTearDownMaxTimeInMinutes = 0

class Clarity3DSetupC2Utils:
    def __init__(self):
        self.g_start_py_Ohio = "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uMwppbXBvcnQgb3MKaW1wb3J0IHNzbAppbXBvcnQganNvbgppbXBvcnQgaHR0cAppbXBvcnQgdGltZQppbXBvcnQgY2JvcjIKaW1wb3J0IGxvZ2dpbmcKaW1wb3J0IGFzeW5jaW8KaW1wb3J0IGFyZ3BhcnNlCmltcG9ydCB0ZW1wZmlsZQppbXBvcnQgc3VicHJvY2VzcwppbXBvcnQgaHR0cC5jbGllbnQKaW1wb3J0IGh1bWFuZnJpZW5kbHkKaW1wb3J0IGxvZ2dpbmcuY29uZmlnCmZyb20gdXJsbGliLnBhcnNlIGltcG9ydCB1cmxwYXJzZQoKY29tcHV0ZV91cmwgPSBOb25lCmNiaWQgPSBvcy5nZXRlbnYoIkNCVF9DQl9JRCIpCmJhc2VfdXJsID0gb3MuZ2V0ZW52KCJDQlRfQ0JfVVJMIikKYXV0aHRva2VuID0gb3MuZ2V0ZW52KCJDQlRfQ0JfQVVUSFRPS0VOIikKY2xhcml0eV9yZWFsX2Jpbl9kaXIgPSBvcy5nZXRlbnYoIkNMQVJJVFlfUkVBTF9CSU5fRElSIikKCmhlYWRlcnMgPSB7CiAgICAiYXV0aHRva2VuIjogYXV0aHRva2VuCn0KCmRvY2tlcl9sYXVuY2hfc3RyID0gJ2RvY2tlciBydW4gLXQgLS1ybSdcCmYnIC12IHtjbGFyaXR5X3JlYWxfYmluX2Rpcn06L2NsYXJpdHlfZGlzdDpybydcCicgLXYgL2Vmcy9kYXRhL3Jlc3VsdGRpcjovd29ya2RpcidcCicgLXYgL2Vmcy9kYXRhOi9lZnMvZGF0YTpybydcCicgLWUgQ0xPRz0iKj1kZWJ1ZyInXAonIC1lIFBBVEg9L3Vzci9sb2NhbC9zYmluOi91c3IvbG9jYWwvYmluOi91c3Ivc2JpbjovdXNyL2Jpbjovc2JpbjovYmluJ1wKJyBjbGFyaXR5X3JlbDpsYXRlc3QnCgpkZWYgZ2V0X2xvZ2dlcigpOgogICAgZGVmYXVsdF9mb3JtYXQgPSAnJShhc2N0aW1lKXMuJShtc2VjcykwM2QgfCAlKG5hbWUpcyB8ICUobGV2ZWxuYW1lKXMgXAogICAgfCAlKHByb2Nlc3MpcyB8ICUobWVzc2FnZSlzJwogICAgZGVmYXVsdF9kYXRlZm10ID0gJyV5JW0lZDolSCVNJVMnCiAgICBmb3JtYXR0ZXIgPSBsb2dnaW5nLkZvcm1hdHRlcihkZWZhdWx0X2Zvcm1hdCkKICAgIGZvcm1hdHRlci5jb252ZXJ0ZXIgPSB0aW1lLmdtdGltZQogICAgZm9ybWF0dGVyLmRhdGVmbXQgPSBkZWZhdWx0X2RhdGVmbXQKICAgIHRoZV9jb25zb2xlID0gbG9nZ2luZy5TdHJlYW1IYW5kbGVyKCkKICAgIHRoZV9jb25zb2xlLnNldEZvcm1hdHRlcihmb3JtYXR0ZXIpCgogICAgbG9nZ2luZy5iYXNpY0NvbmZpZyhsZXZlbD1sb2dnaW5nLklORk8sIGhhbmRsZXJzPVt0aGVfY29uc29sZV0pCiAgICByZXR1cm4gbG9nZ2luZy5nZXRMb2dnZXIoIkF3c1JtdExuY2hyIikKCmxvZ2dlciA9IGdldF9sb2dnZXIoKQoKCmFzeW5jIGRlZiBnZXRfbWVzc2FnZXMoKToKICAgIGdsb2JhbCBiYXNlX3VybCwgYXV0aHRva2VuLCBoZWFkZXJzCiAgICB1cmwgPSB1cmxwYXJzZShjb21wdXRlX3VybCkKICAgIGxvZ2dlci5pbmZvKGYiVVJMOiB7dXJsfSIpCiAgICBsb2dnZXIuaW5mbyhmIkhFQURFUlM6IHtoZWFkZXJzfSIpCiAgICBsb2dnZXIuaW5mbyhmIlN0YXJ0aW5nIGNvbm5lY3Rpb246eyB1cmx9IikKICAgIGNvbnRleHQgPSBzc2wuU1NMQ29udGV4dCgpCiAgICBjb250ZXh0LmxvYWRfdmVyaWZ5X2xvY2F0aW9ucyhjYXBhdGg9Ii9ldGMvc3NsL2NlcnRzLyIpCiAgICBjb25uID0gaHR0cC5jbGllbnQuSFRUUFNDb25uZWN0aW9uKHVybC5uZXRsb2MsIGNvbnRleHQ9Y29udGV4dCkKICAgIGNvbm4ucmVxdWVzdCgiR0VUIiwgdXJsLnBhdGgsIGhlYWRlcnM9aGVhZGVycykKICAgIHJlc3AgPSBjb25uLmdldHJlc3BvbnNlKCkKICAgIHRyeToKICAgICAgICBsb2dnZXIuaW5mbyhmIlJlc3A6IHtyZXNwfSIpCiAgICAgICAgcmVzcCA9IGNib3IyLmxvYWRzKHJlc3AucmVhZCgpKQogICAgICAgIGxvZ2dlci5pbmZvKGYie2pzb24uZHVtcHMocmVzcCl9IikKICAgICAgICBpZiAiZGF0YSIgaW4gcmVzcDoKICAgICAgICAgICAgcmV0dXJuIHJlc3BbImRhdGEiXVsiYXR0cmlidXRlcyJdWyJpcCJdCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGVycjoKICAgICAgICBsb2dnZXIuaW5mbyhmIkVycm9yIE9jY3VyZWQ6IHtlcnJ9IikKICAgIHJldHVybiBOb25lCgphc3luYyBkZWYgYWRkX2NvbXB1dGUoY3B1LCBtZW0pOgogICAgZ2xvYmFsIGNvbXB1dGVfdXJsCiAgICB1cmwgPSB1cmxwYXJzZShiYXNlX3VybCArICJhZGROZXdDb21wdXRlIikKCiAgICBoZWFkZXJzID0gewogICAgICAgICdhdXRodG9rZW4nOiBmInthdXRodG9rZW59IiwKICAgICAgICAnQ29udGVudC10eXBlJzogJ2FwcGxpY2F0aW9uL2pzb24nCiAgICB9CgogICAgcGFyYW1zID0gewogICAgICAgICJ2Q3B1cyI6IGYie2NwdX0iLAogICAgICAgICJtZW1vcnkiOiBmInttZW19IgogICAgfQogICAgbG9nZ2VyLmluZm8oZiJTdGFydGluZyBjb25uZWN0aW9uOnsgdXJsfSIpCiAgICBjb250ZXh0ID0gc3NsLlNTTENvbnRleHQoKQogICAgY29udGV4dC5sb2FkX3ZlcmlmeV9sb2NhdGlvbnMoY2FwYXRoPSIvZXRjL3NzbC9jZXJ0cy8iKQogICAgY29ubiA9IGh0dHAuY2xpZW50LkhUVFBTQ29ubmVjdGlvbih1cmwubmV0bG9jLCBjb250ZXh0PWNvbnRleHQpCiAgICBjb25uLnJlcXVlc3QoIlBPU1QiLCB1cmwucGF0aCwganNvbi5kdW1wcyhwYXJhbXMpLCBoZWFkZXJzKQogICAgcmVzcCA9IGNvbm4uZ2V0cmVzcG9uc2UoKQogICAgcmVzcF9qc29uID0ganNvbi5sb2FkcyhyZXNwLnJlYWQoKS5kZWNvZGUoKSkKICAgIGxvZ2dlci5pbmZvKGpzb24uZHVtcHMocmVzcF9qc29uKSkKICAgIGNvbXB1dGVfdXJsID0gcmVzcF9qc29uWyJkYXRhIl1bImF0dHJpYnV0ZXMiXVsiYWRkQ29tcHV0ZVJlc3BvbnNlVVJMIl0KCmFzeW5jIGRlZiBzdGFydF9zdmNsYXVuY2hlcihyZW1vdGVfaXAsIGFyZ3MpOgogICAgc3NoX3Bhcm1zID0gIi1pIC9lZnMvZGF0YS9pZF9yc2EgLW8gU3RyaWN0SG9zdEtleUNoZWNraW5nPW5vIC14IgogICAgY21kc3RyID0gZiIvdXNyL2Jpbi9zc2gge3NzaF9wYXJtc30gZWMyLXVzZXJAe3JlbW90ZV9pcH0ge2FyZ3N9IgogICAgbG9nZ2VyLmluZm8oZiJDbWQgU3RyOiB7Y21kc3RyfSIpCgogICAgY21kbHN0ID0gY21kc3RyLnNwbGl0KCIgIikKICAgIHByb2MgPSBhd2FpdCBhc3luY2lvLmNyZWF0ZV9zdWJwcm9jZXNzX2V4ZWMoKmNtZGxzdCkKICAgIGF3YWl0IHByb2Mud2FpdCgpCiAgICBsb2dnZXIuaW5mbyhmIlN2Y2xhdW5jaGVyIGV4aXRlZCB3aXRoIFJDOiB7cHJvYy5yZXR1cm5jb2RlfSIpCiAgICByZXR1cm4gVHJ1ZQoKYXN5bmMgZGVmIG1haW4oKToKICAgIHBhcnNlciA9IGFyZ3BhcnNlLkFyZ3VtZW50UGFyc2VyKCkKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoJy0tbWVtJykKICAgIHBhcnNlci5hZGRfYXJndW1lbnQoJy0tY3B1cycsIHR5cGU9aW50KQogICAgYXJncywgcmVzdCA9IHBhcnNlci5wYXJzZV9rbm93bl9hcmdzKCkKICAgIG51bV9ieXRlcyA9IGh1bWFuZnJpZW5kbHkucGFyc2Vfc2l6ZShhcmdzLm1lbSkKICAgIGxvZ2dlci5pbmZvKGYiQXJncyBjcHVzOiB7YXJncy5jcHVzfSB7bnVtX2J5dGVzfSIpCiAgICB0cnk6CiAgICAgICAgYXdhaXQgYWRkX2NvbXB1dGUoYXJncy5jcHVzLCBudW1fYnl0ZXMpCiAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGVycjoKICAgICAgICBsb2dnZXIuZXJyb3IoZiJBZGQgQ29tcHV0ZSBDYWxsIEZhaWxlZDpcblx0e2Vycn0iKQogICAgICAgIHJldHVybiBGYWxzZQoKICAgIHJlbW90ZV9pcCA9IE5vbmUKICAgIGJlZ2luX3dhaXRfdGltZSA9IHRpbWUudGltZSgpCiAgICBwYXRpZW5jZSA9IDYwLjAgKiAxMC4wICMxMCBtaW51dGVzCiAgICB3aGlsZSBOb25lID09IHJlbW90ZV9pcDoKICAgICAgICAjIElmIHdlIGRvbid0IGhhdmUgaXQgYWZ0ZXIgYSB3aGlsZSB0aGVuIGV4aXQgYW5kIGxldCBzb21lb25lIGVsc2UgdHJ5CiAgICAgICAgaWYgKHRpbWUudGltZSgpIC0gYmVnaW5fd2FpdF90aW1lKSA+IHBhdGllbmNlOgogICAgICAgICAgICBicmVhawogICAgICAgIHJlbW90ZV9pcCA9IGF3YWl0IGdldF9tZXNzYWdlcygpCiAgICBpZiByZW1vdGVfaXAgaXMgTm9uZToKICAgICAgICBsb2dnZXIuaW5mbygiSSBhbSBuZXZlciBnZXR0aW5nIGFuIElQIHNvIGdpdmluZyB1cCIpCiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICBsb2dnZXIuaW5mbyhmIlJlbW90ZUlwOiB7cmVtb3RlX2lwfSIpCgogICAgcmVtb3Rlc19sYXVuY2hfY21kX2ZpbGUgPSAiL3dvcmtkaXIvYXRsYXNfbGF1bmNoLWxhdGVzdC9yZW1vdGVfbGF1bmNoZXJzIgogICAgdHJ5OgogICAgICAgIG9zLm1ha2VkaXJzKHJlbW90ZXNfbGF1bmNoX2NtZF9maWxlKQogICAgZXhjZXB0OgogICAgICAgIHBhc3MKCiAgICBmZCwgZnBhdGggPSB0ZW1wZmlsZS5ta3N0ZW1wKGRpcj1yZW1vdGVzX2xhdW5jaF9jbWRfZmlsZSwgdGV4dD1UcnVlKQogICAgb3Mud3JpdGUoZmQsIHJlc3RbMF0uZW5jb2RlKCkpCiAgICBvcy5jbG9zZShmZCkKCiAgICByZXR1cm4gYXdhaXQgc3RhcnRfc3ZjbGF1bmNoZXIocmVtb3RlX2lwLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGYie2RvY2tlcl9sYXVuY2hfc3RyfSAvYmluL2Jhc2gge2ZwYXRofSIpCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgIyBJZiB3ZSByZXR1cm4gd2l0aG91dCBzdGFydGluZyBzb21ldGhpbmcgdGhlbiBpdCB3aWxsIG5vdCBiZSBjYWxsZWQgYWdhaW4KICAgICMgIEhhbmRsZSByZXRyaWVzIGludGVybmFsbHkKICAgIGxvZ2dlci5pbmZvKCJTdGFydGluZyB0byBhcXVpcmUgcmVtb3RlIG5vZGUiKQogICAgd2hpbGUgVHJ1ZToKICAgICAgICB0cnk6CiAgICAgICAgICAgICMgcmlnaHQgbm93IEF0bGFzIGRvZXNuJ3QgdXNlIHJlc3RhcnRlZCBsYXVuY2hlcnMgdGhpcyBpcyBiYWQgYW5kCiAgICAgICAgICAgICMgbmVlZHMgdG8gYmUgZml4ZWQgYnV0IGZvciBub3cgSSBkb24ndCBuZWVkIHRvIHJlbGF1bmNoCiAgICAgICAgICAgIGlmIGFzeW5jaW8ucnVuKG1haW4oKSk6CiAgICAgICAgICAgICAgICBwcmludCgiQnJlYWtpbmcgdGhlIGxvb3Agd2lsbCBub3QgcmV0cnkgc3ZjbGF1bmNoZXIiKQogICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICAgICAgbG9nZ2VyLmluZm8oIkxhdW5jaGVyIG5vdCBzdGFydGVkIHdpbGwgc2xlZXAgZm9yIGEgc2VjIGFuZCB0aGVuIHJldHJ5IikKICAgICAgICAgICAgdGltZS5zbGVlcCgxKQogICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgYnJlYWsKICAgIGxvZ2dlci5pbmZvKCJGaW5pc2hlZCB3aXRoIHJlbW90ZSBub2RlIikK";
        self.g_tst_json_Ohio_Prod = "ewogICAgImF3cyI6IHsKICAgICAgICAiYXdzX2NiZCI6IHsKICAgICAgICAgICJyZWdpb24iOiAiT3JlZ29uIiwKICAgICAgICAgICJ1cmwiOiAiaHR0cHM6Ly9oeWJyaWRjbG91ZC5jYWRlbmNlY2xvdWQubmV0LyIsCiAgICAgICAgICAicG9ydGFsX3VybCI6ICJodHRwczovL3BvcnRhbC5jYWRlbmNlY2xvdWQubmV0L2FwaS8iCiAgICAgICAgfQogICAgfQp9";
        self.g_tst_json_Ohio = "ewogICAgImF3cyI6IHsKICAgICAgICAiYXdzX2NiZCI6IHsKICAgICAgICAgICJyZWdpb24iOiAiT2hpbyIsCiAgICAgICAgICAidXJsIjogImh0dHBzOi8vZDFveXVwam1pM2g5bjYuY2xvdWRmcm9udC5uZXQvIiwKICAgICAgICAgICJwb3J0YWxfdXJsIjogImh0dHBzOi8vcG9ydGFsYmV0YS5jYWRlbmNlY2xvdWQubmV0L2FwaS8iCiAgICAgICAgfQogICAgfQp9Cg==";
        self.g_tst_json_Virginia = "ewogICAgImF3cyI6IHsKICAgICAgICAiYXdzX2NiZCI6IHsKICAgICAgICAgICAgInJlZ2lvbiI6ICJOLiBWaXJnaW5pYSIsCiAgICAgICAgICAgICJ1cmwiOiAiaHR0cHM6Ly9kNjJobTV0NDdobjVhLmNsb3VkZnJvbnQubmV0LyIsCiAgICAgICAgICAgICJwb3J0YWxfdXJsIjogImh0dHBzOi8vcG9ydGFsZHYuY2FkZW5jZWNsb3VkLm5ldC9hcGkvIgogICAgICAgIH0KICAgIH0KfQ==";
        self.g_tst_json_Oregon = "ewogICAgImF3cyI6IHsKICAgICAgICAiYXdzX2NiZCI6IHsKICAgICAgICAgICJyZWdpb24iOiAiT3JlZ29uIiwKICAgICAgICAgICJhcGlrZXkiOiAiVUJScTVIOW1KVzY0NTZvTmpLTTd3OEtGYVZnVnZlSWY3RzNyRjB6eSIsCiAgICAgICAgICAidXJsIjogImh0dHBzOi8vZDYyaG01dDQ3aG41YS5jbG91ZGZyb250Lm5ldC8iLAogICAgICAgICAgInBvcnRhbF91cmwiOiAiaHR0cHM6Ly9wb3J0YWxkdi5jYWRlbmNlY2xvdWQubmV0L2FwaS8iCiAgICAgICAgfQogICAgfQp9Cg==";

    def genC2TstConfig(self):
        decoded_bytes = base64.b64decode(self.g_tst_json_Virginia)
        # Convert the bytes to a string
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

    def genC2StartPy(self):
        decoded_bytes = base64.b64decode(self.g_start_py_Ohio)
        # Convert the bytes to a string
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string



class C2CloudJobManager:
    def __init__(self):
        self.m_licRemotes = LicenseHolder()
        self.m_awsCbdInfo = C2AwsCBDInfo()
        self.m_awsUserAuthInfo = C2AwsUserAuthInfo()
        self.m_userId = "clarity_test_user_3@cssotest.com"
        self.m_password = "Cadence123"
        self.m_runType = "FIRST_LAUNCH"
        self.m_jobIdFromCase = ""
        self.m_quitForce = False

    def getC2CloudInstance(self):
        return self

    def resetStatus(self):
        self.m_quitForce = False

    def setLicenseRemotes(self, licNumRemotes):
        self.m_licRemotes = licNumRemotes
        hostID = self.m_licRemotes.m_host_id
        licType = self.m_licRemotes.m_LIC_TYPE_1

    def setRunType(self):
        pass

    def setJobIdForResumeOrReconnect(self, id):
        self.m_jobIdFromCase = id

    def loadAwsConfig(self):
        if self.m_awsCbdInfo.inited:
            return True

        if not self.initAwsCbdInfo():
            return False

        return True

    def initAwsCbdInfo(self):
        if self.m_awsCbdInfo.inited:
            return False

        config_json = Clarity3DSetupC2Utils().genC2TstConfig()
        data = json.loads(config_json)
        self.m_awsCbdInfo.region = data["aws"]["aws_cbd"]["region"]
        self.m_awsCbdInfo.url = data["aws"]["aws_cbd"]["url"]
        self.m_awsCbdInfo.portal_url = data["aws"]["aws_cbd"]["portal_url"]
        self.m_awsCbdInfo.inited = True
        return True

    def authenticateUserImpl(self):
        self.loadAwsConfig()
        webUtil = ClarityWebLibUtils()
        authUrl = self.m_awsCbdInfo.portal_url + "authenticateUser"
        jsobj = {}
        attributes = {
            "username": self.m_userId,
            "password": self.m_password
        }
        data = {
            "type": "AuthenticateUserRequest",
            "attributes": attributes
        }
        jsobj["data"] = data
        response = requests.post(authUrl, json=jsobj, timeout=30)
        if response.ok:
            data = response.json()
            token = data['data']['attributes']['authToken']
            self.m_awsUserAuthInfo.auth_token = token
            self.m_awsUserAuthInfo.auth_token_expiry_timestamp,\
            self.m_awsUserAuthInfo.is_admin = webUtil.jwt_decode(token)
        return


    def loadUserAuthenInfo(self):
        user, passwd = ClarityUserLoginUtils().getExistingUserAccount()
        if not user or not passwd:
            return False
        self.m_userId = user
        self.m_password = passwd
        return True

    def getJobsStatusUnblocked(self):
        pass

    def startSimulation(self):
        self.resetStatus()
        self.loadAwsConfig()
        self.loadUserAuthenInfo()

        designFile = C2CloudJobEntry().getDesignFile()
        configFile = C2CloudJobEntry().getConfigFile()
        sLogFile = os.path.dirname(designFile) + configFile[:configFile.rfind('.')] + "_run.log"


class C2CloudJobEntry:
    def __init__(self):
        self.m_type = "SpdType"
        self.m_config = "one_trace.config"
        self.m_spdFile = "D:/clarity_case/one/one_trace.spd"
        self.m_savingFolder = "D:/clarity_case/one"
        self.m_onCloudJobId = ""
        self.m_isPerfMode = False
        self.m_licRemotes = LicenseHolder()
        self.m_awsCbdSession = C2AwsSessionInfo()
        self.m_isResume = False
        self.m_isSimStarted = False
        self.m_isSimFinished = False

    def getDesignFile(self):
        return self.m_spdFile

    def getConfigFile(self):
        return self.m_config

    def run(self):
        self.createStartPy()

    def setupRemoteEnvSession(self):
        c2Ins = C2CloudJobManager()
        # webUtil = ClarityWebLibUtils()
        # c2Ins.initAwsCbdInfo()
        c2Ins.authenticateUserImpl()
        url = c2Ins.m_awsCbdInfo.url + "getCBChamber/auth"
        data = self.generateStartEnvAuthRequestData(c2Ins)
        # hostName, relPath, port = webUtil.parseUrl(url)
        headers = {
            "authtoken": c2Ins.m_awsUserAuthInfo.auth_token
        }

        # url = f"http://{hostName}:{port}{relPath}"

        response = requests.post(url, json=data, headers=headers, timeout=30)

        if response.ok:
            content = response.json()
            self.m_awsCbdSession.cbid = content['data']['attributes']['cbId']
            self.m_awsCbdSession.cb_url = content['data']['attributes']['cbURL']
            self.m_awsCbdSession.heartBeatIntervalInMinutes = content['data']['attributes']['heartBeatIntervalInMinutes']
            self.m_awsCbdSession.heartBeatTearDownMaxTimeInMinutes = content['data']['attributes']['heartBeatTearDownMaxTimeInMinutes']
            self.m_awsCbdSession.auth_token = content['data']['attributes']['authtoken']
            self.m_awsCbdSession.auth_token_expiry_timestamp = content['data']['attributes']['authTokenExpiry']

            self.m_onCloudJobId = self.m_awsCbdSession.cbid

        else:
            raise Exception("Remote env auth failed!")
        return c2Ins

    def setupRemoteEnv(self):
        authUrl = self.m_awsCbdSession.cb_url + "/setupRemoteEnv"
        data = self.generateStartEnvRequestData()
        headers = {
            "authtoken": self.m_awsCbdSession.auth_token
        }
        response = requests.post(authUrl, json=data, headers=headers, timeout=30)
        if response.ok:
            res = response.json()
            if res['data']['type'] != "SetupRemoteEnvResp":
                return False
        return True

    def disableDataService(self):
        caseFile = self.getDesignFile()
        case = os.path.basename(caseFile)
        directory = os.path.dirname(caseFile)
        fileList = os.listdir(directory)
        isControlFileExists = False

        for fileName in fileList:
            if fileName.endswith("_trinity_dev.control") or fileName.endswith("_simulation_dev.control"):
                isControlFileExists = True
                break
            else:
                continue

        if not isControlFileExists:
            newControlFile = os.path.join(directory, case.split(".")[0] + "_simulation_dev.control")
            with open(newControlFile, "w") as f:
                f.write("ATLAS_ENABLE_DATA_SERVICE 0")
                f.close()
        pass

    def launchRemoteTask(self):
        authUrl = self.m_awsCbdSession.cb_url + "/runRemoteTask"
        data = self.generateStartTaskRequestData()
        headers = {
            "authtoken": self.m_awsCbdSession.auth_token
        }
        response = requests.post(authUrl, json=data, headers=headers, timeout=30)
        if response.ok:
            res = response.json()
            if res['data']['type'] != "runRemoteTask":
                return False
        return True

    def generateStartTaskRequestData(self):
        attributes = self.generateStartTaskRequestJson()
        return attributes


    def uploadCaseFileToS3(self, c2Ins):
        fileName = self.getDesignFile()
        dataUtil = ClarityDataUtil()
        self.getCloudStorage(c2Ins)
        s3Client = self.initS3Client()
        if dataUtil.validateFileName(os.path.basename(fileName)):
            fileList = self.generateUploadFileList()
            if fileList:
                for file in fileList:
                    self.uploadFileToCloud(s3Client, file)

    def uploadFileToCloud(self,s3Client, file):
        target_file = os.path.basename(file)
        cloud_path = os.path.join(C2AwsS3Storage.storage_folder, "resultdir", target_file)

        # Verify that the file exists
        if not os.path.exists(file):
            error_message = f"Error: File '{file}' does not exist."
            return False, error_message

        try:
            with open(file, 'rb') as f:
                file_content = f.read()
                md = hashlib.md5(file_content).digest()
                content_md5 = base64.b64encode(md).decode('utf-8')

                response = s3Client.put_object(
                    Bucket=C2AwsS3Storage.storage_bucket,
                    Key=cloud_path,
                    Body=file_content,
                    ContentMD5=content_md5
                )

            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return True

        except Exception as e:
            error_message = f"Error: uploading file: {file} {str(e)}"
            return False

        return False

    def initS3Client(self):
        session = boto3.Session(
            aws_access_key_id=C2AwsS3Storage.access_key,
            aws_secret_access_key=C2AwsS3Storage.secret_key,
            aws_session_token = C2AwsS3Storage.session_token
        )
        s3 = session.client('s3')

        return s3

    def getCloudStorage(self, c2Ins):
        url = c2Ins.m_awsCbdInfo.url + "getStorageAccess/auth"
        cbid = self.m_onCloudJobId
        attr = {"cbId": cbid}
        headers  = {
            "authtoken": c2Ins.m_awsUserAuthInfo.auth_token
        }
        response = requests.post(url, json=attr, headers=headers, timeout=30)
        if response.ok:
            res = response.json()
            C2AwsS3Storage.access_key = res['data']['attributes']['credentials']['accesskey']
            C2AwsS3Storage.secret_key = res['data']['attributes']['credentials']['secretKey']
            C2AwsS3Storage.expiration = res['data']['attributes']['credentials']['expiration']
            C2AwsS3Storage.storage_folder = res['data']['attributes']['credentials']['storageFolder']
            C2AwsS3Storage.storage_bucket = res['data']['attributes']['credentials']['storageBucket']
            C2AwsS3Storage.session_token = res['data']['attributes']['credentials']['sessionToken']
            C2AwsS3Storage.isValid = True
        return True

    def generateUploadFileList(self):
        case  = self.getDesignFile()
        casePath = os.path.dirname(case)
        caseName = os.path.basename(case).split(".")[0]
        allList = os.listdir(casePath)
        fList = [
                    os.path.basename(case),
                    caseName + ".prop.xml",
                    caseName + ".config",
                    caseName + ".control",
                    caseName + "_trinity_dev.control",
                    caseName + "_simulation_dev.control",
                    "start_remote.py"
                ]
        result = []
        for file in fList:
            if file in allList:
                file = os.path.join(casePath, file)
                result.append(file)
        return result
    def generateStartEnvAuthRequestData(self, c2Ins):
        jsObj = {}
        self.m_licRemotes.m_host_id = "b4969164dac4"
        license = {
            "hostId": self.m_licRemotes.m_host_id,
            "checkedOut": {
                self.m_licRemotes.m_LIC_TYPE_1: self.m_licRemotes.m_num_lic_checkedout
            }
        }

        jsObj["region"] = c2Ins.m_awsCbdInfo.region
        jsObj["tool"] = "Clarity"
        jsObj["toolVersion"] = "0.1.2"
        jsObj["licenseInfo"] = license

        return jsObj

    def generateStartEnvRequestData(self):
        license = {}
        license["hostId"] = self.m_licRemotes.m_host_id
        license["checkedOut"] = {
            self.m_licRemotes.m_LIC_TYPE_1: self.m_licRemotes.m_num_lic_checkedout
        }
        attributes = self.generateStartTaskRequestJson()
        attributes["resume"] = self.m_isResume
        attributes["continueOnDisconnect"] = True
        attributes["licenseInfo"] = license

        return attributes

    def generateStartTaskRequestJson(self):
        attributes = {}
        case = os.path.basename(self.getDesignFile())
        attributes["cmd"] = "/clarity_dist/tools/bin/run_atlas_clarity.dev"
        attributes["enviromentVars"] = [["CLARITY_CONFIG", "/workdir/" + self.m_config], ["ATLAS_ENABLE_DATA_SERVICE", "0"]]
        attributes["args"] = ["--bundle",
                              "/clarity_dist/atlas_clarity/dists.rel/latest/",
			                  "--run-dir",
                              "/workdir",
                              "--design-name",
                              self.getDesignFile(),
			                  "2>&1", "|", "tee", "-a",
                              "/workdir/" + case.split(".")[0] + "_c2_run.log"
                            ]
        curTime = datetime.datetime.utcnow()
        formTime = curTime.strftime("%Y:%m:%d %H:%M:%S")
        fileName = self.getDesignFile()
        metaData = {
            "curTime": formTime,
            "fileName": fileName
        }
        metaInfoBase64 = base64.b64encode(json.dumps(metaData).encode()).decode()
        attributes["job_metadata"] = metaInfoBase64

        if self.m_isPerfMode:
            attributes["cores"] = 64
        return attributes

    def createStartPy(self):
        startPyStr = Clarity3DSetupC2Utils.genC2StartPy()
        file = os.path.dirname(self.m_spdFile) + "/start_remote.py"
        with open(file, 'w') as f:
            f.write(startPyStr)
            f.close()
        return




if __name__ == "__main__":
    job = C2CloudJobEntry()
    c2Ins = job.setupRemoteEnvSession()
    job.setupRemoteEnv()
    # job.disableDataService()
    job.uploadCaseFileToS3(c2Ins)
    job.launchRemoteTask()