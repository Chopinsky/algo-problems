package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// CSSProblems ...
type CSSProblems struct {
	set []*CSS
}

// Solve ...
func (p *CSSProblems) Solve() {
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

// CSS ...
type CSS struct {
	data   []int
	k      int
	output int
}

// CreateCSS ...
func CreateCSS() s.Problem {
	set := make([]*CSS, 0, 4)

	set = append(set, &CSS{
		data:   []int{10, 2, -10, 5, 20},
		k:      2,
		output: 37,
	})

	set = append(set, &CSS{
		data:   []int{-1, -2, -3},
		k:      1,
		output: -1,
	})

	set = append(set, &CSS{
		data:   []int{10, -2, -10, -5, 20},
		k:      2,
		output: 23,
	})

	return &CSSProblems{set}
}

func (p *CSS) solve() int {
	size := len(p.data)
	
	dp := make([]int, size)
	dp[0] = p.data[0]

	queue := make([]int, 0, p.k * size)
	queue = append(queue, 0)

	max := dp[0]

	for i := 1; i < size; i++ {
		qLen := len(queue)

		if i > p.k && qLen > 0 && queue[0] == i - p.k - 1 {
			queue = queue[1:]
			qLen--
		}

		dp[i] = p.data[i]

		if qLen > 0 {
			front := queue[0]
			if dp[front] > 0 {
				dp[i] += dp[front]
			}
		}

		if dp[i] > max {
			max = dp[i]
		}

		if s.DebugMode() {
			fmt.Println(i, dp[i], queue)
		}

		backIdx := qLen - 1
		for backIdx >= 0 && dp[i] >= dp[queue[backIdx]] {
			backIdx--
		}

		if backIdx != qLen - 1 {
			queue = queue[:backIdx+1]
		}

		queue = append(queue, i)
	}

	return max
}

func (p *CSS) solve1() int {
	size := len(p.data)
	dp := make([]int, size)
	heap := s.InitHeap(size)

	dp[0] = p.data[0]
	max := dp[0]
	heap.Push([]int{0, p.data[0]})

	for i := 1; i < size; i++ {
		dp[i] = p.data[i]

		/*
			 * Brutal force solution
			pos := i - 1
			for pos >= 0 && i-pos <= p.k {
				tgt := dp[pos] + p.data[i]

				if tgt >= dp[i] {
					dp[i] = tgt
				}

				pos--
			}
		*/

		largest := heap.Peek()[1]

		if largest > 0 {
			dp[i] += largest
		}

		if i == 0 || dp[i] > max {
			max = dp[i]
		}

		if i < p.k {
			heap.Push([]int{i, dp[i]})
		} else {
			heap.Update(i-p.k, []int{i, dp[i]})
		}

		if s.DebugMode() {
			fmt.Println(i, largest, dp[i])
			heap.Debug()
		}
	}

	return max
}
