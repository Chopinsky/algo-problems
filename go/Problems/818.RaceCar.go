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

	case 2:
		p.target = 9996
		p.output = 43
		p.result = "..."

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
		// method 1: bfs
		//output = bfs(map[int][]int{0: []int{1}}, p.target, 0)

		// method 2: in place bfs
		// output = bfsInPlace(map[int][]int{0: []int{1}}, p.target)

		// method 3: generic search
		cache := make(map[int]int)
		output = search(p.target, cache)
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
	cache := make(map[int]map[int]bool)
	var reverse int

	for pos, speeds := range curr {
		for _, speed := range speeds {
			// if we can reach target at this run
			if pos == target || pos+speed == target {
				d.Debug(curr, 0)
				return step + 1
			}

			// forward
			insert(next, pos+speed, speed*2, target, cache)

			// backward
			if speed > 0 {
				reverse = -1
			} else {
				reverse = 1
			}

			insert(next, pos, reverse, target, cache)
		}
	}

	return bfs(next, target, step+1)
}

func bfsInPlace(curr map[int][]int, target int) int {
	cache := make(map[int]map[int]bool)
	var reverse int
	step := 0

	for {
		next := make(map[int][]int, 2*len(curr))
		step++

		for pos, speeds := range curr {
			for _, speed := range speeds {
				// if we can reach target at this run
				if pos == target || pos+speed == target {
					//d.Debug(curr, 0)
					//d.Debug(cache, 0)
					return step
				}

				// forward
				insert(next, pos+speed, speed*2, target, cache)

				// backward
				if speed > 0 {
					reverse = -1
				} else {
					reverse = 1
				}

				insert(next, pos, reverse, target, cache)
			}
		}
		curr = next
	}
}

func insert(base map[int][]int, pos, speed, target int, cache map[int]map[int]bool) {
	// trim impossible cases
	if (target > 0 && pos < 0 && speed < 0) || (target < 0 && pos > 0 && speed > 0) {
		return
	}

	if (target > 0 && (pos > 2*target || speed > 2*target)) || (target < 0 && (pos < 2*target || speed < 2*target)) {
		return
	}

	if s, ok := cache[pos]; ok {
		if _, ok := s[speed]; ok {
			return
		}

		s[speed] = true
	} else {
		inner := make(map[int]bool, 1)
		inner[speed] = true
		cache[pos] = inner
	}

	// actual insert
	base[pos] = append(base[pos], speed)
}

func search(target int, cache map[int]int) int {
	d.Debug(target, 0)

	if target <= 0 {
		return 0
	}

	if s, ok := cache[target]; ok {
		return s
	}

	step := 0
	pos := 0
	speed := 1

	// approaching the target
	for {
		step++
		pos += speed
		speed *= 2

		if pos == target {
			cache[target] = step
			return step
		}

		if pos < target && pos+speed > target {
			break
		}
	}

	// now we're close to the target --
	//   route A = before target, reset speed at position (RR), search for the remainder
	//   route B = overshoot target, then reverse and reset speed (AR), search for the remainder
	routeA := step + 2 + search(target-pos, cache)
	routeB := step + 2 + search(pos+speed-target, cache)

	final := d.Min(routeA, routeB)
	cache[target] = final

	return final
}
