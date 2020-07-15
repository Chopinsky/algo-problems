package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// MSTPProblems ...
type MSTPProblems struct {
	set []*MSTP
}

// Solve ...
func (p *MSTPProblems) Solve() {
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

// MSTP ...
type MSTP struct {
	data   []int
	output int
}

// CreateMSTP ...
func CreateMSTP() s.Problem {
	set := make([]*MSTP, 0, 4)

	set = append(set, &MSTP{
		data:   []int{35,73,90,27,71,80,21,33,33,13,48,12,68,70,80,36,66,3,70,58},
		output: 140295,
	})

	return &MSTPProblems{set}
}

func (p *MSTP) solve() int {
	return wmt(p.data)
}

// see: https://en.wikipedia.org/wiki/Minimum-weight_triangulation
func wmt(a []int) int {
  size := len(a)

  dp := make([][]int, size)
  for i := range dp {
    dp[i] = make([]int, size)
  }

  for i := size-2; i >= 0; i-- {
    for j := i+1; j < size; j++ {
      if j-i == 1 {
        dp[i][j] = a[i]*a[j]
        continue
      }

      if j-i == 2 {
        dp[i][j] = a[i]*a[i+1]*a[i+2]
        continue
      }

      best := -1
      for k := i+1; k < j; k++ {
        val := a[i]*a[k]*a[j]

        if k-i > 1 {
          val += dp[i][k]
        }

        if j-k > 1 {
          val += dp[k][j]
        }

        if best == -1 || val < best {
          best = val
        }
      }

      dp[i][j] = best
    }
  }

  // for i := range dp {
  //   fmt.Println(dp[i])
  // }

  return dp[0][size-1]
}