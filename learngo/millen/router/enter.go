package router

import (
	"yanfeiw/millen/router/job"
	"yanfeiw/millen/router/k8s"
)

type Router struct {
	Job job.RouterGroup
	K8s k8s.RouterGroup
}

var GroupApp = new(Router)
