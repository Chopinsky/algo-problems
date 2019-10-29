package problems

import (
	"strconv"

	p1 "./1-999"
	p2 "./1000-1999"
	i "./interface"
)

// Create ...
func Create(problem string) (i.Problem, string, error) {
	num, err := strconv.Atoi(problem)
	if err != nil {
		return nil, "", err
	}

	var p i.Problem
	var t string

	if num < 1000 {
		return p1.MakeProblemSet(num)
	} else if num < 2000 {
		return p2.MakeProblemSet(num)
	}

	return p, t, nil
}
