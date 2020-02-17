package problems

import "fmt"

// MCS ...
type MCS struct {
	source []int
	output int
}

// CreateMCS ...
func CreateMCS() *MCS {
	return &MCS{}
}

// Build ...
func (p *MCS) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 0, 2, 3, 4}
		p.output = 4

	case 2:
		p.source = []int{1, 2, 3, 0, 5, 4}
		p.output = 2

	default:
		p.source = []int{4, 3, 2, 1, 0}
		p.output = 1

	}
}

// Run ...
func (p *MCS) Run() {
	fmt.Println("Caculated result: ", p.count())
	fmt.Println("Expected result: ", p.output)
}

func (p *MCS) count() int {
	num := 0
	end := -1
	last := len(p.source) - 1

	for i, val := range p.source {
		if val > end {
			// if the val should be the last element, the remainder chunk has to be in the
			// same sub-array
			if val == last {
				num++
				break
			}

			// otherwise, update the location of the end of the current presumed segment
			end = val
		}

		if i == end {
			// we're at the end of the segment and all elements inside can be sorted to
			// its rightful location now, reset the end as well
			num++
			end = -1
		}
	}

	return num
}
