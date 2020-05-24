package p1

import (
	"fmt"
	"math/rand"
	"time"

	s "go-problems/shared"
)

// MTCAProblems ...
type MTCAProblems struct {
	set []*MTCA
}

// Solve ...
func (p *MTCAProblems) Solve() {
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

// MTCA ...
type MTCA struct {
	data      [][]int
	n         int
	hasApples []bool
	output    int
}

// CreateMTCA ...
func CreateMTCA() s.Problem {
	set := make([]*MTCA, 0, 4)

	set = append(set, &MTCA{
		data:      [][]int{{0, 1}, {0, 2}, {1, 4}, {1, 5}, {2, 3}, {2, 6}},
		n:         7,
		hasApples: []bool{false, false, true, false, true, true, false},
		output:    8,
	})

	set = append(set, &MTCA{
		data:      [][]int{{0, 1}, {0, 2}, {1, 4}, {1, 5}, {2, 3}, {2, 6}},
		n:         7,
		hasApples: []bool{false, false, true, false, false, true, false},
		output:    6,
	})

	set = append(set, &MTCA{
		data:      [][]int{{0, 1}, {0, 2}, {1, 4}, {1, 5}, {2, 3}, {2, 6}},
		n:         7,
		hasApples: []bool{false, false, false, false, false, false, false},
		output:    0,
	})

	testMergeSort()

	return &MTCAProblems{set}
}

func testMergeSort() {
	var a s.MergeSort

	size := 250
	r1 := rand.New(rand.NewSource(time.Now().UnixNano()))
	vals := make(map[int]bool)

	a = make([]int, size)
	for i := 0; i < size; i++ {
		val := r1.Intn(5 * size)

		for vals[val] {
			val = r1.Intn(5 * size)
		}

		vals[val] = true
		a[i] = val
	}

	fmt.Println("before sort:", a)

	a.Sort(0, size-1)

	fmt.Println("post sort:", a)

	for i := 1; i < size; i++ {
		if a[i] <= a[i-1] {
			fmt.Println("invalid position:", i)
		}
	}

	fmt.Println("validation done ... ")
}

func (p *MTCA) solve() int {
	edges := make(map[int][]int)

	for i := 0; i < len(p.data); i++ {
		from, to := p.data[i][0], p.data[i][1]
		edges[from] = append(edges[from], to)
	}

	has, count := p.walk(edges, 0, 0)

	if !has {
		return 0
	}

	return count
}

func (p *MTCA) walk(edges map[int][]int, root, steps int) (bool, int) {
	leaves := edges[root]
	size := len(leaves)

	if size == 0 {
		if p.hasApples[root] {
			return true, steps
		}

		return false, 0
	}

	hasApple := p.hasApples[root]

	for i := 0; i < size; i++ {
		has, count := p.walk(edges, leaves[i], 2)

		if has {
			steps += count
			hasApple = true
		}
	}

	return hasApple, steps
}
