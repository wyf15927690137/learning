package main

import (
	"context"
	"fmt"
	"github.com/bndr/gojenkins"
	"precheck/core"
	"precheck/global"
	"precheck/initialize"
)

func main() {

	global.PrecheckViper = core.Viper()
	global.PrecheckDB = initialize.GormMysql()
	global.PrecheckLog = core.Zap()
	initialize.StartJobFlusher()
	jenkins := gojenkins.CreateJenkins(nil, global.PrecheckServer.JenkinsInfo.JenkinsUrl, global.PrecheckServer.JenkinsInfo.UserName, global.PrecheckServer.JenkinsInfo.PassWord)

	// Initialize the Jenkins client
	if _, err := jenkins.Init(context.Background()); err != nil {
		fmt.Println("Failed to create Jenkins client:", err)
		return
	}
	// Get information about the job
	jobName := "CheckBuild/job/PreCheck_main"

	job, err := jenkins.GetJob(context.Background(), jobName)
	if err != nil {
		fmt.Println("Failed to fetch job details:", err)
		return
	}

	fmt.Println("Job Name:", job.GetName())
	fmt.Println("Job Description:", job.GetDescription())
	//fmt.Println("Job Last Build Number:", job.GetLastBuildNumber())
	// ... and so on

}
