package main

import (
	"fmt"
	"os"
	"strings"

	"./LFU"
	"./LRU"
)

func main() {
	args := os.Args[1:]
	debug := false
	var toRun []string

	for _, arg := range args {
		val := strings.ToLower(arg)

		if val == "--debug" || val == "-d" {
			debug = true
			continue
		}

		switch val {
		case "lfu":
			toRun = append(toRun, "lfu")
		default:
			fmt.Printf("Flag not supported: %s\n", arg)
		}
	}

	for _, problem := range toRun {
		switch problem {
		case "lfu":
			lfu.Run(2, debug)
		case "lru":
			lru.Run(2, debug)
		default:
			fmt.Printf("Problem category not defined...")
		}
	}

	fmt.Println("\nDone...")
}
