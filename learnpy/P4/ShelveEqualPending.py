from P4 import P4, P4Exception
import base64
import sys

p4 = P4()
p4.client = "PC-DT-YANFEI"
p4.user = "yanfeiw"
# ccPwd = base64.b64decode("QzJkZW5jZUAyMDIx")
# ccPwd = ccPwd.decode('ascii')
p4.password = "Yfw!1997"
p4.port = "ssl:p4shanghai:2644"
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
p4.connect()
# info = p4.run( "info" )        # Run "p4 info" (returns a dict)
# for key in info[0]:            # and display all key-value pairs
#     print(key)

# spec = p4.run("describe", "-S", "-du", "460737")
spec = p4.run("diff", "-du", "//depot/sigrity/23.10/ISR3/Install/cm/jenkins_utils/BuildProjectLinuxUSScript.csh")
print(spec)
# spec = spec[0]
# desc = spec['depotFile']
# print(desc)