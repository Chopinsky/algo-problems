package problems

import (
	"fmt"

	d "../Utils"
)

// DAT ...
type DAT struct {
	source int
	output int
}

// CreateDAT ...
func CreateDAT() *DAT {
	return &DAT{}
}

// Build ...
func (p *DAT) Build(test int) {
	switch test {
	default:
		p.source = 3
		p.output = 5

	}
}

// Run ...
func (p *DAT) Run() {
	fmt.Println("Calculated result: ", dnt(p.source))
	fmt.Println("Expected result: ", p.output)
}

func dnt(n int) int {
	if n <= 0 {
		return 0
	}

	if n == 1 {
		return 1
	}

	if n == 2 {
		return 2
	}

	// n >= 3
	x0 := 1 // previous+2 col
	y0 := 2 // previous+1 col, only 1 more than x0
	y1 := 1 // previous+1 col w/ 1 tile taken from previous patterns
	var temp int

	for i := 3; i <= n; i++ {
		// x0 existing styles with 1 unique new, plus y0 existing styles with 1 more unique new,
		// plus y1 existing styles with Lll-shape tile at the end, L can be facing up or down, so times 2.
		temp = x0 + y0 + 2*y1

		// y1 existing styles and 1 more unique domino tile, plus x0 existing styles with 1 more
		// L-shape tile. Updating the index at the same time -- use new y1 to replace old y1.
		y1 += x0

		// update x0 and y0 indices -- moving along
		x0 = y0
		y0 = temp

		d.Debug(fmt.Sprintln("Column", i, "->", x0, y0, y1), 0)
	}

	return y0
}
