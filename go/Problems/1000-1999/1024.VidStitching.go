package problems

import (
	"fmt"
	"sort"

	d "../../Utils"
)

// VS ...
type VS struct {
	source [][]int
	target int
	output int
}

// CreateVS ...
func CreateVS() *VS {
	return &VS{
		source: nil,
		target: 0,
		output: 0,
	}
}

// Build ...
func (p *VS) Build(test int) {
	switch test {
	case 1:
		p.source = [][]int{{0, 1}, {1, 2}}
		p.target = 5
		p.output = -1

	case 2:
		p.source = [][]int{
			{0, 1}, {6, 8}, {0, 2}, {5, 6}, {0, 4}, {0, 3}, {6, 7}, {1, 3}, {4, 7},
			{1, 4}, {2, 5}, {2, 6}, {3, 4}, {4, 5}, {5, 7}, {6, 9},
		}

		p.target = 9
		p.output = 3

	case 3:
		p.source = [][]int{{0, 4}, {2, 8}}
		p.target = 5
		p.output = 2

	default:
		p.source = [][]int{{0, 2}, {4, 6}, {8, 10}, {1, 9}, {1, 5}, {5, 9}}
		p.target = 10
		p.output = 3

	}
}

// Run ...
func (p *VS) Run() {
	sort.Slice(p.source, func(i, j int) bool {
		if p.source[i][0] != p.source[j][0] {
			return p.source[i][0] < p.source[j][0]
		}

		return p.source[i][1] > p.source[j][1]
	})

	fmt.Println("Expected clips to merge: ", p.output)
	fmt.Println("Calculated result: ", p.merge())
}

// return found
func (p *VS) merge() int {
	size := len(p.source)
	if size < 1 {
		return -1
	}

	if p.source[0][0] != 0 {
		return -1
	}

	if size == 1 {
		if p.source[0][1] < p.target {
			return -1
		}

		return 1
	}

	count := 1
	clip := p.source[0]
	d.Debug(fmt.Sprintf("Starting with: %v", p.source[0]), 0)

	i := 1
	var next int
	for i < len(p.source) {
		if clip[1] >= p.target {
			// done
			return count
		}

		if p.source[i][0] > clip[1] {
			// can't merge this clip
			break
		}

		if p.source[i][1] <= clip[1] {
			// clip already covered by what we have
			i++
			continue
		}

		// search for the next clip to merge
		next, i = p.search(clip[1], i)
		if next == -1 {
			return -1
		}

		// found the correct clip to merge, count++
		clip[1] = next
		count++
	}

	if clip[1] >= p.target {
		return count
	}

	return -1
}

// return end (top_val, last_index)
func (p *VS) search(lastPos int, start int) (int, int) {
	index := start
	loc := start
	top := -1

	for index < len(p.source) {
		if p.source[index][0] > lastPos {
			break
		}

		if p.source[index][1] > top {
			top = p.source[index][1]
			loc = index
		}

		index++
	}

	d.Debug(fmt.Sprintf("Merging: %v", p.source[loc]), 0)

	return top, index
}
