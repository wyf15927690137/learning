package main

import (
	"fmt"
	"sync"
)

func worker(id int, wg *sync.WaitGroup) {
	defer wg.Done()

	fmt.Printf("Worker %d starting\n", id)

	// Perform some work

	fmt.Printf("Worker %d completed\n", id)
}

func main() {
	var wg sync.WaitGroup

	// Launch 3 goroutines
	wg.Add(3)
	go worker(1, &wg)
	go worker(2, &wg)
	go worker(3, &wg)

	// Wait for all goroutines to complete
	wg.Wait()

	fmt.Println("All workers completed")
}