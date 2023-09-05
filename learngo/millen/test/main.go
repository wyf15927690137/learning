package main

import (
	"strconv"
	"strings"
	"time"
)
import "fmt"

func main() {
	d := strings.TrimSpace("7d")
	dr, err := time.ParseDuration(d)
	if err == nil {
		fmt.Println(err)
	}
	println(dr)
	if strings.Contains(d, "d") {
		index := strings.Index(d, "d")

		hour, _ := strconv.Atoi(d[:index])
		dr = time.Hour * 24 * time.Duration(hour)
		ndr, err := time.ParseDuration(d[index+1:])
		println(ndr)
		if err != nil {
			println(err)
		}
	}

	dv, err := strconv.ParseInt(d, 10, 64)
	println(dv)
}
