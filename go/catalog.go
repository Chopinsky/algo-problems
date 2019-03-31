package main

import (
	"fmt"
	"strings"

	problems "./Problems"
)

// LIST ...
var LIST = []string{
	"nthprimefraction",
}

// Problem ...
type Problem interface {
	Run()
}

// Execute ...
func Execute(problem string, test int) {
	var p Problem
	var target string

	for _, candidate := range LIST {
		if len(problem) > len(candidate) {
			continue
		}

		if strings.HasPrefix(candidate, problem) {
			Debug(
				"Matched with problem: \""+candidate+"\"\n",
				0,
			)

			target = candidate
			break
		}
	}

	if len(target) == 0 {
		fmt.Printf("Unable to match the correct problem for %s to run...\n", problem)
		return
	}

	switch target {
	case "nthprimefraction":
		p = problems.MakeNPF(test)

	default:
		fmt.Printf("Unable to match the correct problem for %s to run...\n", problem)

	}

	p.Run()
}
