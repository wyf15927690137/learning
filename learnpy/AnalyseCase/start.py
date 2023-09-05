# python start.py 30
from getLog import LogProcessor
from Config import Config
from parseLog import ParseLog
from genXlsx import GenXLSX
import sys

logProcessor = LogProcessor(Config.jenkinsLinuxUrl, Config.user, Config.passwd)
# build number must < 500
build_nums = int(sys.argv[1])
builds = logProcessor.getBuilds(build_nums)
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
