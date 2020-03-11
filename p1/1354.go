package p1

import (
	"fmt"
	"time"

	s "../shared"
	sp "../support"
)

// CTAProblems ...
type CTAProblems struct {
	set []*CTA
}

// Solve ...
func (p *CTAProblems) Solve() {
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

// CTA ...
type CTA struct {
	data   []int
	output int
}

// CreateCTA ...
func CreateCTA() s.Problem {
	set := make([]*CTA, 0, 4)

	set = append(set, &CTA{
		data:   []int{9, 3, 5},
		output: 1,
	})

	set = append(set, &CTA{
		data:   []int{1, 1, 1, 2},
		output: 0,
	})

	set = append(set, &CTA{
		data:   []int{8, 5},
		output: 1,
	})

	return &CTAProblems{set}
}

func (p *CTA) solve() int {
	sum, size := 0, len(p.data)
	for i := 0; i < size; i++ {
		sum += p.data[i]
	}

	heap := sp.BuildHeap(p.data, true)
	found := 0

	for {
		val := heap.Pop()

		// not going to finish ...
		if 2*val-sum <= 0 {
			break
		}

		// skipping a couple of middle states to find the final value
		next := sum % (sum - val)

		if next == 0 {
			// the next value is the muliply of the excluding-self-sum, use the least val here
			next = sum - val
		}

		// calc the new sum
		sum -= val - next

		// check if we're getting the initial array: all 1s
		if sum == size {
			found = 1
			break
		}

		heap.Push(next)
	}

	return found
}
