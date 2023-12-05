import os
import json
import jwt

# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Hash import SHA256, MD5
from urllib.parse import urlparse


class LicenseHolder:
    def __init__(self):
        # self.m_LIC_TYPE_1 = "Clarity_3DSolverG"
        self.m_LIC_TYPE_1 = "Clarity_3D_v32C"
        self.m_host_id = "LIC_SUPPORT_DISABLED"
        self.m_num_lic_checkedout = 1

class ClarityUserLoginUtils:
    def __init__(self):
        pass

    def isUserAccountExisting(self):
        res = self.getExistingUserAccount()
        return res[0] != "" and res[1] != ""

    def getExistingUserAccount(self):
        loginFile = self.userLoginAccountFileName()
        if not loginFile:
            return "", ""
        with open(loginFile) as file:
            data = json.load(file)
        user = data["user"]
        encryptedPasswd = data["password"]
        passwd = self.decodeOperation(encryptedPasswd)

        return user, passwd

    def setUserAccount(self):
        pass

    def userLoginAccountFileName(self):
        homePath = os.path.expanduser("~")
        loginFile = homePath + "/.cadence/Clarity" + "/userAccount_Test.json"
        return loginFile

    def decodeOperation(self, encryptedString):
        if len(encryptedString) == 0:
            return ""

        key = b'clarity-aes-key'
        iv = b'clarity-aes-IV-vector'

        hashKey = SHA256.new(key).digest()
        hashIV = MD5.new(iv).digest()

        cipher = AES.new(hashKey, AES.MODE_CBC, hashIV)
        decodeText = cipher.decrypt(bytes.fromhex(encryptedString))
        decodedString = decodeText.rstrip(b'\0').decode()

        return decodedString


class ClarityWebLibUtils:
    def __init__(self):
        pass

    def jwt_decode(self, token):
        res = ('', '')  # Empty strings as default result
        if not token:
            return res

        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            return decoded['authTokenExpiry'], decoded['isAdmin']
        except jwt.InvalidTokenError:
            return res

    def parseUrl(self, url):
        parsed_url = urlparse(url)

        # Extract hostname
        hostname = parsed_url.hostname  # "d62hm5t47hn5a.cloudfront.net"
        rel_path = parsed_url.path  # "/getCBChamber/auth"
        port = parsed_url.port  # 443

        # Ensure the port is set correctly if not explicitly defined in the URL
        if port is None:
            if url.startswith("https://"):
                port = 443
            elif url.startswith("http://"):
                port = 80
        return hostname, rel_path, port

class ClarityDataUtil:
    def __init__(self):
        pass

    def validateFileName(self, fileName):
        for cha in fileName:
            if cha.isalpha() or cha.isdigit() or cha == "_" or cha == "-" or cha == "." or cha == "/":
                continue
            else:
                return False
        return True


if __name__ == "__main__":
    util = ClarityUserLoginUtils()
    print(util.isUserAccountExisting())