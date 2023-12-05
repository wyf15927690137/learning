package main

import (
	"fmt"
	"regexp"
)

func main() {
	re := regexp.MustCompile(`^mln-\d+w\d+-.*$`)
	str := "mln-302w1-7c4668d8d-l9fj2"

	if re.MatchString(str) {
		fmt.Println("String matches the format")
	} else {
		fmt.Println("String does not match the format")
	}
}