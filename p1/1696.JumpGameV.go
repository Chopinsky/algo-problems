package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// JGVProblems ...
type JGVProblems struct {
	set []*JGV
}

// Solve ...
func (p *JGVProblems) Solve() {
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

// JGV ...
type JGV struct {
	data   []int
	k      int
	output int
}

// CreateJGV ...
func CreateJGV() s.Problem {
	set := make([]*JGV, 0, 4)

	set = append(set, &JGV{
		data:   []int{1, -1, -2, 4, -7, 3},
		k:      2,
		output: 7,
	})

	set = append(set, &JGV{
		data:   []int{10, -5, -2, 4, 0, 3},
		k:      3,
		output: 17,
	})

	set = append(set, &JGV{
		data:   []int{1, -5, -20, 4, -1, 3, -6, -3},
		k:      2,
		output: 0,
	})

	return &JGVProblems{set}
}

func (p *JGV) solve() int {
	nums, k := p.data, p.k
	size := len(nums)

	dp := make([]int, size)
	dp[0] = nums[0]

	stack := make([][]int, 0, size)
	stack = append(stack, []int{0, dp[0]})

	for i := 1; i < size; i++ {
		idx := 0
		for idx < len(stack) && stack[idx][0] < i-k {
			idx++
		}

		stack = stack[idx:]

		if len(stack) == 0 {
			dp[i] = nums[i]
		} else {
			dp[i] = nums[i] + stack[0][1]
		}

		idx = len(stack) - 1
		for idx >= 0 && (stack[idx][0] < i-k || stack[idx][1] <= dp[i]) {
			idx--
		}

		stack = stack[:idx+1]
		stack = append(stack, []int{i, dp[i]})
	}

	return dp[size-1]
}
