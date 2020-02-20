package p1

import (
	"fmt"
	s "go-problems/shared"
	"sort"
	"time"
)

var count = 0

// MNEProblems ...
type MNEProblems struct {
	set []*MNE
}

// Solve ...
func (p *MNEProblems) Solve() {
	fmt.Println()

	start := time.Now()

	for j := 0; j <= count; j++ {
		for i, p := range p.set {
			result := p.solve()

			if j == count {
				s.Print(i, p.output, result)
			}
		}
	}

	fmt.Println("Algorithm took", time.Since(start))
}

// MNE ...
type MNE struct {
	data   [][]int
	output int
}

// CreateMNE ...
func CreateMNE() s.Problem {
	set := make([]*MNE, 0, 4)

	set = append(set, &MNE{
		data: [][]int{
			{1, 2}, {2, 3}, {3, 4},
		},
		output: 3,
	})

	set = append(set, &MNE{
		data: [][]int{
			{1, 2}, {2, 3}, {3, 4}, {1, 2},
		},
		output: 4,
	})

	set = append(set, &MNE{
		data: [][]int{
			{1, 4}, {4, 4}, {2, 2}, {3, 4}, {1, 1},
		},
		output: 4,
	})

	set = append(set, &MNE{
		data: [][]int{
			{1, 100000},
		},
		output: 1,
	})

	set = append(set, &MNE{
		data: [][]int{
			{1, 1}, {1, 2}, {1, 3}, {1, 4}, {1, 5}, {1, 6}, {1, 7},
		},
		output: 7,
	})

	set = append(set, &MNE{
		data: [][]int{
			{1, 5}, {2, 3}, {2, 3}, {1, 5}, {1, 5},
		},
		output: 5,
	})

	set = append(set, &MNE{
		data: [][]int{
			{1, 4}, {1, 1}, {2, 2}, {3, 4}, {4, 4},
		},
		output: 4,
	})

	return &MNEProblems{set}
}

func (p *MNE) solve() int {
	data, size := p.data, len(p.data)

	sort.SliceStable(data, func(i, j int) bool {
		if data[i][1] != data[j][1] {
			return data[i][1] < data[j][1]
		}

		return data[i][0] < data[j][0]
	})

	if s.DebugMode() {
		fmt.Println(data)
	}

	seen := make([]int, data[size-1][1])
	seen[0]++
	count := 1

	for i := 1; i < size; i++ {
		for j := data[i][0]; j <= data[i][1]; j++ {
			if seen[j-1] > 0 {
				continue
			}

			seen[j-1]++
			count++

			break
		}
	}

	return count
}
