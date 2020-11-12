package p0

import (
	"fmt"

	s "go-problems/shared"
)

func findProblem(num int) (string, s.Problem) {
	var t string
	var p s.Problem

	switch num {
	case 33:
		t = "Search In Rotated Sorted Array"
		p = CreateSRSA()

	case 87:
		t = "Scramble String"
		p = CreateSS()

	case 106:
		t = "Construct Binary Tree from Inorder and Postorder"
		p = CreateCBTFIP()

	case 123:
		t = "Best Time to Buy and Sell Stocks III"
		p = CreateBTTBASS()

	case 126:
		t = "Word Ladder II"
		p = CreateWLII()

	case 150:
		t = "Evaluate Reverse Polish Notation"
		p = CreateERPN()

	case 154:
		t = "Find Min In Rotated Sorted Array II"
		p = CreateMRSA()

	case 207:
		t = "Course Schedule"
		p = CreateCS()

	case 210:
		t = "Course Schedule"
		p = CreateCSII()

	case 247:
		t = "H-Index"
		p = CreateHI()

	case 273:
		t = "Integer To English Words"
		p = CreateITEW()

	case 304:
		t = "Range Sum Query 2D"
		p = CreateRSQ()

	case 309:
		t = "Best Time to Buy and Sell Stock with Cooldown"
		p = CreateBTTBSS()

	case 341:
		t = "Top K Frequent Element"
		p = CreateTKFE()

	case 378:
		t = "Kth Smallest Element in a Sorted Matrix"
		p = CreateKSESM()

	case 393:
		t = "UTF-8 Validation"
		p = CreateUTF8()

	case 621:
		t = "Task Schedule"
		p = CreateTS()

	case 685:
		t = "Redundant Connection II"
		p = CreateRCII()

	case 719:
		t = "Kth Smallest Pair Distance"
		p = CreateKSPD()

	case 726:
		t = "Kth Smallest Prime Fraction"
		p = CreateKSPF()

	case 741:
		t = "Cherry Pick"
		p = CreateCP()

	case 743:
		t = "Network Delay Time"
		p = CreateNDT()

	case 778:
		t = "Swim In Rising Water"
		p = CreateSRW()

	case 813:
		t = "Largest Sum Of Averages"
		p = CreateLSOA()

	case 816:
		t = "Ambiguous Coordinates"
		p = CreateAC()

	case 825:
		t = "Friends of Appropriate Ages"
		p = CreateFAA()

	case 851:
		t = "Loud and Rich"
		p = CreateLAR()

	case 887:
		t = "Super Egg Drop"
		p = CreateSED()

	case 879:
		t = "Profitable Schemes"
		p = CreatePS()

	case 902:
		t = "Numbers At Most N Given Digit Set"
		p = CreateNAMNGDS()

	case 935:
		t = "Knight Dialer"
		p = CreateKD()

	case 952:
		t = "Largest Component Size By Common Factor"
		p = CreateLCS()

	case 954:
		t = "Array of Doubled Pairs"
		p = CreateAODP()

	case 975:
		t = "Odd Even Jump"
		p = CreateOEJ()

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
