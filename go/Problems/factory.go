package problems

import (
	"errors"
	"fmt"
	"strconv"
)

var dir = []int{-1, 0, 1, 0, -1}
var empty = struct{}{}

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
		p = CreateMSI()

	case 1024:
		t = "Video Stitching"
		p = CreateVS()

	case 486:
		t = "Predict Winner"
		p = CreatePW()

	case 823:
		t = "Binary Tree Factors"
		p = CreateBTF()

	case 1019:
		t = "Next Greater Node"
		p = CreateNGN()

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

	default:
		return nil, "", errors.New(fmt.Sprint("unable to find the problem: ", problem))
	}

	return p, t, nil
}
