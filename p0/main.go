package p0

import (
	"fmt"

	s "go-problems/shared"
)

func findProblem(num int) (string, s.Problem) {
	var t string
	var p s.Problem

	switch num {
	case 87:
		t = "Scramble String"
		p = CreateSS()

	case 393:
		t = "UTF-8 Validation"
		p = CreateUTF8()

	case 685:
		t = "Redundant Connection II"
		p = CreateRCII()

	case 207:
		t = "Course Schedule"
		p = CreateCS()

	case 935:
		t = "Knight Dialer"
		p = CreateKD()
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)

	fmt.Println("Solving problem:", title)

	return p
}
