package p0

import (
	"fmt"
	"sort"
	"time"

	s "go-problems/shared"
)

// OEJProblems ...
type OEJProblems struct {
	set []*OEJ
}

// Solve ...
func (p *OEJProblems) Solve() {
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

	fmt.Println("Algorithm finished in:", time.Since(start))
}

// OEJ ...
type OEJ struct {
	data   []int
	output int
}

// CreateOEJ ...
func CreateOEJ() s.Problem {
	set := make([]*OEJ, 0, 4)

	set = append(set, &OEJ{
		data:   []int{2, 3, 1, 1, 4},
		output: 3,
	})

	return &OEJProblems{set}
}

func (p *OEJ) solve() int {
	return oddEvenJumps(p.data)
}

// Build the jumping array, then rebuild the list of the
// starting points. Use the condition: we can only jump
// forward to speed up
func oddEvenJumps(A []int) int {
	size := len(A)
	vals := make([][]int, size)

	hiNext := make(map[int]int)
	loNext := make(map[int]int)
	stack := make([]int, size)

	for i := range A {
		vals[i] = []int{A[i], i}
	}

	sort.Slice(vals, func(i, j int) bool {
		if vals[i][0] == vals[j][0] {
			return vals[i][1] < vals[j][1]
		}

		return vals[i][0] < vals[j][0]
	})

	stack[0] = vals[size-1][1]
	buildOEJ(vals, stack, size, hiNext)

	sort.Slice(vals, func(i, j int) bool {
		if vals[i][0] == vals[j][0] {
			return vals[i][1] < vals[j][1]
		}

		return vals[i][0] > vals[j][0]
	})

	stack[0] = vals[size-1][1]
	buildOEJ(vals, stack, size, loNext)

	odd := make([]bool, size)
	even := make([]bool, size)

	odd[size-1] = true
	even[size-1] = true

	for i := size - 2; i >= 0; i-- {
		if next, ok := hiNext[i]; ok {
			odd[i] = even[next]
		}

		if next, ok := loNext[i]; ok {
			even[i] = odd[next]
		}
	}

	fmt.Println(hiNext, loNext)

	sum := 0
	for _, v := range odd {
		if v {
			sum++
		}
	}

	return sum
}

func buildOEJ(vals [][]int, stack []int, size int, jump map[int]int) {
	si := 1

	for i := size - 2; i >= 0; i-- {
		idx := vals[i][1]

		if si == 0 {
			stack[si] = idx
			si++
		} else if idx < stack[si-1] {
			jump[idx] = stack[si-1]
			stack[si] = idx
			si++
		} else {
			for si > 0 && idx > stack[si-1] {
				si--
			}

			stack[si] = idx
			if si > 0 {
				jump[idx] = stack[si-1]
			}

			si++
		}
	}
}
