package problems

import (
	"fmt"

	d "../Utils"
)

// RC ...
type RC struct {
	target int
	output int
	result string
}

// CreateRC ...
func CreateRC() *RC {
	return &RC{}
}

// Build ...
func (p *RC) Build(test int) {
	switch test {
	case 1:
		p.target = 6
		p.output = 5
		p.result = "AAARA"

	default:
		p.target = 3
		p.output = 2
		p.result = "AA"

	}
}

// Run ...
func (p *RC) Run() {
	var output int

	if p.target != 0 {
		// bfs search
		//output = bfs(map[int][]int{0: []int{1}}, p.target, 0)
		output = bfsInPlace(map[int][]int{0: []int{1}}, p.target)
	} else {
		// "RA" -- position: 0 -> 1 -> 0; speed: 1 -> -1 -> -2, output = 2
		// but really, just stay where you're, that's output = 0
		output = 0
	}

	fmt.Println("Expected steps: ", p.output)
	fmt.Println("Calculated steps: ", output)
}

func bfs(curr map[int][]int, target, step int) int {
	size := len(curr)
	next := make(map[int][]int, 2*size)
	var reverse int

	for pos, speeds := range curr {
		for _, speed := range speeds {
			// if we can reach target at this run
			if pos == target || pos+speed == target {
				d.Debug(curr, 0)
				return step + 1
			}

			// forward
			insert(next, pos+speed, speed*2, target)

			// backward
			if speed > 0 {
				reverse = -1
			} else {
				reverse = 1
			}

			insert(next, pos, reverse, target)
		}
	}

	return bfs(next, target, step+1)
}

func bfsInPlace(curr map[int][]int, target int) int {
	var reverse int
	step := 0

	for {
		next := make(map[int][]int, 2*len(curr))
		step++

		for pos, speeds := range curr {
			for _, speed := range speeds {
				// if we can reach target at this run
				if pos == target || pos+speed == target {
					d.Debug(curr, 0)
					return step
				}

				// forward
				insert(next, pos+speed, speed*2, target)

				// backward
				if speed > 0 {
					reverse = -1
				} else {
					reverse = 1
				}

				insert(next, pos, reverse, target)
			}
		}
		curr = next
	}
}

func insert(base map[int][]int, pos, speed, target int) {
	// trim impossible cases
	if target*pos < 0 && target*speed < 0 {
		return
	}

	// actual insert
	vals, ok := base[pos]
	if ok {
		vals = append(vals, speed)
	} else {
		base[pos] = []int{speed}
	}
}
