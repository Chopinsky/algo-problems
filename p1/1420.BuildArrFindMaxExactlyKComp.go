package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// BAFMEKCProblems ...
type BAFMEKCProblems struct {
	set []*BAFMEKC
}

// Solve ...
func (p *BAFMEKCProblems) Solve() {
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

// BAFMEKC ...
type BAFMEKC struct {
	n int
	m int
	k int
	output int
}

// CreateBAFMEKC ...
func CreateBAFMEKC() s.Problem {
	set := make([]*BAFMEKC, 0, 4)

	set = append(set, &BAFMEKC{
		n: 2,
		m: 3,
		k: 1,
		output: 6,
	})

	set = append(set, &BAFMEKC{
		n: 5,
		m: 2,
		k: 3,
		output: 0,
	})

	set = append(set, &BAFMEKC{
		n: 9,
		m: 1,
		k: 1,
		output: 1,
	})

	set = append(set, &BAFMEKC{
		n: 50,
		m: 100,
		k: 25,
		output: 34549172,
	})

	set = append(set, &BAFMEKC{
		n: 37,
		m: 17,
		k: 7,
		output: 418930126,
	})

	return &BAFMEKCProblems{set}
}

func (p *BAFMEKC) solve() int {
	return numOfArrays(p.n, p.m, p.k)
}

// *Algo*:
// for state (i, j, k), where `i` is the array length, `j` is the
// numbers range, and `k` is the cost, the state transformation is
// defined as following:
//
// 1) (i, j, k) += j * (i-1, j, k)
//    because we can append one of the numbers in the range of `1 ~ j`
//    to each of the array from the (i-1, j, k) arrays.
//
// 2) (i, j, k) += for x in (1..=j-1) Sum((i-1, x, k-1))
//    because we can append number `j` to each of the array from the
//    (i-1, x, k-1) arrays, since this will surely add 1 to the comparison
//    cost, because `j` is greater than all numbers in (i-1, x, k-1), where
//    x is in the range of `1 ~ j-1`.
//
// initial state: (1, j, 1) = 1 for j > 0, because with array of single
// element, as long as it's larger than 0, and we're *appending* j to the
// (0, j, 1) states, which yields a single possibility of the outcome.
//
// For final results, sum all (n, x, k) for x in `1 ~ j`, because we can
// have arrays with numbers in `1 ~ x` only
func numOfArrays(n int, m int, k0 int) int {
  dp := make([][][]int, n+1)
  mod := 1000000007

  // init the dp grid
  for i := range dp {
    dp[i] = make([][]int, m+1)
    for j := range dp[i] {
      dp[i][j] = make([]int, k0+1)

      if i == 1 && j > 0 {
        dp[1][j][1] = 1
      }
    }
	}

  for i := 1; i <= n; i++ {
    for j := 1; j <= m; j++ {
      for k := 1; k <= k0; k++ {
        dp[i][j][k] = (dp[i][j][k] + j * dp[i-1][j][k]) % mod

        for jj := 1; jj < j; jj++ {
          dp[i][j][k] = (dp[i][j][k] + dp[i-1][jj][k-1]) % mod
        }
      }
    }
  }

  sum := 0
  for j := 1; j <= m; j++ {
    sum = (sum + dp[n][j][k0]) % mod
  }

  return sum
}