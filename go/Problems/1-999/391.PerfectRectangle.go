package problems

import (
	"fmt"
	"strconv"

	d "../../Utils"
)

// PR ...
type PR struct {
	source    [][]int
	output    bool
	testCount int
}

// CreatePR ...
func CreatePR() *PR {
	return &PR{}
}

// Build ...
func (p *PR) Build(test int) {
	p.ResetGlobals()
	p.testCount = 1

	switch test {
	default:
		p.source = [][]int{
			{1, 1, 3, 3},
			{3, 1, 4, 2},
			{3, 2, 4, 4},
			{1, 3, 2, 4},
			{2, 3, 3, 4},
		}
		p.output = true

	}
}

// ResetGlobals ...
func (p *PR) ResetGlobals() {
}

// Run ...
func (p *PR) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(buildShape(p.source), p.output)
			} else {
				buildShape(p.source)
			}
		}

		fmt.Println()
	}
}

func buildShape(src [][]int) bool {
	shape := make(map[string][]int, 2*len(src))

	for i := range src {
		// bottom-left
		updateShape(shape, []int{src[i][0], src[i][1]})

		// bottom-right
		updateShape(shape, []int{src[i][2], src[i][1]})

		// top-left
		updateShape(shape, []int{src[i][0], src[i][3]})

		// top-right
		updateShape(shape, []int{src[i][2], src[i][3]})
	}

	return testShape(shape)
}

func testShape(shape map[string][]int) bool {
	d.Debug(shape, 0)

	if len(shape) != 4 {
		return false
	}

	x, y := make(map[int]int, 2), make(map[int]int, 2)
	for _, v := range shape {
		x[v[0]]++
		y[v[1]]++
	}

	if len(x) != 2 || len(y) != 2 {
		return false
	}

	for _, v := range x {
		if v != 2 {
			return false
		}
	}

	for _, v := range y {
		if v != 2 {
			return false
		}
	}

	return true
}

func updateShape(shape map[string][]int, src []int) map[string][]int {
	key := strconv.Itoa(src[0]) + "," + strconv.Itoa(src[1])
	if _, ok := shape[key]; ok {
		delete(shape, key)
	} else {
		shape[key] = src
	}

	return shape
}
