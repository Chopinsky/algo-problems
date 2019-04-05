package problems

import (
	"fmt"
	"strings"

	d "../Debug"
)

// LIST ...
var LIST = map[string]Problem{
	"nthprimefraction":  CreateNPF(),
	"nextgreaternode":   CreateNGN(),
	"binarytreefactors": CreateBTF(),
}

// Problem ...m
type Problem interface {
	Run()
	Build(int)
}

// Create ...
func Create(problem string) (Problem, error) {
	for k, v := range LIST {
		if len(problem) > len(k) {
			continue
		}

		if strings.HasPrefix(k, problem) {
			d.Debug("Target found: "+k+"\n", 0)
			return v, nil
		}
	}

	return nil, fmt.Errorf("Unable to match the correct problem for %s to run", problem)
}
