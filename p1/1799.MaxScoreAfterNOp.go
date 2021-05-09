package p1

import (
	"fmt"
	"time"
	// "strconv"

	s "go-problems/shared"
)

// MSANOProblems ...
type MSANOProblems struct {
	set []*MSANO
}

// Solve ...
func (p *MSANOProblems) Solve() {
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

// MSANO ...
type MSANO struct {
	data   []int
	output int
}

// CreateMSANO ...
func CreateMSANO() s.Problem {
	set := make([]*MSANO, 0, 4)

	set = append(set, &MSANO{
		data:   []int{1, 2},
		output: 1,
	})

	set = append(set, &MSANO{
			data:   []int{3, 4, 6, 8},
			output: 11,
	})

	set = append(set, &MSANO{
		data:   []int{1, 2, 3, 4, 5, 6},
		output: 14,
	})

	return &MSANOProblems{set}
}

func (p *MSANO) solve() int {
	arr := p.data
	l := len(arr)

	pairs := make([]int, 0, l*l)
	stack := make(map[int]int, l*l)

	if l == 2 {
		return s.GCD(arr[0], arr[1])
	}

	dp := make(map[int]int, l)
	for i := 0; i < l; i++ {
		for j := i+1; j < l; j++ {
			score := s.GCD(arr[i], arr[j])
			pair := (1<<i) | (1<<j)
			pairs = append(pairs, pair)

			dp[pair] = score
			stack[pair] = score
		}
	}

	// fmt.Println(dp, stack)

	for i := 2; i <= l/2; i++ {
		next := make(map[int]int)

		for p, s := range stack {
			for _, pp := range pairs {
				// a number is already taken
				if pp & p > 0 {
					continue
				}

				// next pair
				np := pp | p
				score := s + i*dp[pp]

				// fmt.Println(i, np, p, pp, score)

				// update best scores
				if best, ok := next[np]; !ok || (best < score) {
					next[np] = score
				}
			}
		}

		// fmt.Println(i, round, next)

		stack = next
	}

	return stack[(1<<l)-1]
}
