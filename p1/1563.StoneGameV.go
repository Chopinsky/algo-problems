package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SGVProblems ...
type SGVProblems struct {
	set []*SGV
}

// Solve ...
func (p *SGVProblems) Solve() {
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

// SGV ...
type SGV struct {
	data   []int
	output int
}

// CreateSGV ...
func CreateSGV() s.Problem {
	set := make([]*SGV, 0, 4)

	set = append(set, &SGV{
		data:   []int{6, 2, 3, 4, 5, 5},
		output: 18,
	})

	set = append(set, &SGV{
		data:   []int{7, 7, 7, 7, 7, 7, 7},
		output: 28,
	})

	set = append(set, &SGV{
		data:   []int{4},
		output: 0,
	})

	return &SGVProblems{set}
}

func (p *SGV) solve() int {
	size := len(p.data)
	if size <= 1 {
		return 0
	}

	if size == 2 {
		return min(p.data[0], p.data[1])
	}

	presum := make([]int, size+1)
	for i := range p.data {
		presum[i+1] = presum[i] + p.data[i]
	}

	dp := make([][]int, size)
	for i := range dp {
		dp[i] = make([]int, size)
		dp[i][i] = p.data[i]

		if i > 0 {
			// best scores for 2 stones
			dp[i-1][i] = min(dp[i][i], dp[i-1][i-1]) + dp[i][i] + dp[i-1][i-1]
		}
	}

	ans := calcSGV(dp, presum, 0, size-1) - presum[size]

	// for i := range dp {
	// 	fmt.Println(dp[i])
	// }

	return ans
}

func calcSGV(dp [][]int, presum []int, l, r int) int {
	if dp[l][r] > 0 {
		return dp[l][r]
	}

	ans := 0
	var lscore, rscore, score int

	for k := l; k < r; k++ {
		lscore = presum[k+1] - presum[l]
		rscore = presum[r+1] - presum[k+1]

		if lscore == rscore {
			ltotal := calcSGV(dp, presum, l, k)
			rtotal := calcSGV(dp, presum, k+1, r)
			score = max(ltotal, rtotal)
		} else if lscore > rscore {
			score = calcSGV(dp, presum, k+1, r)
		} else {
			score = calcSGV(dp, presum, l, k)
		}

		if score > ans {
			ans = score
		}
	}

	dp[l][r] = ans + presum[r+1] - presum[l]
	return dp[l][r]
}
