package p0

import (
	"fmt"
	s "go-problems/shared"
)

func findProblem(num int) (string, s.Problem) {
	var t string
	var p s.Problem

	switch num {
	case 685:
		t = "Redundant Connection II"
		p = CreateRCII()
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)

	fmt.Println("Solving problem:", title)

	return p
}
