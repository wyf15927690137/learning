package main

import (
	"github.com/gin-gonic/gin"
)

func main() {
	// Create a new Gin router instance
	router := gin.Default()

	// Create a router group with a shared route prefix
	api := router.Group("/api")

	// Routes specific to the "/api" group
	api.GET("/users", getUsers)
	api.POST("/users", createUser)

	apiGroup := api.Group("/group")

	// Routes specific to the "/api/group" sub-group
	apiGroup.GET("/users", getUsersInGroup)
	apiGroup.POST("/users", createUserInGroup)

	// Start the server
	router.Run(":8888")
}

func getUsers(c *gin.Context) {
	// Handle GET request for "/api/users"
	// use the c.JSON() method to send a JSON response back to the client with a status code of 200 (OK) and a JSON object containing a “message” key with the value “Get users”.
	c.JSON(200, gin.H{
		"message": "Get users",
	})
}

func createUser(c *gin.Context) {
	// Handle POST request for "/api/users"
	c.JSON(200, gin.H{
		"message": "Create user",
	})
}

func getUsersInGroup(c *gin.Context) {
	// Handle GET request for "/api/group/users"
	c.JSON(200, gin.H{
		"message": "Get users in group",
	})
}

func createUserInGroup(c *gin.Context) {
	// Handle POST request for "/api/group/users"
	c.JSON(200, gin.H{
		"message": "Create user in group",
	})
}
