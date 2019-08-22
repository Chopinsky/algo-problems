package problems

import d "../../Utils"

// PL ...
type PL struct {
	source string
	output []int
}

// CreatePL ...
func CreatePL() *PL {
	return &PL{}
}

// Build ...
func (p *PL) Build(test int) {
	switch test {
	default:
		p.source = "ababcbacadefegdehijhklij"
		p.output = []int{9, 7, 8}

	}
}

// Run ...
func (p *PL) Run() {
	d.Output(p.findBounds(), p.output)
}

func (p *PL) findBounds() []int {
	// build the auxillary data structures
	indices := make(map[int]int) // last pos the char appears
	store := [][]int{}           // first pos the char appears

	for i, r := range p.source {
		char := int(r)
		if _, ok := indices[char]; !ok {
			// first time saw this element, push to the array in order
			store = append(store, []int{char, i})
		}

		// set the last pos index where the character appears
		indices[char] = i
	}

	// now find the partition bounds
	bounds := []int{}
	char := store[0][0]
	last := indices[char]
	var charLast int

	for i := 1; i < len(store); i++ {
		char = store[i][0]
		charLast = indices[char]

		if store[i][1] > last {
			// we've found a min-partition bound, push the result
			bounds = append(bounds, last)
			last = charLast
		} else if charLast > last {
			// the char push back the bound
			last = charLast
		}

		// the bound is last char, the remainder is in the last segment
		if last == len(p.source)-1 {
			break
		}
	}

	bounds = append(bounds, last)
	result := make([]int, len(bounds))

	// update to the number of char in the segments
	for i := range bounds {
		if i == 0 {
			result[0] = bounds[0] + 1
		} else {
			result[i] = bounds[i] - bounds[i-1]
		}
	}

	return result
}
