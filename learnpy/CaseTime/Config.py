import base64

class Config:
    user = "admin"
    enpasswd = "YWRtaW4xMjM0NTY3ODk="
    passwd = base64.b64decode(enpasswd).decode('ascii')
    jenkinsServer = 'http://si-rdtest1:9090'
    jenkinsLinuxUrl = 'http://si-rdtest1:9090/job/CheckBuild'
