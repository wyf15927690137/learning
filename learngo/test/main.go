package main

import (
	"fmt"
	"strings"
)

func main() {
	var sts []string
	sts = append(sts, "121")
	sts = append(sts, "fa")
	for index, value := range sts {
		println(index)
		println(value)6
	}

	stringA := "abcdefGHIJ"
	stringB := "abcdefXYZ"
	println(stringB[:6])

	if strings.HasPrefix(stringA, stringB[:6]) {
		fmt.Println("The first 6 letters of string A are the same as string B.")
	} else {
		fmt.Println("The first 6 letters of string A are different from string B.")
	}
}
