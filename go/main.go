package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"

	problems "./Problems"
	d "./Utils"
)

func main() {
	args := os.Args[1:]
	testCase := 0

	var toRun string

	for _, arg := range args {
		val := strings.ToLower(arg)

		if val == "--debug" || val == "-d" {
			d.DEBUG = true
			continue
		}

		param := strings.SplitN(val, "=", 2)

		switch len(param) {
		case 1:
			toRun = strings.ToLower(param[0])

		case 2:
			switch param[0] {
			case "test":
				num, err := strconv.Atoi(param[1])
				if err != nil || num < 0 {
					fmt.Printf("Unable to parse the test case number: %s\n", param[1])
				}

				testCase = num

			default:
				fmt.Printf("Unable to recognize this param: %s", param[0])
			}

		default:
			fmt.Printf("Illegal params: %s ...", val)
		}
	}

	d.Debug(
		fmt.Sprintf(
			"Running debug mode...\n>> Input Arguments... \n>>   is-debug:  { %t } \n>>   test-case: { %d }\n",
			d.DEBUG,
			testCase,
		),
		0,
	)

	fmt.Println()
	fmt.Println("====== Running ======")
	fmt.Println()

	var elapsed time.Duration
	var done bool

	if len(toRun) > 0 {
		p, err := problems.Create(toRun)
		if err != nil {
			fmt.Print(err)
			return
		}

		start := time.Now()
		p.Build(testCase)
		p.Run()

		elapsed = time.Since(start)
		done = true
	} else {
		fmt.Println("Unable to find the problem to run...")
	}

	fmt.Println("\n======  Done  ======")

	if done {
		fmt.Println("\n>> Program finished in", elapsed, " <<")
	}

	fmt.Println()
}
