import time
import datetime
import os
import requests
import pandas as pd
import openpyxl

def download_file():

    url_list = ["http://master-sigrity.cadence.com/blue/rest/organizations/jenkins/pipelines/AutoBuild/pipelines/PostBuildSigrity_main/runs/1297/nodes/153/steps/157/log/?start=0",
                "http://master-sigrity.cadence.com/blue/rest/organizations/jenkins/pipelines/AutoBuild/pipelines/PostBuildSigrity_main/runs/1298/nodes/153/steps/157/log/?start=0",
                "http://master-sigrity.cadence.com/blue/rest/organizations/jenkins/pipelines/AutoBuild/pipelines/PostBuildSigrity_main/runs/1295/nodes/153/steps/157/log/?start=0",
                "http://si-rdtest1:9090/blue/rest/organizations/jenkins/pipelines/CheckBuild/pipelines/PreCheck_main/runs/10756/nodes/197/steps/261/log/?start=0",
                "http://si-rdtest1:9090/blue/rest/organizations/jenkins/pipelines/CheckBuild/pipelines/PreCheck_main/runs/10756/nodes/198/steps/262/log/?start=0",
                "http://si-rdtest1:9090/blue/rest/organizations/jenkins/pipelines/CheckBuild/pipelines/PreCheck_main/runs/10756/nodes/199/steps/263/log/?start=0",
                "http://si-rdtest1:9090/blue/rest/organizations/jenkins/pipelines/CheckBuild/pipelines/PreCheck_main/runs/10755/nodes/197/steps/261/log/?start=0",
                "http://si-rdtest1:9090/blue/rest/organizations/jenkins/pipelines/CheckBuild/pipelines/PreCheck_main/runs/10755/nodes/198/steps/262/log/?start=0",
                "http://si-rdtest1:9090/blue/rest/organizations/jenkins/pipelines/CheckBuild/pipelines/PreCheck_main/runs/10755/nodes/199/steps/263/log/?start=0",
                "http://master-sigrity.cadence.com/blue/rest/organizations/jenkins/pipelines/AutoBuild/pipelines/CheckCM/runs/24/nodes/67/steps/119/log/?start=0"]
    num = 1
    result = []
    for url in url_list:
        response = requests.get(url, stream=True)

        with open(f'{num}.txt', 'wb') as file:
            for data in response.iter_content(128):
                file.write(data)
        print(response.status_code)
        result.append(f"{num}.txt")
        num = num + 1
    return result 

def get_case(case_name):
    str = './'
    index = case_name.index(str) + 2
    result = ''
    while(case_name[index] != ' ' and case_name[index] != ':'):
        result = result + case_name[index]
        index = index + 1
    return result

def Get_Standard_TimeStamp_string(timestamp):
    timestamp = timestamp[1:11] + ' ' + timestamp[12:20]
    return timestamp

def CaculateSingeLog(file):
    passed_case = {}
    failed_case = {}
    ignored_case = {}
    
    s_file = open(file,"r",encoding='UTF-8')
    all_content = s_file.read()
    lines = all_content.split('\n')
    start_time_stamp_string = Get_Standard_TimeStamp_string(lines[0][0:26])
    start_time_stamp = datetime.datetime.strptime(start_time_stamp_string, "%Y-%m-%d %H:%M:%S")
    print(f"The start time stamp: {start_time_stamp}")

    for one_line in lines:
        if "  PASSED on " in one_line or "  FAILED on " in one_line: 
            end_time_stamp_string = Get_Standard_TimeStamp_string(one_line[0:26])
            end_time_stamp = datetime.datetime.strptime(end_time_stamp_string,"%Y-%m-%d %H:%M:%S")
            cost_time_stamp = end_time_stamp - start_time_stamp
            start_time_stamp = end_time_stamp
            case_name = get_case(one_line)
            if "  PASSED on " in one_line:
                passed_case[case_name] = cost_time_stamp
            else:
                failed_case[case_name] = cost_time_stamp
        if ": Ignored" in one_line:
            case_name = get_case(one_line)
            time_zero = datetime.datetime.strptime("00:00:00","%H:%M:%S")
            cost_time_stamp =time_zero - time_zero
            ignored_case[case_name] = cost_time_stamp
    return passed_case,failed_case,ignored_case

def get_max_min_timecost(cases):
    zero_time = datetime.datetime.strptime("00:00:00","%H:%M:%S")
    max_time_cost = zero_time - zero_time
    min_time_cost = datetime.datetime.strptime("23:59:59","%H:%M:%S") - zero_time
    max_time_case = ""
    min_time_case = ""
    for k,v in cases.items():
        if v >= max_time_cost:
            max_time_cost = v
            max_time_case = k
        if v <= min_time_cost:
            min_time_cost = v
            min_time_case = k
    if min_time_cost == (datetime.datetime.strptime("23:59:59","%H:%M:%S") - zero_time):
        min_time_cost = zero_time - zero_time
    return max_time_cost, max_time_case, min_time_cost, min_time_case

def write_result(passed,failed,ignored,name):
    passed_number = len(passed)
    failed_number = len(failed)
    ignored_number = len(ignored)
    result = []
    cur = []
    # index
    case_name = []
    # column
    columns = ["Passed","Failed","Ignored"]
    zero_time = datetime.datetime.strptime("00:00:00","%H:%M:%S")
    total_passed_time = zero_time - zero_time
    total_failed_time = zero_time - zero_time
    total_ignored_time = zero_time - zero_time
    total_result = []
    for k,v in passed.items():
        case_name.append(k)
        cur = [str(v),'','']
        result.append(cur)
        total_passed_time = total_passed_time + v
    for k,v in failed.items():
        case_name.append(k)
        cur = ['',str(v),'']
        result.append(cur)
        total_failed_time = total_failed_time + v
    for k,v in ignored.items():
        case_name.append(k)
        cur = ['','',str(v)]
        result.append(cur)
        total_ignored_time = total_ignored_time + v
    df = pd.DataFrame(result,index=case_name,columns=columns)
    # index
    index = ["Total Time Cost","Average Time Cost","Max Time Cost Case","Min Time Cost","Max Time Cost","Min Time Cost Case","Case Numbers"]
    total_result.append([str(total_passed_time),str(total_failed_time),str(total_ignored_time)]) 
    max_passed_time, max_passed_case, min_passed_time, min_passed_case = get_max_min_timecost(passed)
    max_failed_time, max_failed_case, min_failed_time, min_failed_case = get_max_min_timecost(failed)
    if passed_number == 0:
        average_passed_time = zero_time - zero_time
    else:
        average_passed_time = total_passed_time/passed_number
    if failed_number == 0:
        average_failed_time = zero_time - zero_time
    else:
        average_failed_time = total_failed_time/failed_number
    if ignored_number == 0:
        average_ignored_time = zero_time - zero_time
    else:
        average_ignored_time = total_ignored_time/ignored_number
    total_result.append([str(average_passed_time)[:7],str(average_failed_time)[:7],str(average_ignored_time)[:7]])
    total_result.append([max_passed_case, max_failed_case, ""])
    total_result.append([str(max_passed_time),str(max_failed_time),str(zero_time - zero_time)])
    total_result.append([min_passed_case, min_failed_case, ""])
    total_result.append([str(min_passed_time),str(min_failed_time),str(zero_time -zero_time)])
    total_result.append([passed_number,failed_number,ignored_number])
    total_df = pd.DataFrame(total_result,index=index,columns=columns)
    with pd.ExcelWriter(name) as writer:
        df.to_excel(writer,sheet_name='sheet1')
        total_df.to_excel(writer,sheet_name='sheet2')


# getlog("./data")
files = download_file()
num = 1
for file in files:
    passed,failed,ignored = CaculateSingeLog(file)
    name = f"{num}.xlsx"
    write_result(passed,failed,ignored,name)
    num = num + 1