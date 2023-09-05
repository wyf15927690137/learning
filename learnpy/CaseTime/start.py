# python start.py -multi 30
# python start.py -single 20106
from getLog import LogProcessor
from Config import Config
from parseLog import ParseLog
from genXlsx import GenXLSX
import sys

logProcessor = LogProcessor(Config.jenkinsLinuxUrl, Config.user, Config.passwd)
# build number must < 500
options = sys.argv[1]
if options == "-multi":
    numbers = int(sys.argv[2])
    builds = logProcessor.getBuilds(numbers)
else:
    num = int(sys.argv[2])
    builds = logProcessor.getBuild(num)
logs = logProcessor.getLogs(builds)
files = logProcessor.downloadLogs(logs)
print(files)

for file in files:
    parse = ParseLog()
    genXls = GenXLSX()
    try:
        cases = parse.parseLog(f"{file}.txt")
        parse.parseCase(cases, file)
        genXls.genXlsx(file)
    except:
        print(f"{file} didn't run case")
