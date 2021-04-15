package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// SGVIIProblems ...
type SGVIIProblems struct {
	set []*SGVII
}

// Solve ...
func (p *SGVIIProblems) Solve() {
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

// SGVII ...
type SGVII struct {
	data   []int
	output int
}

// CreateSGVII ...
func CreateSGVII() s.Problem {
	set := make([]*SGVII, 0, 4)

	set = append(set, &SGVII{
		data:   []int{5, 3, 1, 4, 2},
		output: 6,
	})

	set = append(set, &SGVII{
		data:   []int{7, 90, 5, 1, 100, 10, 10, 2},
		output: 122,
	})

	return &SGVIIProblems{set}
}

func (p *SGVII) solve() int {
	stones := p.data
	size := len(p.data)
	presum := make([]int, size+1)

	for i, s := range stones {
		presum[i+1] = presum[i] + s
	}

	dp := make([][]int, size)
	for i := range dp {
		dp[i] = make([]int, size)
	}

	for i := 0; i < size-1; i++ {
		dp[i][i+1] = max(stones[i], stones[i+1])
	}

	// idea is bottom-up dp: calculate the end games: [0,1], [1,2], ...
	// [n-1,n] for dp[i][i+1], calculate the relative strength for the
	// current player, than move up with the previous play, which is
	// [0,2], [1,3], ..., [n-2,n], where the game can be generated from
	// stone[i]+[i+1,i+k], or game [i,i+k-1]+stone[k], and we just make
	// sure the score from this play - the previous best relative strength
	// is the highest / optimal for the current player; the current score
	// is (all stones with in the range, except the one taken off) - (the
	// best strength from the resulting range), former == "total - stone
	// that's taken off", the last equals dp[last-start][last-end].
	for l := 3; l <= size; l++ {
		for i := 0; i+l <= size; i++ {
			// fmt.Println("line:", l, i, i+l-1, dp[i][i+l-2], dp[i+1][i+l-1], size)

			total := presum[i+l] - presum[i]
			dp[i][i+l-1] = max(total-stones[i]-dp[i+1][i+l-1], total-stones[i+l-1]-dp[i][i+l-2])
		}
	}

	// fmt.Println(dp)

	return dp[0][size-1]
}
