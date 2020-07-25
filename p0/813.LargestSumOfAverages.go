package p0

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// LSOAProblems ...
type LSOAProblems struct {
	set []*LSOA
}

// Solve ...
func (p *LSOAProblems) Solve() {
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

// LSOA ...
type LSOA struct {
	data   []int
	k      int
	output int
}

// CreateLSOA ...
func CreateLSOA() s.Problem {
	set := make([]*LSOA, 0, 4)

	set = append(set, &LSOA{
		data:   []int{9,1,2,3,9,},
		k:      3,
		output: 0,
	})

	return &LSOAProblems{set}
}

func (p *LSOA) solve() float64 {
	return largestSumOfAverages(p.data, p.k)
}

func largestSumOfAverages(A []int, K int) float64 {
  size := len(A)
  prefix := make([]int, size+1)

  for i := range A {
    prefix[i+1] = prefix[i] + A[i]
  }

  if K == size {
    return float64(prefix[size])
  }

  dp := make([][]float64, K)

  for i := range dp {
    if i == 0 {
      dp[0] = make([]float64, size)

      for j := range dp[0] {
        dp[0][j] = float64(prefix[j+1]) / float64(j+1)
      }
    } else {
      dp[i] = make([]float64, size)
    }
  }

  if K == 1 {
    return dp[0][size-1]
  }

  for i := 1; i < K; i++ {
    for j := i; j < size; j++ {
      for k := j-1; k >= i-1; k-- {
        sum := dp[i-1][k] + avg(prefix, k+1, j)

        if dp[i][j] == 0 || dp[i][j] < sum {
          dp[i][j] = sum
        }
      }
    }
  }

  return dp[K-1][size-1]
}

func avg(prefix []int, i, j int) float64 {
  return float64(prefix[j+1] - prefix[i]) / float64(j - i  + 1)
}