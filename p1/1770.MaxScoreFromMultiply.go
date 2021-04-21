package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MSFMProblems ...
type MSFMProblems struct {
	set []*MSFM
}

// Solve ...
func (p *MSFMProblems) Solve() {
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

// MSFM ...
type MSFM struct {
	data   []int
	multi  []int
	output int
}

// CreateMSFM ...
func CreateMSFM() s.Problem {
	set := make([]*MSFM, 0, 4)

	set = append(set, &MSFM{
		data:   []int{1, 2, 3},
		multi:  []int{3, 2, 1},
		output: 14,
	})

	set = append(set, &MSFM{
		data:   []int{-5, -3, -3, -2, 7, 1},
		multi:  []int{-10, -5, 3, 4, 6},
		output: 102,
	})

	return &MSFMProblems{set}
}

func (p *MSFM) solve() int {
	m := len(p.multi)
	n := len(p.data)

	dp := make([]int, 0, m)
	tmp := make([]int, 0, m)

	arr := p.data
	multi := p.multi[m-1]

	for i := 0; i < m; i++ {
		dp = append(dp, max(multi*arr[i], multi*arr[i+n-m]))
	}

	// fmt.Println(dp)

	bound := n - m
	for i := m - 2; i >= 0; i-- {
		multi = p.multi[i]
		bound++

		l, r := 0, bound
		for r < n {
			tmp = append(tmp, max(dp[l]+multi*arr[r], dp[l+1]+multi*arr[l]))
			l++
			r++
		}

		dp, tmp = tmp, dp
		tmp = tmp[:0]
	}

	return dp[0]
}
