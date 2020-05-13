package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CTTAProblems ...
type CTTAProblems struct {
	set []*CTTA
}

// Solve ...
func (p *CTTAProblems) Solve() {
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

// CTTA ...
type CTTA struct {
	data   []int
	output int
}

// CreateCTTA ...
func CreateCTTA() s.Problem {
	set := make([]*CTTA, 0, 4)

	set = append(set, &CTTA{
		data:   []int{2, 3, 1, 6, 7},
		output: 4,
	})

	set = append(set, &CTTA{
		data:   []int{1, 1, 1, 1, 1},
		output: 10,
	})

	set = append(set, &CTTA{
		data:   []int{2, 3},
		output: 0,
	})

	set = append(set, &CTTA{
		data:   []int{1, 3, 5, 7, 9},
		output: 3,
	})

	set = append(set, &CTTA{
		data:   []int{7, 11, 12, 9 ,5, 2, 7, 17, 22},
		output: 8,
	})

	return &CTTAProblems{set}
}

func (p *CTTA) solve() int {
	size := len(p.data)
	count := 0

	cache := make(map[int][]int)
	cache[0] = []int{1, -1}
	sum := make([]int, 0, size + 1)

	sum = append(sum, 0)
	for i := 0; i < size; i++ {
		val := sum[i] ^ p.data[i]

		if data, ok := cache[val]; ok {
			count += data[0] * (i - 1) - data[1]
			data[0]++
			data[1] += i
		} else {
			cache[val] = []int{1, i}
		}

		sum = append(sum, val)
	}

	if s.DebugMode() {
		fmt.Println(cache, sum)		
	}

	return count
}
