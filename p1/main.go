package p1

import (
	"fmt"

	s "go-problems/shared"
)

var count = 0
var mod = 1000000007

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

	case 1368:
		t = "Min Cost to Make at Least One Valid Path in a Grid"
		p = CreateMCMLP()

	case 1373:
		t = "Maximum Sum BST in Binary Tree"
		p = CreateMSB()

	case 1377:
		t = "Frog Position After T Seconds"
		p = CreateFPS()

	case 1371:
		t = "Find the Longest Substring Containing Vowels in Even Counts"
		p = CreateFLSCV()

	case 1382:
		t = "Balance a Binary Search Tree"
		p = CreateBBST()

	case 1395:
		t = "Count Number of Teams"
		p = CreateCNT()

	case 1406:
		t = "Stone Game III"
		p = CreateSGIII()

	case 1409:
		t = "Queries on a Permutation with Key"
		p = CreateQPK()

	case 1411:
		t = "Number of Ways to Paint N x 3 Grid"
		p = CreateNWPG()

	case 1416:
		t = "Restore The Array"
		p = CreateRA()

	case 1425:
		t = "Constrained Subset Sum"
		p = CreateCSS()

	case 1424:
		t = "Diagnoal Traverse II"
		p = CreateDTII()

	case 1438:
		t = "Lonngest Subarray with Absolute Diff Less Than the Limit"
		p = CreateLSWD()

	case 1442:
		t = "Count Triplets Forming Two Arrays of Equal XOR"
		p = CreateCTTA()

	case 1443:
		t = "Min Time to Collect All Apples in Tree"
		p = CreateMTCA()

	case 1444:
		t = "Number of Ways of Cutting a Pizza"
		p = CreateNWCP()

	case 1449:
		t = "Form Largest Integer With Digits That Add Up to Target"
		p = CreateFLI()

	case 1457:
		t = "Pseud-Palindromic Paths in a Binary Tree"
		p = CreatePPPBT()

	case 1458:
		t = "Max Dot Product of Two Subsequences"
		p = CreateMDPTS()

	case 1463:
		t = "Cherry Pick II"
		p = CreateCPII()

	case 1467:
		t = "Probability of a Two Boxes Having the Same Number of Distinct Balls"
		p = CreatePTBSN()

	case 1473:
		t = "Paint House III"
		p = CreatePHIII()
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)

	fmt.Println("Solving problem:", title)

	return p
}
