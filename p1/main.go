package p1

import (
	"fmt"
	s "go-problems/shared"
)

var count = 0

func findProblem(num int) (string, s.Problem) {
	var t string
	var p s.Problem

	switch num {
	case 1334:
		t = "City With the Smallest Number of Neighbors Within the Threshold"
		p = CreateCSNN()

	case 1335:
		t = "Minimum Difficulty of a Job Schedule"
		p = CreateMDJS()

	case 1343:
		t = "Maximum Product of Splitted Binary Tree"
		p = CreateMPSBT()

	case 1349:
		t = "Maximum Students Taking Exam"
		p = CreateMSTE()

	case 1353:
		t = "Maximum Number of Events That Can Be Attened"
		p = CreateMNE()

	case 1354:
		t = "Construct Target Array with Multiple Sums"
		p = CreateCTA()
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)

	fmt.Println("Solving problem:", title)

	return p
}
