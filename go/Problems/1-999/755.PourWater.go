package problems

import d "../../Utils"

// PWT ...
type PWT struct {
	source []int
	vol    int
	index  int
	output []int
}

// CreatePWT ...
func CreatePWT() *PWT {
	return &PWT{}
}

// Build ...
func (p *PWT) Build(test int) {
	switch test {
	case 1:
		p.source = []int{1, 2, 3, 4}
		p.vol = 2
		p.index = 2
		p.output = []int{2, 3, 3, 4}

	case 2:
		p.source = []int{3, 1, 3}
		p.vol = 5
		p.index = 1
		p.output = []int{4, 4, 4}

	default:
		p.source = []int{2, 1, 1, 2, 1, 2, 2}
		p.vol = 4
		p.index = 3
		p.output = []int{2, 2, 2, 3, 2, 2, 2}

	}
}

// Run ...
func (p *PWT) Run() {
	p.pour()
	d.Output(p.source, p.output)
}

func (p *PWT) pour() {
	for i := 0; i < p.vol; i++ {
		p.source[move(p.index, p.source)]++
	}
}

func move(start int, cup []int) int {
	// move left
	for i := start - 1; i >= 0; i-- {
		if cup[i] > cup[start] {
			break
		}

		if cup[i] < cup[start] {
			return i
		}
	}

	// move right
	for i := start + 1; i < len(cup); i++ {
		if cup[i] > cup[start] {
			break
		}

		if cup[i] < cup[start] {
			return i
		}
	}

	// can't move, return start
	return start
}
