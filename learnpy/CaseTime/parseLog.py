from datetime import datetime
import pandas as pd

class ParseLog:
    def __init__(self):
        pass

    def getProduct(self, str):
        split_str = []
        if "Install/cm/jenkins_utils/RunPVLinuxRegression.sh /data/Automation" in str:
            split_str = str.split(" ")
        return split_str

    def caseTimeCost(self, str, start_time):
        split_str = str.split(" ")
        result = [split_str[5], start_time, split_str[4][7:27]]
        return result
    def parseLog(self, file):
        s_file = open(file, "r", encoding='UTF-8')
        all_content = s_file.read()
        lines = all_content.split('\n')
        result = []
        for line in lines:
            re = self.getProduct(line)
            if re != []:
                start_time = re[4][7:27]
                product = re[8]
                result.append(product)
            if "  PASSED on " in line or "  FAILED on " in line:
                caseStatus = self.caseTimeCost(line, start_time)
                start_time = caseStatus[2]
                if "  PASSED on " in line:
                    caseStatus.append("PASSED")
                else:
                    caseStatus.append("FAILED")
                result.append(caseStatus)
            # if "Sending interrupt signal to process" in line:
            #     caseStatus =self.caseTimeCost(line,start_time)
        return result

    def getStandardTimeStampString(self, timestamp):
        timestamp = timestamp[0:10] + ' ' + timestamp[11:19]
        return timestamp
    def parseCase(self, cases, num):
        for case in cases:
            if type(case) == list:
                case[1] = self.getStandardTimeStampString(case[1])
                case[2] = self.getStandardTimeStampString(case[2])
                cost_time_stamp = datetime.strptime(case[2],"%Y-%m-%d %H:%M:%S") - datetime.strptime(case[1],"%Y-%m-%d %H:%M:%S")
                cu_re = [case[0], str(cost_time_stamp), case[3]]
                with open(f"{num}_case.txt", "a") as file:
                    file.write(str(cu_re) + '\n')
            else:
                with open (f"{num}_case.txt", "a") as file:
                    file.write(str(case) + '\n')

if __name__ == "__main__":
    parse = ParseLog()
    cases = parse.parseLog("20019.txt")
    parse.parseCase(cases, 20019)