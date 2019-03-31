package problems

import (
	"fmt"
	"strconv"
)

// NPF ...
type NPF struct {
	source []int
	kth    int
}

// MakeNPF ...
func MakeNPF(test int) *NPF {
	return &NPF{
		source: []int{1, 2, 3, 5},
		kth:    2,
	}
}

// Run ...
func (p NPF) Run() {
	fmt.Println("Running problem: Nth Prime Fraction")
	fmt.Println("Source len: " + strconv.Itoa(len(p.source)) + "\nKth: " + strconv.Itoa(p.kth))
}
