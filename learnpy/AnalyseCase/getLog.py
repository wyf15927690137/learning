import requests

from Config import Config
from jenkinsapi.jenkins import Jenkins

class LogProcessor:
    def __init__(self, jenkinsUrl , username, password):
        self.jenkinsUrl = jenkinsUrl
        self.username = username
        self.password = password
        pass

    def getBuilds(self, num):
        jnk = Jenkins(self.jenkinsUrl, self.username, self.password, timeout=30)
        for job in jnk.keys():
            if job == "PreCheck_main":
                all_builds = jnk[job].get_build_dict()
                builds = [(key, all_builds[key]) for key in all_builds.keys()]
                builds = builds[20:20 + num]
        return builds

    def getLogs(self, builds):
        results = []
        if len(builds) < 1:
            return results
        server = Config.jenkinsServer

        for build in builds:
            build_number = build[0]
            build_url = build[1] + "wfapi/"
            logs = []
            response = requests.get(build_url)
            data = response.json()
            stages = data['stages']
            for stage in stages:
                if "Automation" in stage['name']:
                    automation = requests.request("GET", server + stage['_links']['self']['href'])
                    dat = automation.json()
                    stage_flow_nodes = dat['stageFlowNodes']
                    for one in stage_flow_nodes:
                        if "Shell" in one['name']:
                            log = one['_links']['console']['href']
                            logs.append(server + log)
            results.append({build_number: logs})
        return results

    def downloadLogs(self, logs):
        nums = []
        for log in logs:
            for num, urls in log.items():
                nums.append(num)
                if urls == []:
                    break
                for url in urls:
                    response = requests.get(url + "/?consoleFull", stream=True)
                    with open(f'{num}.txt', 'ab') as file:
                        for data in response.iter_content(128):
                            file.write(data)
        return nums



if __name__ == "__main__":
    logProcessor = LogProcessor(Config.jenkinsLinuxUrl, Config.user, Config.passwd)
    # build number must < 500
    build_nums = 2
    builds = logProcessor.getBuilds(build_nums)
    logs = logProcessor.getLogs(builds)
    logProcessor.downloadLogs(logs)

