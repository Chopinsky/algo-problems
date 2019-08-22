package problems

import (
	"strconv"

	d "../../Utils"
)

var visited map[int]bool

// OTL ...
type OTL struct {
	source []string
	target string
	output int
}

// CreateOTL ...
func CreateOTL() *OTL {
	return &OTL{}
}

// Build ...
func (p *OTL) Build(test int) {
	switch test {
	case 1:
		p.source = []string{"8888"}
		p.target = "0009"
		p.output = 1

	case 2:
		p.source = []string{"8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"}
		p.target = "8888"
		p.output = -1

	default:
		p.source = []string{"0201", "0101", "0102", "1212", "2002"}
		p.target = "0202"
		p.output = 6

	}
}

// Run ...
func (p *OTL) Run() {
	buildDeadend(p.source)
	target, _ := strconv.Atoi(p.target)

	if checkDeadlock(target) {
		d.Output(-1, p.output)
		return
	}

	d.Output(check(target), p.output)
}

func buildDeadend(list []string) {
	visited = make(map[int]bool, 10000)
	for i := range list {
		if num, err := strconv.Atoi(list[i]); err == nil {
			visited[num] = true
		}
	}
}

func check(target int) int {
	done, count := false, 0
	combos := []int{0}
	visited[0] = true

	for len(visited) < 10000 {
		combos, done = rotateWheel(combos, target)
		count++

		if done {
			return count
		}

		if len(combos) == 0 {
			return -1
		}
	}

	return -1
}

func checkDeadlock(target int) bool {
	var turnLeft bool
	var next int

	for j := 0; j < 4; j++ {
		for k := 0; k < 2; k++ {
			next = nextWheel(target, j, turnLeft)
			turnLeft = !turnLeft

			if !visited[next] {
				return false
			}
		}
	}

	return true
}

func rotateWheel(combos []int, target int) ([]int, bool) {
	temp := make([]int, 0, 4*len(combos))
	var next int
	var turnLeft bool

	for i := range combos {
		for j := 0; j < 4; j++ {
			for k := 0; k < 2; k++ {
				next = nextWheel(combos[i], j, turnLeft)
				turnLeft = !turnLeft

				if next == target {
					return temp, true
				}

				if !visited[next] {
					temp = append(temp, next)
					visited[next] = true
				}
			}
		}
	}

	return temp, false
}

func nextWheel(lock int, pos int, turnLeft bool) int {
	base, num := 1, lock
	for i := pos; i > 0; i-- {
		num /= 10
		base *= 10
	}

	// if turning left
	if turnLeft {
		if num%10 == 0 {
			return lock + 9*base
		}

		return lock - base
	}

	// if turning right
	if num%10 == 9 {
		return lock - 9*base
	}

	return lock + base
}
