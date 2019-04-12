package problems

import (
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

	default:
		t = "Nth Prime Fraction"
		p = CreateNPF()
	}

	return p, t, nil
}
