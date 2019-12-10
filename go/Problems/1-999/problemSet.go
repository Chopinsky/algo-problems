package problems

import (
	"errors"
	"fmt"

	i "../interface"
)

// MakeProblemSet ...
func MakeProblemSet(num int) (i.Problem, string, error) {
	var p i.Problem
	var t string

	switch num {
	case 801:
		t = "Min Swap to Increase"
		p = CreateMSI()

	case 486:
		t = "Predict Winner"
		p = CreatePW()

	case 823:
		t = "Binary Tree Factors"
		p = CreateBTF()

	case 818:
		t = "Race Car"
		p = CreateRC()

	case 786:
		t = "Nth Prime Fraction"
		p = CreateNPF()

	case 417:
		t = "Pacific-Atlantic Water Flow"
		p = CreateWF()

	case 817:
		t = "Linked-List Components"
		p = CreateLLC()

	case 815:
		t = "Bus Routes"
		p = CreateBR()

	case 813:
		t = "Largest Sum of Averages"
		p = CreateLSA()

	case 450:
		t = "Delete Node in BST"
		p = CreateDN()

	case 560:
		t = "Sub-Array Sum"
		p = CreateSAS()

	case 803:
		t = "Bricks Falling When Hit"
		p = CreateBFH()

	case 802:
		t = "Find Eventual Safe States"
		p = CreateESS()

	case 799:
		t = "Champagne Tower"
		p = CreateCT()

	case 792:
		t = "Number of Matching Subsequences"
		p = CreateNMS()

	case 790:
		t = "Domino and Tromino"
		p = CreateDAT()

	case 787:
		t = "Cheapeast Flights Connecting K Stops"
		p = CreateCFS()

	case 784:
		t = "Letter Case Permutation"
		p = CreateLCP()

	case 773:
		t = "Sliding Puzzle"
		p = CreateSP()

	case 636:
		t = "Exclusive Time of Functions"
		p = CreateETF()

	case 464:
		t = "Can I Win the 100-Game?"
		p = CreateOHG()

	case 769:
		t = "Max Chunk to Make Sorted"
		p = CreateMCS()

	case 282:
		t = "Expression Add Operator"
		p = CreateEAO()

	case 480:
		t = "Sliding Window Median"
		p = CreateSWM()

	case 763:
		t = "Partition Labels"
		p = CreatePL()

	case 239:
		t = "Sliding Window Max"
		p = CreateSWMAX()

	case 69:
		t = "Square Root"
		p = CreateSQRT()

	case 494:
		t = "Target Sum"
		p = CreateTS()

	case 759:
		t = "Employee Free Time"
		p = CreateEFT()

	case 264:
		t = "Ugly Number II"
		p = CreateUN2()

	case 621:
		t = "Task Scheduler"
		p = CreateTSE()

	case 755:
		t = "Pour Water"
		p = CreatePWT()

	case 309:
		t = "Best Time to Buy and Sell Stocks"
		p = CreateBTTS()

	case 315:
		t = "Count Smaller Numbers Than Self"
		p = CreateCSN()

	case 322:
		t = "Coin Change"
		p = CreateCCHG()

	case 754:
		t = "Reach A Number"
		p = CreateRAN()

	case 652:
		t = "Find Duplicate Subtrees"
		p = CreateFDS()

	case 416:
		t = "Partition Equal Subset Sum"
		p = CreatePESS()

	case 753:
		t = "Cracking The Safe"
		p = CreateCS()

	case 752:
		t = "Open The Lock"
		p = CreateOTL()

	case 17:
		t = "Letter Combo of a Phone Number"
		p = CreateLC()

	case 171:
		t = "Best Time to Buy and Sell Stocks"
		p = CreateBTBSS()

	case 301:
		t = "Remove Invalid Parentheses"
		p = CreateRIP()

	case 23:
		t = "Merge Sorted Lists"
		p = CreateMSL()

	case 748:
		t = "Shortest Completing Word"
		p = CreateSCW()

	case 391:
		t = "Perfect Rectangle"
		p = CreatePR()

	case 746:
		t = "Min Cost To Climb Stairs"
		p = CreateMCC()

	case 749:
		t = "Contains Virus"
		p = CreateCV()

	case 377:
		t = "Combo Sum 4"
		p = CreateCS4()

	case 540:
		t = "Single Element in Sorted Array"
		p = CreateSE()

	case 477:
		t = "Total Hamming Distance"
		p = CreateTHD()

	case 212:
		t = "Word Search II"
		p = CreateWSII()

	case 116:
		t = "Populate Next Right Pointer"
		p = CreateNRP()

	case 210:
		t = "Course Schedule II"
		p = CreateCSII()

	case 130:
		t = "Surrounded Regions"
		p = CreateSR()

	case 132:
		t = "Palindrome Patition II"
		p = CreatePPII()

	default:
		return nil, "", errors.New(fmt.Sprint("unable to find the problem: ", num))
	}

	return p, t, nil
}
