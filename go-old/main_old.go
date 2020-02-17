package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"

	bipartition "./Bipartition"
	bitorsub "./BitOrSub"
	lfu "./LFU"
	lru "./LRU"
)

func main1() {
	args := os.Args[1:]
	debug := false
	testCase := 1

	var toRun []string

	for _, arg := range args {
		val := strings.ToLower(arg)

		if val == "--debug" || val == "-d" {
			debug = true
			continue
		}

		param := strings.SplitN(val, "=", 2)

		if len(param) == 2 {
			switch param[0] {
			case "test":
				num, err := strconv.Atoi(param[1])
				if err != nil || num < 0 {
					fmt.Printf("Unable to parse the test case number: %s", param[1])
				}

				testCase = num

			default:
			}

			continue
		}

		if val == "lfu" || val == "lru" || val == "bipartition" || val == "bit" {
			toRun = append(toRun, val)
		}
	}

	fmt.Println("====== Running... ======")
	fmt.Println()

	for _, problem := range toRun {
		switch problem {
		case "lfu":
			lfu.Run(2, debug)
		case "lru":
			lru.Run(2, debug)
		case "bipartition":
			bipartition.Run(testCase, debug)
		case "bit":
			bitorsub.Run(testCase, debug)
		default:
			fmt.Printf("\n>>> Problem category not defined... <<<\n")
		}
	}

	fmt.Println("\n====== Done ======")
	fmt.Println()
}
