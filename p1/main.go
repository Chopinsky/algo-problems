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
	case 1039:
		t = "Min Score"
		p = CreateMSTP()

	case 1172:
		t = "Dinner Plate Stacks"
		p = CreateDPS()

	case 1235:
		t = "Max Profit in Job Scheduling"
		p = CreateMPJS()

	case 1240:
		t = "Tiling Rectangle With The Fewest Squares"
		p = CreateTRWTFS()

	case 1255:
		t = "Max Score Words Formed By Letters"
		p = CreateMSWFBL()

	case 1267:
		t = "Server Networks"
		p = CreateSN()

	case 1307:
		t = "Verbal Arith Puzzle"
		p = CreateVAP()

	case 1311:
		t = "Get Watched Videos by Friends"
		p = CreateGWV()

	case 1316:
		t = "Distinct Echo Substrings"
		p = CreateDES()

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

	case 1420:
		t = "Build Array Where You can Find The Maximum Exactly K Comparisons"
		p = CreateBAFMEKC()

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

	case 1475:
		t = "Final Prices with a Special Discount in a Shop"
		p = CreateFPD()

	case 1477:
		t = "Find 2 Non-Overlapping Subarrays Each With Target Sum"
		p = CreateFNS()

	case 1483:
		t = "Kth Ancestor of a Tree Node"
		p = CreateKAT()

	case 1488:
		t = "Avoid Flood in the City"
		p = CreateAFC()

	case 1489:
		t = "Find Critical and Pseudo-Critical Edges in a MST"
		p = CreateFCEMST()

	case 1493:
		t = "Longest Subarray of 1's After Deleting One Element"
		p = CreateLSADOE()

	case 1494:
		t = "Parallel Courses II"
		p = CreatePCII()

	case 1499:
		t = "Max Value Of Equation"
		p = CreateMVE()

	case 1505:
		t = "Minimum Possible Integer After At Most K Adjacent Swaps"
		p = CreateMPI()

	case 1508:
		t = "Range Sum of Sorted Subarray Sums"
		p = CreateRSSS()

	case 1520:
		t = "Max Number of Non-Overlapping Substring"
		p = CreateMNNS()

	case 1524:
		t = "Number of Sub-Arrays With Odd Sum"
		p = CreateNSOS()

	case 1530:
		t = "Number of Good Leaf Nodes Pairs"
		p = CreateNGLNP()

	case 1531:
		t = "String Compression II"
		p = CreateSCII()

	case 1537:
		t = "Get Max Score"
		p = CreateGMS()

	case 1542:
		t = "Find Longest Awesome Substring"
		p = CreateFLS()

	case 1553:
		t = "Min Number of Days to Eat N Oranges"
		p = CreateMNDENO()

	case 1563:
		t = "Stone Game V"
		p = CreateSGV()

	case 1558:
		t = "Min Number of Function Calls to Make Target Array"
		p = CreateMNFCMTA()

	case 1573:
		t = "Number of Ways to Split a String"
		p = CreateNWSS()

	case 1579:
		t = "Remove Max Number of Edges to Keep Graph Fully Traversable"
		p = CreateRMNEKGC()

	case 1585:
		t = "Check If String Is Transformable With Substring Sort Operations"
		p = CreateCISITWS()

	case 1593:
		t = "Split a String Into the Max Number of Unique Substring"
		p = CreateSSMUS()

	case 1595:
		t = "Min Cost to Connect Two Group of Points"
		p = CreateMCTCTGP()

	case 1606:
		t = "Find Servers That Handled Most Number of Requests"
		p = CreateFBS()

	case 1610:
		t = "Max Number of Visible Points"
		p = CreateMNVP()

	case 1616:
		t = "Spint Two Strings to Make Palindrome"
		p = CreateSTSMP()

	case 1617:
		t = "Count Subtrees With Max Distance Between Cities"
		p = CreateCSWMD()

	case 1621:
		t = "Number of Sets of K Non-Overlapping Line Segments"
		p = CreateNSOKNOLS()

	case 1631:
		t = "Path with Minimum Effort"
		p = CreatePME()

	case 1642:
		t = "Furthest Building You Can Reach"
		p = CreateFBYCR()

	case 1648:
		t = "Sell Diminishing Valued Colored Balls"
		p = CreateSDVCB()

	case 1655:
		t = "Distribute Repeating Integers"
		p = CreateDPI()

	case 1659:
		t = "Maximum Grid Happiness"
		p = CreateMGH()
	}

	return t, p
}

// CreateProblem ...
func CreateProblem(num int) s.Problem {
	title, p := findProblem(num)
	fmt.Println("Solving problem:", title)

	return p
}

func min(a, b int) int {
	if b >= a {
		return a
	}

	return b
}

func max(a, b int) int {
	if b >= a {
		return b
	}

	return a
}
