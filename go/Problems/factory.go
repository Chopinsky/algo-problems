package problems

import (
	"errors"
	"fmt"
	"strconv"

	p1 "./1-999"
	p2 "./1000-1999"
)

// Problem ...m
type Problem interface {
	Run()
	Build(int)
}

// Create ...
func Create(problem string) (Problem, string, error) {
	num, err := strconv.Atoi(problem)
	if err != nil {
		return nil, "", err
	}

	var p Problem
	var t string

	switch num {
	case 801:
		t = "Min Swap to Increase"
		p = p1.CreateMSI()

	case 1024:
		t = "Video Stitching"
		p = p2.CreateVS()

	case 486:
		t = "Predict Winner"
		p = p1.CreatePW()

	case 823:
		t = "Binary Tree Factors"
		p = p1.CreateBTF()

	case 1019:
		t = "Next Greater Node"
		p = p2.CreateNGN()

	case 818:
		t = "Race Car"
		p = p1.CreateRC()

	case 786:
		t = "Nth Prime Fraction"
		p = p1.CreateNPF()

	case 417:
		t = "Pacific-Atlantic Water Flow"
		p = p1.CreateWF()

	case 817:
		t = "Linked-List Components"
		p = p1.CreateLLC()

	case 815:
		t = "Bus Routes"
		p = p1.CreateBR()

	case 813:
		t = "Largest Sum of Averages"
		p = p1.CreateLSA()

	case 450:
		t = "Delete Node in BST"
		p = p1.CreateDN()

	case 560:
		t = "Sub-Array Sum"
		p = p1.CreateSAS()

	case 803:
		t = "Bricks Falling When Hit"
		p = p1.CreateBFH()

	case 802:
		t = "Find Eventual Safe States"
		p = p1.CreateESS()

	case 799:
		t = "Champagne Tower"
		p = p1.CreateCT()

	case 792:
		t = "Number of Matching Subsequences"
		p = p1.CreateNMS()

	case 790:
		t = "Domino and Tromino"
		p = p1.CreateDAT()

	case 787:
		t = "Cheapeast Flights Connecting K Stops"
		p = p1.CreateCFS()

	case 784:
		t = "Letter Case Permutation"
		p = p1.CreateLCP()

	case 773:
		t = "Sliding Puzzle"
		p = p1.CreateSP()

	case 636:
		t = "Exclusive Time of Functions"
		p = p1.CreateETF()

	case 464:
		t = "Can I Win the 100-Game?"
		p = p1.CreateOHG()

	case 769:
		t = "Max Chunk to Make Sorted"
		p = p1.CreateMCS()

	case 282:
		t = "Expression Add Operator"
		p = p1.CreateEAO()

	case 1043:
		t = "Partition Array for Maximum Sum"
		p = p2.CreatePAMS()

	case 480:
		t = "Sliding Window Median"
		p = p1.CreateSWM()

	case 763:
		t = "Partition Labels"
		p = p1.CreatePL()

	case 239:
		t = "Sliding Window Max"
		p = p1.CreateSWMAX()

	case 69:
		t = "Square Root"
		p = p1.CreateSQRT()

	case 494:
		t = "Target Sum"
		p = p1.CreateTS()

	case 759:
		t = "Employee Free Time"
		p = p1.CreateEFT()

	case 264:
		t = "Ugly Number II"
		p = p1.CreateUN2()

	case 621:
		t = "Task Scheduler"
		p = p1.CreateTSE()

	case 755:
		t = "Pour Water"
		p = p1.CreatePWT()

	case 309:
		t = "Best Time to Buy and Sell Stocks"
		p = p1.CreateBTTS()

	case 315:
		t = "Count Smaller Numbers Than Self"
		p = p1.CreateCSN()

	case 322:
		t = "Coin Change"
		p = p1.CreateCCHG()

	case 754:
		t = "Reach A Number"
		p = p1.CreateRAN()

	case 652:
		t = "Find Duplicate Subtrees"
		p = p1.CreateFDS()

	case 1092:
		t = "Shortest Common Super-Sequence"
		p = p2.CreateSCSS()

	case 416:
		t = "Partition Equal Subset Sum"
		p = p1.CreatePESS()

	case 753:
		t = "Cracking The Safe"
		p = p1.CreateCS()

	case 752:
		t = "Open The Lock"
		p = p1.CreateOTL()

	case 17:
		t = "Letter Combo of a Phone Number"
		p = p1.CreateLC()

	case 171:
		t = "Best Time to Buy and Sell Stocks"
		p = p1.CreateBTBSS()

	case 301:
		t = "Remove Invalid Parentheses"
		p = p1.CreateRIP()

	case 23:
		t = "Merge Sorted Lists"
		p = p1.CreateMSL()

	case 748:
		t = "Shortest Completing Word"
		p = p1.CreateSCW()

	case 1105:
		t = "Filling Bookcase Shelf"
		p = p2.CreateFBS()

	case 1106:
		t = "Parsing Boolean Expression"
		p = p2.CreatePBE()

	case 391:
		t = "Perfect Rectangle"
		p = p1.CreatePR()

	case 746:
		t = "Min Cost To Climb Stairs"
		p = p1.CreateMCC()

	case 749:
		t = "Contains Virus"
		p = p1.CreateCV()

	case 377:
		t = "Combo Sum 4"
		p = p1.CreateCS4()

	case 540:
		t = "Single Element in Sorted Array"
		p = p1.CreateSE()

	case 1124:
		t = "Longest Well-Performing Interval"
		p = p2.CreateLPI()

	case 1125:
		t = "Smallest Sufficient Team"
		p = p2.CreateSST()

	case 477:
		t = "Total Hamming Distance"
		p = p1.CreateTHD()

	case 1129:
		t = "Shortest Path with Alternative colors"
		p = p2.CreateSPC()

	case 1140:
		t = "Stone Game II"
		p = p2.CreateSGII()

	case 1145:
		t = "Binary Tree Coloring"
		p = p2.CreateBTC()

	case 1110:
		t = "DeleteNodesAndReturnForest"
		p = p2.CreateDNRF()

	case 1155:
		t = "Num of Dice Rools with Target Sum"
		p = p2.CreateNDR()

	case 212:
		t = "Word Search II"
		p = p1.CreateWSII()

	default:
		return nil, "", errors.New(fmt.Sprint("unable to find the problem: ", problem))
	}

	return p, t, nil
}
