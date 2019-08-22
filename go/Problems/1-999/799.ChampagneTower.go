package problems

import (
	"fmt"

	d "../../Utils"
)

// CT ...
type CT struct {
	source int
	row    int
	glass  int
	output float32
}

// CreateCT ...
func CreateCT() *CT {
	return &CT{}
}

// Build ...
func (p *CT) Build(test int) {
	switch test {
	case 1:
		p.source = 2
		p.row = 1
		p.glass = 1
		p.output = 0.5

	case 2:
		p.source = 15
		p.row = 5
		p.glass = 3
		p.output = 0.875

	default:
		p.source = 1
		p.row = 1
		p.glass = 1
		p.output = 0.0

	}
}

// Run ...
func (p *CT) Run() {
	size := p.row + 1
	tower := make([][]float32, size)

	for i := 0; i < size; i++ {
		tower[i] = make([]float32, size)
	}

	tower[0][0] = float32(p.source)
	tower = p.outflow(tower, size)

	if d.DEBUG {
		for _, row := range tower {
			fmt.Println(row)
		}
	}

	fmt.Println("Calculated result: ", tower[p.row][p.glass])
	fmt.Println("Expected result: ", p.output)
}

func (p *CT) outflow(tower [][]float32, size int) [][]float32 {
	var remainder float32
	var spill int

	for i := 0; i < size; i++ {
		spill = 0
		for j := 0; j < i+1; j++ {
			remainder = tower[i][j] - 1.0
			if remainder > 0 {
				// can only hold 1 glass of wine in this glass
				tower[i][j] = 1.0
				spill++

				// early return, the glass is full
				if i == p.row && j == p.glass {
					return tower
				}

				// if the last row, spill will flow out of the system, no need for book-keeping
				if i == size-1 {
					continue
				}

				// update the layer below
				tower[i+1][j] += remainder / 2.0
				tower[i+1][j+1] += remainder / 2.0
			}
		}

		// not spilling to the row below, we're good
		if spill == 0 {
			break
		}
	}

	return tower
}
