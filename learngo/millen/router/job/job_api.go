package job

import "github.com/gin-gonic/gin"
import "fmt"

type Router struct {
	Job string
}

func CreateJob(c *gin.Context) {
	fmt.Println("create job")
}

func (e *Router) InitJobRouter(router *gin.RouterGroup) {
	customeRouter := router.Group("job")
	customeRouter.POST("newjob", CreateJob)
	customeRouter.GET("newjob", CreateJob)
}
