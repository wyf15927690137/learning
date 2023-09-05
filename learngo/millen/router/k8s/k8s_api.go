package k8s

import (
	"fmt"
	"github.com/gin-gonic/gin"
)

type Router struct {
	K8s string
}

func InitK8s(c *gin.Context) {
	fmt.Println("init k8s")
}

func (e *Router) InitK8sRouter(router *gin.RouterGroup) {
	customeRouter := router.Group("k8s")
	customeRouter.POST("initk8s", InitK8s)
	customeRouter.GET("initk8s", InitK8s)
}
