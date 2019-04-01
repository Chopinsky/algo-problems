package problems

import (
	"fmt"
	"strings"

	d "../Debug"
)

// LIST ...
var LIST = []string{
	"nthprimefraction",
	"nextgreaternode",
}

// Problem ...
type Problem interface {
	Run()
	Build(int)
}

// Create ...
func Create(problem string) (Problem, error) {
	var target string
	var p Problem

	for _, candidate := range LIST {
		if len(problem) > len(candidate) {
			continue
		}

		if strings.HasPrefix(candidate, problem) {
			target = candidate
			break
		}
	}

	d.Debug("Target: "+target+"\n", 0)

	if len(target) == 0 {
		return nil, fmt.Errorf("Failed to interpret the target problem: %s", problem)
	}

	switch target {
	case "nthprimefraction":
		p = CreateNPF()

	case "nextgreaternode":
		p = CreateNGN()

	default:
		return nil, fmt.Errorf("Unable to match the correct problem for %s to run", problem)

	}

	return p, nil
}
