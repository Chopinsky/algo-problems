package p1

import (
	"fmt"
	"time"

	s "go-problems/shared"
)

// TRWTFSProblems ...
type TRWTFSProblems struct {
	set []*TRWTFS
}

// Solve ...
func (p *TRWTFSProblems) Solve() {
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

// TRWTFS ...
type TRWTFS struct {
	m      int
	n      int
	output int
}

// CreateTRWTFS ...
func CreateTRWTFS() s.Problem {
	set := make([]*TRWTFS, 0, 4)

	set = append(set, &TRWTFS{
		m: 13,
		n: 11,
		output: 6,
	})

	return &TRWTFSProblems{set}
}

func (p *TRWTFS) solve() int {
	return tilingRectangle(p.n, p.m)
}

func tilingRectangle(n int, m int) int {
  if m == n {
    return 1
  }

  if m == 1 {
    return n
  }

  if n == 1 {
    return m
  }

  m, n = shuffle(m, n)
  dp := make([][]int, m+1)

  for i := range dp {
    dp[i] = make([]int, n+1)

    if i == 1 {
      for j := range dp[i] {
        dp[1][j] = j
      }
    } else {
      dp[i][1] = i
    }

    if i <= m {
      dp[i][i] = 1
    }
  }

  val := findSquares(m, n, dp)

  // for i := range dp{
  //   fmt.Println(dp[i])
  // }

  return val
}

func findSquares(m, n int, dp [][]int) int {
  if m == 0 || n == 0 {
    return 0
  }

  if m == n {
    return 1
  }

  m, n = shuffle(m, n)

  if dp[m][n] > 0 {
    return dp[m][n]
  }

  best := -1

  for i := 1; i <= m; i++ {
    for j := m - i; j + i <= n && j <= m; j++ {
      // base bottom-left square
      val := 1

      if j > 0 {
        // if top-right square exists
        val++
      }

      if m - i > 0 {
        // top-left square
        c := findSquares(m-i, n-j, dp)

        // if i == 7 && j == 5 {
        //   fmt.Println("t-l", m-i, n-j, c)
        // }

        val += c
      }

      if m - j > 0 {
        // bottom-right square
        c := findSquares(m-j, n-i, dp)

        // if i == 7 && j == 5 {
        //   fmt.Println("b-r", m-j, n-i, c)
        // }

        val += c
      }

      if i + j - m > 0 && n - i - j > 0 {
        // mid-mid square
        c := findSquares(i+j-m, n-i-j, dp)

        // if i == 7 && j == 5 {
        //   fmt.Println("mid", c)
        // }

        val += c
      }

      // if m == 11 && n == 13 {
      //   fmt.Println(i, j, val)
      // }

      if best == -1 || best > val {
        best = val
      }
    }
  }

  dp[m][n] = best

  return best
}

func shuffle(a, b int) (int, int) {
  if a > b {
    return b, a
  }

  return a, b
}
