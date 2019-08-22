package problems

import (
	"fmt"

	d "../../Utils"
)

// SE ...
type SE struct {
	source    []int
	output    int
	testCount int
}

// CreateSE ...
func CreateSE() *SE {
	return &SE{}
}

// Build ...
func (p *SE) Build(test int) {
	p.ResetGlobals()
	p.testCount = 4

	switch test {
	case 1:
		p.source = []int{3, 3, 7, 7, 10, 11, 11}
		p.output = 10

	case 2:
		p.source = []int{1, 1, 2, 2, 3, 3, 5}
		p.output = 5

	case 3:
		p.source = []int{1, 2, 2, 3, 3, 5, 5}
		p.output = 1

	default:
		p.source = []int{1, 1, 2, 3, 3, 4, 4, 8, 8}
		p.output = 2

	}
}

// ResetGlobals ...
func (p *SE) ResetGlobals() {
}

// Run ...
func (p *SE) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(srchSingle(p.source), p.output)
			} else {
				srchSingle(p.source)
			}
		}
	}
}

func srchSingle(src []int) int {
	size := len(src)
	if size == 1 {
		return src[0]
	}

	if size == 3 {
		if src[0] != src[1] {
			return src[0]
		}

		return src[2]
	}

	left, right := 0, size-1
	for left < right {
		// mid is always an even number, since [left, right] shall always have odd number
		// of elements
		mid := (left + right) / 2

		// the middle is the single elem
		if src[mid] != src[mid-1] && src[mid] != src[mid+1] {
			return src[mid]
		}

		if (mid-left)%2 == 1 {
			if src[mid] == src[mid-1] {
				left = mid + 1
			} else {
				right = mid - 1
			}
		} else {
			if src[mid] == src[mid+1] {
				left = mid + 2
			} else {
				right = mid - 2
			}
		}
	}

	return src[left]
}
