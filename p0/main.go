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

	case 126:
		t = "Word Ladder II"
		p = CreateWLII()

	case 150:
		t = "Evaluate Reverse Polish Notation"
		p = CreateERPN()

	case 207:
		t = "Course Schedule"
		p = CreateCS()

	case 210:
		t = "Course Schedule"
		p = CreateCSII()

	case 247:
		t = "H-Index"
		p = CreateHI()

	case 304:
		t = "Range Sum Query 2D"
		p = CreateRSQ()

	case 341:
		t = "Top K Frequent Element"
		p = CreateTKFE()

	case 393:
		t = "UTF-8 Validation"
		p = CreateUTF8()

	case 685:
		t = "Redundant Connection II"
		p = CreateRCII()

	case 719:
		t = "Kth Smallest Pair Distance"
		p = CreateKSPD()

	case 741:
		t = "Cherry Pick"
		p = CreateCP()

	case 825:
		t = "Friends of Appropriate Ages"
		p = CreateFAA()

	case 935:
		t = "Knight Dialer"
		p = CreateKD()

	case 954:
		t = "Array of Doubled Pairs"
		p = CreateAODP()

	case 996:
		t = "Rotting Oranges"
		p = CreateRO()
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)

	fmt.Println("Solving problem:", title)

	return p
}
