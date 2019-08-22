package problems

import (
	"fmt"

	d "../../Utils"
)

// DNRF ...
type DNRF struct {
	source    []int
	del       []int
	output    [][]int
	testCount int
}

// CreateDNRF ...
func CreateDNRF() *DNRF {
	return &DNRF{}
}

// Build ...
func (p *DNRF) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = []int{1, 2, 3, 4, 5, 6, 7}
		p.del = []int{3, 5}
		p.output = [][]int{
			{1, 2, -1, 4},
			{6},
			{7},
		}

	}
}

// ResetGlobals ...
func (p *DNRF) ResetGlobals() {
}

// Run ...
func (p *DNRF) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcDNRF(p.source, p.del), p.output)
			} else {
				calcDNRF(p.source, p.del)
			}
		}
	}
}

func buildDNRF(del []int) map[int]bool {
	list := make(map[int]bool, len(del))

	for _, val := range del {
		list[val] = true
	}

	return list
}

func calcDNRF(tree, del []int) [][]int {
	res := [][]int{}
	size := len(tree)

	list := buildDNRF(del)
	roots := make([]int, 0, size)
	roots = append(roots, 0)

	var currRoot int
	var newTree []int

	for len(roots) > 0 {
		currRoot, roots = roots[0], roots[1:]

		newTree, roots = iterTree(list, tree, make([]int, 0, size), roots, currRoot, size)
		newTree = trimTree(newTree)

		if len(newTree) > 0 {
			res = append(res, newTree)
		}
	}

	return res
}

func iterTree(list map[int]bool, base, tree, roots []int, root, size int) ([]int, []int) {
	level := []int{root}
	var nextRoot int

	for len(level) > 0 {
		nextLevel := make([]int, 0, 2*len(level))

		for i := 0; i < len(level); i++ {
			nextRoot = level[i]
			tree, roots, nextLevel = updateTree(list, base, tree, roots, nextLevel, nextRoot, size)
		}

		level = nextLevel
	}

	return tree, roots
}

func updateTree(list map[int]bool, base, tree, roots, level []int, root, size int) ([]int, []int, []int) {
	nextLeftRoot, nextRightRoot := 2*root+1, 2*root+2

	if list[base[root]] {
		if nextLeftRoot < size {
			roots = append(roots, nextLeftRoot)
		}

		if nextRightRoot < size {
			roots = append(roots, nextRightRoot)
		}

		tree = append(tree, -1)
	} else {
		if nextLeftRoot < size {
			level = append(level, nextLeftRoot)
		}

		if nextRightRoot < size {
			level = append(level, nextRightRoot)
		}

		tree = append(tree, base[root])
	}

	return tree, roots, level
}

func trimTree(tree []int) []int {
	i := len(tree) - 1
	for i >= 0 {
		if tree[i] > -1 {
			break
		}

		i--
	}

	return tree[:i+1]
}
