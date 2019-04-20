package problems

import (
	"errors"
	"fmt"
	"strconv"
)

// LIST ...
var LIST = map[string]Problem{
	"nthprimefraction":      CreateNPF(),
	"1019.nextgreaternode":  CreateNGN(),
	"823.binarytreefactors": CreateBTF(),
	"486.predictwinner":     CreatePW(),
	"1024.vidstitching":     CreateVS(),
	"801.minswapinc":        CreateMSI(),
}

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

	default:
		return nil, "", errors.New(fmt.Sprint("unable to find the problem: ", problem))
	}

	return p, t, nil
}
