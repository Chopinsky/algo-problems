package problems

import (
	"fmt"

	d "../../Utils"
)

// EFT ...
type EFT struct {
	source [][][]int
	output [][]int
}

// CreateEFT ...
func CreateEFT() *EFT {
	return &EFT{}
}

// Build ...
func (p *EFT) Build(test int) {
	switch test {
	case 1:
		p.source = [][][]int{
			{{1, 3}, {6, 7}},
			{{2, 4}},
			{{2, 5}, {9, 12}},
		}
		p.output = [][]int{{5, 6}, {7, 9}}

	default:
		p.source = [][][]int{
			{{1, 2}, {5, 6}},
			{{1, 3}},
			{{4, 10}},
		}
		p.output = [][]int{{3, 4}}

	}
}

// Run ...
func (p *EFT) Run() {
	fmt.Println(p.findFreeTime())
}

func (p *EFT) findFreeTime() [][]int {
	result := append([][]int(nil), p.source[0]...)

	for i := 1; i < len(p.source); i++ {
		result = merge(result, p.source[i])
	}

	return invert(result)
}

func merge(src, tgt [][]int) [][]int {
	sSize, tSize := len(src), len(tgt)

	if sSize == 0 {
		return append([][]int(nil), tgt...)
	}

	if tSize == 0 {
		return src
	}

	i, j, idx := 0, 0, -1
	result := [][]int{}
	var curr []int
	var set bool

	// flatten the 2 arries
	for i < sSize || j < tSize {
		if j == tSize || (i < sSize && src[i][0] <= tgt[j][0]) {
			curr, set = src[i], true
			i++
		} else if i == sSize || (j < tSize && src[i][0] > tgt[j][0]) {
			curr, set = tgt[j], true
			j++
		}

		if set {
			// first elem or no overlapping with the last slot in the result
			if idx < 0 || curr[0] > result[idx][1] {
				result = append(result, curr)
				idx++
				continue
			}

			// overlapping found, take the longest finishing hour
			if curr[1] > result[idx][1] {
				result[idx][1] = curr[1]
			}
		}

		curr, set = nil, false
	}

	/*
		idx = 0

		// merging the neighboring slots
		for i := 1; i < size; i++ {
			// no overlapping with the last slot in the result
			if temp[i][0] > result[idx][1] {
				result = append(result, temp[i])
				idx++
				continue
			}

			// overlapping found, take the longest finishing hour
			if temp[i][1] > result[idx][1] {
				result[idx][1] = temp[i][1]
			}
		}
	*/

	d.Debug(fmt.Sprintln("merge result: ", result), 0)

	return result
}

func invert(src [][]int) [][]int {
	if len(src) <= 1 {
		return nil
	}

	size := len(src) - 1
	result := make([][]int, size)

	for i := 0; i < size; i++ {
		result[i] = make([]int, 2)
		result[i][0] = src[i][1]
		result[i][1] = src[i+1][0]
	}

	return result
}
