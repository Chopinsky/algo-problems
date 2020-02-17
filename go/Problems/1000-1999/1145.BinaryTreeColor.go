package problems

import (
	"fmt"

	d "../../Utils"
)

// BTC ...
type BTC struct {
	source    []int
	count     int
	first     int
	output    bool
	testCount int
}

// CreateBTC ...
func CreateBTC() *BTC {
	return &BTC{}
}

// Build ...
func (p *BTC) Build(test int) {
	p.testCount = 1

	switch test {
	default:
		p.source = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
		p.count = 11
		p.first = 3
		p.output = true

	}

	p.ResetGlobals(p.count)
}

var treeNodesCount map[int]int

// ResetGlobals ...
func (p *BTC) ResetGlobals(count int) {
	treeNodesCount = make(map[int]int, count)
}

// Run ...
func (p *BTC) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(play(p.source, p.first, p.count), p.output)
			} else {
				play(p.source, p.first, p.count)
			}
		}
	}
}

func countTree(start, size int) int {
	if start >= size {
		return 0
	}

	if val, ok := treeNodesCount[start]; ok {
		return val
	}

	val := 1 + countTree(2*start+1, size) + countTree(2*start+2, size)
	treeNodesCount[start] = val

	return val
}

func play(src []int, x, size int) bool {
	var totalX, totalY int

	// if y take the parent node
	totalX = countTree(x, size)
	totalY = size - totalX
	if totalY > totalX {
		return true
	}

	// if y take the left child node
	totalY = countTree(2*x+1, size)
	totalX = size - totalY
	if totalY > totalX {
		return true
	}

	// if y take the right child node
	totalY = countTree(2*x+2, size)
	totalX = size - totalY
	if totalY > totalX {
		return true
	}

	return false
}
