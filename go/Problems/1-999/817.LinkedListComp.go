package problems

import (
	"fmt"

	d "../../Utils"
)

var v struct{}

// LLC ...
type LLC struct {
	source *d.Node
	target []int
	output int
}

// CreateLLC ...
func CreateLLC() *LLC {
	return &LLC{}
}

// Build ...
func (p *LLC) Build(test int) {
	switch test {
	case 1:
		p.source = d.Build([]int{0, 1, 2, 3, 4})
		p.target = []int{0, 3, 1, 4}
		p.output = 2

	default:
		p.source = d.Build([]int{0, 1, 2, 3})
		p.target = []int{0, 1, 3}
		p.output = 2

	}
}

// Run ...
func (p *LLC) Run() {
	m := make(map[int]struct{}, len(p.target))
	for _, val := range p.target {
		m[val] = v
	}

	curr := p.source
	count := 0
	isComponent := false

	for {
		if curr == nil {
			break
		}

		if _, ok := m[curr.Value()]; ok && !isComponent {
			// start a new component
			isComponent = true
		} else if isComponent {
			// update the counter since we're done with this component
			isComponent = false
			count++
		}

		curr = curr.Next()
	}

	if isComponent {
		// last components continues till the end of the list
		count++
	}

	fmt.Println("Calculated count: ", count)
	fmt.Println("Expected count: ", p.output)
}
