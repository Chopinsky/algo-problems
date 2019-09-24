package problems

import (
	"fmt"

	d "../../Utils"
)

// UNIII ...
type UNIII struct {
	source    []int
	nth       int
	output    int
	testCount int
}

// CreateUNIII ...
func CreateUNIII() *UNIII {
	return &UNIII{}
}

// Build ...
func (p *UNIII) Build(test int) {
	p.ResetGlobals()
	p.testCount = 4

	switch test {
	case 1:
		p.source = []int{2, 3, 4}
		p.nth = 4
		p.output = 6

	case 2:
		p.source = []int{2, 11, 13}
		p.nth = 5
		p.output = 10

	case 3:
		p.source = []int{2, 217983653, 336916467}
		p.nth = 1000000000
		p.output = 1999999972

	default:
		p.source = []int{2, 3, 5}
		p.nth = 3
		p.output = 4

	}
}

// ResetGlobals ...
func (p *UNIII) ResetGlobals() {
}

// Run ...
func (p *UNIII) Run() {
	for j := 0; j < 10; j++ {
		fmt.Println("============ Running Trial: ", j, " ============")

		for i := 0; i < p.testCount; i++ {
			p.Build(i)

			if j == 9 {
				fmt.Println("\nTest case: ", i, ":")
				d.Output(calcUNIII(p.source, p.nth), p.output)
			} else {
				calcUNIII(p.source, p.nth)
			}
		}
	}
}

func calcUNIII(src []int, nth int) int {
	// the 1st number will meet the needs
	if src[0]*nth <= src[1] {
		return src[0] * nth
	}

	if src[1]%src[0] == 0 {
		src[1] = 0
	}

	if src[2]%src[0] == 0 || (src[1] != 0 && src[2]%src[1] == 0) {
		src[2] = 0
	}

	upper, lower := nth, 1

	var a0, b0, c0, total int
	a0 = (upper + lower) / 2

	if src[1] != 0 {
		b0 = src[0] * a0 / src[1]
	}

	if src[2] != 0 {
		c0 = src[0] * a0 / src[2]
	}

	total = a0 + b0 + c0

	for total != nth {
		if total > nth {
			upper = a0 - 1
		} else {
			lower = a0 + 1
		}

		if upper <= lower {
			break
		}

		a0 = (upper + lower) / 2

		if src[1] != 0 {
			b0 = src[0] * a0 / src[1]
		}

		if src[2] != 0 {
			c0 = src[0] * a0 / src[2]
		}

		total = a0 + b0 + c0

		if d.DEBUG {
			fmt.Println(a0, b0, c0, total)
		}
	}

	max1, max2, max3 := src[0]*a0, src[1]*b0, src[2]*c0

	if d.DEBUG {
		fmt.Println("==========")
		fmt.Println(a0, b0, c0)
		fmt.Println(max1, max2, max3)
	}

	if max1 >= max2 && max1 >= max3 {
		return max1
	}

	if max2 >= max1 && max2 >= max3 {
		return max2
	}

	return max3
}
