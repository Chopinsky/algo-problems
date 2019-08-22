package problems

import (
	"fmt"
	"math"
	"sort"

	d "../../Utils"
)

// SWMAX ...
type SWMAX struct {
	source []int
	size   int
	output []int
}

// CreateSWMAX ...
func CreateSWMAX() *SWMAX {
	return &SWMAX{}
}

// Build ...
func (p *SWMAX) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 3, -1, -3, 5, 3, 7, 6, 1, 0, 9}
		p.size = 2
		p.output = []int{3, 3, -1, 5, 5, 7, 7, 6, 1, 9}

	default:
		p.source = []int{1, 3, -1, -3, 5, 3, 6, 7}
		p.size = 3
		p.output = []int{3, 3, 5, 5, 6, 7}

	}
}

// Run ...
func (p *SWMAX) Run() {
	window, median := slideForMax(p.source[:p.size], p.size, math.MinInt32, math.MinInt32)
	result := []int{median}

	for i := p.size; i < len(p.source); i++ {
		if p.source[i-p.size] != p.source[i] {
			window, median = slideForMax(window, p.size, p.source[i-p.size], p.source[i])
		}

		result = append(result, median)
	}

	d.Output(result, p.output)
}

func slideForMax(ary []int, length, oldVal, newVal int) ([]int, int) {
	if length == 1 {
		return nil, int(newVal)
	}

	if oldVal == math.MinInt32 && newVal == math.MinInt32 {
		// init
		ary = append([]int(nil), ary...)
		sort.Ints(ary)
	} else {
		if idx, ok := d.BinarySearch(ary, oldVal); ok {
			d.Debug(fmt.Sprintln(ary, oldVal, newVal, idx), 0)

			if idx < length-1 && newVal > ary[idx+1] {
				ary = fwdInsert(ary, idx+1, newVal)
			} else if idx > 0 && newVal < ary[idx-1] {
				ary = bwdInsert(ary, idx-1, newVal)
			} else {
				ary[idx] = newVal
			}
		} else {
			fmt.Println("Failed to find the old value: {", oldVal, "} from array: ", ary)
		}
	}

	d.Debug(fmt.Sprintln(" -> ", ary, ary[length-1]), 0)

	return ary, ary[length-1]
}
