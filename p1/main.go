package p1

import (
	"fmt"
	s "go-problems/shared"
)

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
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)

	fmt.Println("Solving problem:", title)

	return p
}
