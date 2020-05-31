package p1

import (
	"fmt"
	"strconv"
	"time"

	s "go-problems/shared"
)

// PPPBTProblems ...
type PPPBTProblems struct {
	set []*PPPBT
}

// Solve ...
func (p *PPPBTProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= 0; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == 0 {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// PPPBT ...
type PPPBT struct {
	data   []int
	output int
}

// CreatePPPBT ...
func CreatePPPBT() s.Problem {
	set := make([]*PPPBT, 0, 4)

	set = append(set, &PPPBT{
		data:   []int{2, 3, 1, 3, 1, 0, 1},
		output: 2,
	})

	set = append(set, &PPPBT{
		data:   []int{2, 1, 1, 1, 3, 0, 0, 0, 0, 0, 1},
		output: 1,
	})

	set = append(set, &PPPBT{
		data:   []int{9},
		output: 1,
	})

	return &PPPBTProblems{set}
}

func (p *PPPBT) solve() int {
	return p.walk(0, 0, len(p.data))
}

func (p *PPPBT) walk(root, mask, size int) int {
	left, right := 2*root+1, 2*root+2

	// flip the bits at position of `p.data[root]`
	mask ^= 1 << uint(p.data[root])

	if s.DebugMode() {
		fmt.Println(root, strconv.FormatInt(int64(mask), 2), left >= size && right >= size)
	}

	lValid := left < size && p.data[left] > 0
	rValid := right < size && p.data[right] > 0

	// if at the leaf and the route is psudo-palindromic, add 1
	if !lValid && !rValid && (mask-(mask&-mask)) == 0 {
		return 1
	}

	count := 0

	if left < size && p.data[left] > 0 {
		count += p.walk(left, mask, size)
	}

	if right < size && p.data[right] > 0 {
		count += p.walk(right, mask, size)
	}

	return count
}
