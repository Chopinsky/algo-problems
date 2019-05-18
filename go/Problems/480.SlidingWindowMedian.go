package problems

import (
	"fmt"
	"math"
	"sort"

	d "../Utils"
)

// SWM ...
type SWM struct {
	source []int
	size   int
	output []float32
}

// CreateSWM ...
func CreateSWM() *SWM {
	return &SWM{}
}

// Build ...
func (p *SWM) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 3, -1, -3, 5, 3, 7, 6, 1, 0, 9}
		p.size = 2
		p.output = []float32{2, 1, -2, 1, 4, 5, 6.5, 3.5, 0.5, 4.5}

	default:
		p.source = []int{1, 3, -1, -3, 5, 3, 7, 6}
		p.size = 3
		p.output = []float32{1, -1, -1, 3, 5, 6}

	}
}

// Run ...
func (p *SWM) Run() {
	window, median := slide(p.source[:p.size], p.size, math.MinInt32, math.MinInt32)
	result := []float32{median}

	for i := p.size; i < len(p.source); i++ {
		if p.source[i-p.size] != p.source[i] {
			window, median = slide(window, p.size, p.source[i-p.size], p.source[i])
		}

		result = append(result, median)
	}

	d.Output(result, p.output)
}

func slide(ary []int, length, oldVal, newVal int) ([]int, float32) {
	if length == 1 {
		return nil, float32(newVal)
	}

	if oldVal == math.MinInt32 && oldVal == newVal {
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

	var median float32
	index := length / 2

	if length%2 == 0 {
		// average
		median = float32(ary[index-1]+ary[index]) / 2.0
	} else {
		// median
		median = float32(ary[index])
	}

	d.Debug(fmt.Sprintln(" -> ", ary, median), 0)

	return ary, median
}

func fwdInsert(src []int, start, newVal int) []int {
	for i := start; i < len(src); i++ {
		if newVal > src[i] {
			src[i-1] = src[i]
			if i == len(src)-1 {
				src[i] = newVal
			}
		} else {
			src[i-1] = newVal
			break
		}
	}

	return src
}

func bwdInsert(src []int, start, newVal int) []int {
	for i := start; i >= 0; i-- {
		if newVal < src[i] {
			src[i+1] = src[i]
			if i == 0 {
				src[0] = newVal
			}
		} else {
			src[i+1] = newVal
			break
		}
	}

	return src
}
